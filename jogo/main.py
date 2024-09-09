import time
from control import DatabaseController
from interacoes import exibir_dialogo

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

        # Lógica de movimentação do jogador
        self.player_movement()

    # def display_intro(self, jogador_id):
    #     # Verificar se o jogador já viu a introdução
    #     if self.db_controller.jogador_viu_introducao(jogador_id):
    #         print("Você já viu a introdução. Deseja vê-la novamente? (s/n)")
    #         choice = input().strip().lower()
    #         if choice == 'n':
    #             return  # Retorna sem mostrar a introdução novamente
            
    #     text = ("\nHá muito tempo, Humanos e Monstros conviviam juntos em harmonia sobre a Terra. \nUm dia, uma guerra se iniciou entre as duas raças e depois de um longo confronto, os humanos foram vitoriosos.\n"
    #             "Eles confinaram todos os monstros existentes no subterrâneo do Monte Ebott com uma barreira mágica.\nApenas o poder de 7 almas humanas diferentes poderia romper a barreira permanentemente.\n\n"
    #             "Muito tempo depois, em 201X, uma criança humana acabou escalando o Monte por razões desconhecidas e, consequentemente, caiu no subterrâneo, onde os monstros atualmente residem.\n")
    #     for char in text:
    #         print(char, end='', flush=True)
    #         time.sleep(0.05)  # Pequeno atraso para simular o texto sendo digitado
    #     print("\n")
    #     self.db_controller.marcar_introducao_vista(jogador_id)

    def player_movement(self):
        # Logica de movimentacao do jogador utilizando `self.current_player_id`
        while True:
            print("\nMovimento do Jogador:")
            print("1. Mover para outra sala")
            print("2. Ver status do jogador")
            print("3. Sair do jogo")

            choice = input("Escolha uma opção: ").strip()

            if choice == "1":
                # Chama a procedure de movimentação usando o `self.current_player_id`
                self.move_player()
            elif choice == "2":
                self.show_player_status()
            elif choice == "3":
                print("Saindo do jogo...")
                break
            else:
                print("Opção inválida, tente novamente.")

    def move_player(self):
        destino = input("Digite o ID da sala de destino: ").strip()
        if destino.isdigit():
            try:
                self.db_controller.connect()
                self.db_controller.move_player(self.current_player_id, int(destino))
                self.db_controller.close()
                print("Jogador movido com sucesso.")
            except Exception as e:
                print(f"Erro ao mover jogador: {e}")
        else:
            print("ID da sala inválido.")

    def show_player_status(self):
        # Lógica para mostrar o status do jogador selecionado
        pass

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

