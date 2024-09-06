from textual.app import App, ComposeResult
from textual.containers import ScrollableContainer
from textual.widgets import Button, Footer, Header, Static, Input, Label, Select
import psycopg2
from control import DatabaseController

class TelaInicial(Static):
    """Tela inicial do jogo"""

    def __init__(self, db_controller: DatabaseController, **kwargs):
        super().__init__(**kwargs)
        self.db_controller = db_controller
        self.jogadores = []

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "novo_jogador":
            jogador_nome = self.query_one('#input_nome').value.replace(' ', '_')
            db_name = "Undertale5"
            #db_name = f"jogador_{jogador_nome}_db"
          #  self.db_controller.create_database(db_name)
           # self.db_controller.create_tables(db_name)
            self.db_controller.dbname = db_name  # Conectar ao banco de dados recém-criado
            self.db_controller.add_player(jogador_nome)
            self.update_jogadores_registrados()

        elif event.button.id.startswith("jogador_"):
            jogador_nome = event.button.id.split("_")[1]
            print(f"Iniciando o jogo com o jogador: {jogador_nome}")


    def update_jogadores_registrados(self):
        """Atualiza a lista de jogadores registrados"""
        self.db_controller.connect()  # Conectar ao banco de dados
        conn = self.db_controller.connection
        if conn is not None:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT nome FROM Jogador")
                self.jogadores = [row[0] for row in cursor.fetchall()]
            except psycopg2.Error as e:
                print(f"Erro ao executar a consulta: {e}")
            finally:
                cursor.close()
                self.db_controller.close()  # Fechar a conexão
            self.display_jogadores_registrados()
        else:
            print("Erro ao conectar ao banco de dados.")

    def display_jogadores_registrados(self):
        """Mostra os jogadores registrados como botões"""
        for jogador in self.jogadores:
            self.mount(Button(jogador, id=f"jogador_{jogador}"))

    def compose(self) -> ComposeResult:
        yield Label('Bem vindo ao jogo')
        yield Label("Digite o nome do novo jogador:")
        yield Input(placeholder="Nome do jogador", id="input_nome")
        yield Button('Criar Novo Jogador', id="novo_jogador")
        self.update_jogadores_registrados()
        yield Label(f"Jogadores Registrados: ")
        
class TelaJogo(Static):
    """Tela do jogo em si"""

    def __init__(self, db_controller: DatabaseController, jogador_data, **kwargs):
        super().__init__(**kwargs)
        self.db_controller = db_controller
        self.jogador_data = jogador_data

    def compose(self) -> ComposeResult:
        yield Label(f"Jogador: {self.jogador_data[1]}")
        # Adicione outros widgets necessários para o jogo aqui


class Undertale(App):
    """Aplicativo do jogo"""

    CSS_PATH = "telas.tcss"
    BINDINGS = [("^c", "quit", "Sair")]

    def compose(self) -> ComposeResult:
        db_controller = DatabaseController()
        yield Header()
        yield Footer()
        yield ScrollableContainer(TelaInicial(db_controller), id="main_container")

if __name__ == "__main__":
    app = Undertale()
    app.run()
