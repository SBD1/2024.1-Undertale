# main.py
from control import DatabaseController

class TerminalInterface:
    def __init__(self, db_controller: DatabaseController):
        self.db_controller = db_controller

    def run(self):
        while True:
            print("\nMenu:")
            print("1. Adicionar Novo Jogador")
            print("2. Listar Jogadores")
            print("3. Executar Script SQL")
            print("4. Sair")
            
            choice = input("Escolha uma opção: ").strip()
            
            if choice == "1":
                self.add_player()
            elif choice == "2":
                self.list_players()
            elif choice == "3":
                self.run_sql_script()
            elif choice == "4":
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
