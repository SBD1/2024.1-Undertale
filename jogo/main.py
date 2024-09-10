import time
import psycopg2
from control import DatabaseController
from interacoes import exibir_dialogo, exibir_dialogo_flowey, exibir_dialogo_toriel

class TerminalInterface:
    def __init__(self, db_controller: DatabaseController):
        self.db_controller = db_controller
        self.current_player_id = None  # Variável para armazenar o ID do jogador selecionado

    def run(self):
        while True:
            print("\nMenu:")
            print("1. Adicionar Novo Jogador")
            print("2. Listar Jogadores")
            print("3. Selecionar Jogador e Iniciar Jogo")
            print("4. Executar Script SQL")
            print("5. Sair")

            choice = input("Escolha uma opção: ").strip()

            if choice == "1":
                self.add_player()
            elif choice == "2":
                self.list_players()
            elif choice == "3":
                self.select_player_and_start_game()
            elif choice == "4":
                self.run_sql_script()
            elif choice == "5":
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
        else:
            print("Nome do jogador não pode estar vazio.")

    def list_players(self):
        self.db_controller.connect()
        jogadores = self.db_controller.get_registered_players()
        self.db_controller.close()
        if jogadores:
            print("\nJogadores Registrados:")
            for jogador in jogadores:
                print(f"- {jogador}")
        else:
            print("Nenhum jogador registrado.")

    
    def list_connections(self):
        self.db_controller.connect()
        connections = self.db_controller.get_available_connections(self.current_player_id)
        self.db_controller.close()
        if connections:
            for connection in connections:
                print(f"-[{connection[0]}] {connection[1]}: {connection[2]}")
        else:
            print("Nenhuma conexão registrada.")

    def select_player_and_start_game(self):
        self.db_controller.connect()
        jogadores = self.db_controller.get_registered_players()
        self.db_controller.close()

        if not jogadores:
            print("Nenhum jogador registrado para iniciar o jogo.")
            return

        print("\nEscolha um jogador para iniciar:")
        for index, jogador in enumerate(jogadores):
            print(f"{index + 1}. {jogador}")

        print("")

        choice = input("Digite o número do jogador escolhido: ").strip()
        try:
            choice_index = int(choice) - 1
            if 0 <= choice_index < len(jogadores):
                self.current_player_id = choice_index + 1  # Considera o ID como o índice + 1
                print(f"Jogador {jogadores[choice_index]} selecionado. Iniciando o jogo...")
                self.start_game()
            else:
                print("Número inválido. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

    def start_game(self):
        # Introdução ao jogo
        jogador_id = self.current_player_id
        # self.display_intro(jogador_id)

        exibir_dialogo(self.db_controller, 1, jogador_id)

        db_controller.criar_interacao_flowey(jogador_id)
        exibir_dialogo_flowey(self.db_controller, 2)
        db_controller.criar_interacao_toriel(jogador_id)
        exibir_dialogo_toriel(self.db_controller, 7)

        # Lógica de movimentação do jogador
        self.player_movement()

    def player_movement(self):
        # Logica de movimentacao do jogador utilizando `self.current_player_id`
        while True:
            print("\nMovimento do Jogador:")
            print("1. Mover para outra sala")
            print("2. Ver status do jogador")
            print("3. Sair do jogo")

            choice = input("Escolha uma opção: ").strip()

            print("")

            if choice == "1":
                self.list_connections()
                self.move_player()
            elif choice == "2":
                self.show_player_status()
            elif choice == "3":
                print("Saindo do jogo...")
                break
            else:
                print("Opção inválida, tente novamente.")

    def move_player(self):
        print("")
        destino = input("Digite o número da direção para se mover: ").strip()
        if destino.isdigit():
            try:
                self.db_controller.connect()
                self.db_controller.move_player(self.current_player_id, int(destino))
                self.db_controller.close()
            except Exception as e:
                print(f"Ero ao mover jogador{e}")
        else:
            print("Número da sala inválido.")

    def show_player_status(self):
        self.db_controller.connect()
        jogador_status = self.db_controller.get_status(self.current_player_id)
        self.db_controller.close()
        if jogador_status:
            jogador = jogador_status[0]
            print(f"[Status do jogador] \n Nome: {jogador[0]} \n Nível: {jogador[1]} \n Quantidade de XP: {jogador[2]} \n Quantidade de vida: {jogador[3]}/{jogador[4]}  \n Afiniddade: {jogador[5]} \n Tipo da rota: {jogador[6]} \n Sala atual: {jogador[7]}")
        else:
            print("Nenhuma conexão registrada.")

    def run_sql_script(self):
        script_path = input("Digite o caminho do script SQL a ser executado: ").strip()
        if script_path:
            self.db_controller.connect()
            self.db_controller.execute_sql_script(script_path)
            self.db_controller.close()
        else:
            print("Caminho do script não pode estar vazio.")


if __name__ == "__main__":
    db_controller = DatabaseController()
    terminal_interface = TerminalInterface(db_controller)
    terminal_interface.run()

