import psycopg2
from control import DatabaseController

class TerminalInterface:
    def __init__(self, db_controller: DatabaseController):
        self.db_controller = db_controller

    def run(self):
        while True:
            print("\nMenu:")
            print("1. Adicionar Novo Jogador")
            print("2. Listar Jogadores")
            print("3. Sair")
            
            choice = input("Escolha uma opção: ").strip()
            
            if choice == "1":
                self.add_player()
            elif choice == "2":
                self.list_players()
            elif choice == "3":
                print("Saindo...")
                break
            else:
                print("Opção inválida, tente novamente.")

    def add_player(self):
        jogador_nome = input("Digite o nome do novo jogador: ").strip()
        if jogador_nome:
            self.db_controller.connect()
            self.db_controller.add_player(jogador_nome)
            self.db_controller.close()
            print(f"Jogador '{jogador_nome}' adicionado com sucesso!")
        else:
            print("Nome do jogador não pode estar vazio.")

    def list_players(self):
        self.db_controller.connect()
        conn = self.db_controller.connection
        if conn:
            cursor = conn.cursor()
            try:
                cursor.execute("SELECT nome FROM Jogador")
                jogadores = [row[0] for row in cursor.fetchall()]
                if jogadores:
                    print("Jogadores Registrados:")
                    for jogador in jogadores:
                        print(f"- {jogador}")
                else:
                    print("Nenhum jogador registrado.")
            except psycopg2.Error as e:
                print(f"Erro ao executar a consulta: {e}")
            finally:
                cursor.close()
                self.db_controller.close()
        else:
            print("Erro ao conectar ao banco de dados.")

if __name__ == "__main__":
    db_controller = DatabaseController()  # Certifique-se de que o DatabaseController está configurado corretamente
    terminal_interface = TerminalInterface(db_controller)
    terminal_interface.run()

