import time
from control import DatabaseController

def exibir_dialogo(db_controller: DatabaseController, id_dialogo: int, jogador_id):
    #"""Recupera e exibe um diálogo da tabela Dialogo."""
    db_controller.connect()
    #Verificar se o jogador já viu a introdução
    if db_controller.jogador_viu_introducao(jogador_id):
        print("Você já viu a introdução. Deseja vê-la novamente? (s/n)")
        choice = input().strip().lower()
        if choice == 'n':
            return  # Retorna sem mostrar a introdução novamente
    
    try:
        # Obter o texto do diálogo a partir do banco de dados
        dialogo = db_controller.get_dialog_by_id(id_dialogo)
        if dialogo:
            conteudo = dialogo[0]  # Supondo que o conteúdo é o primeiro campo do resultado
            for char in conteudo:
                print(char, end='', flush=True)
                time.sleep(0.05)  # Pequeno atraso para simular o texto sendo digitado
            print("\n")
            if db_controller.jogador_viu_introducao(jogador_id) == False:
                db_controller.marcar_introducao_vista(jogador_id)

        else:
            print("Diálogo não encontrado.")
    except Exception as e:
        print(f"Erro ao recuperar diálogo: {e}")
    finally:
        db_controller.close()


def exibir_dialogo_flowey(db_controller: DatabaseController, id_dialogo: int):
    # Conecta ao banco de dados
    db_controller.connect()
    
    try:
        # Exibe o diálogo inicial do Flowey
        dialogo = db_controller.get_dialog_by_id(id_dialogo)
        if dialogo:
            conteudo = dialogo[0]
            for char in conteudo:
                print(char, end='', flush=True)
                time.sleep(0.05)
            print("\n")
        else:
            print("Diálogo não encontrado.")
            return
        
        # Adiciona a lógica para interagir com o jogador
        desvios = 0  # Contador de desvios do jogador
        while True:
            print("Flowey sugere que você pegue as 'pétalas da amizade'.")
            print("1. Ir em direção das pétalas")
            print("2. Desviar")

            escolha = input("O que você quer fazer? (Digite 1 ou 2): ").strip()

            if escolha == '1':
                dialogo = db_controller.get_dialog_by_id(6)
                for char in dialogo:
                    print(char, end='', flush=True)
                    time.sleep(0.05)
                print("\n")
                break  # Sai do loop se o jogador escolher ir em direção das pétalas
            elif escolha == '2':
                desvios += 1
                if desvios == 1:
                    dialogo_dodge = db_controller.get_dialog_by_id(3)
                    for char in dialogo_dodge:
                        print(char, end='', flush=True)
                        time.sleep(0.05)
                    print("\n")
                if desvios == 2:
                    dialogo_dodge = db_controller.get_dialog_by_id(4)
                    for char in dialogo_dodge:
                        print(char, end='', flush=True)
                        time.sleep(0.05)
                    print("\n")

                if desvios == 3:
                    # Exibe um novo diálogo após o jogador desviar 3 vezes
                    novo_dialogo = db_controller.get_dialog_by_id(5)  # Supondo que o novo diálogo tenha o ID 3
                    if novo_dialogo:
                        for char in novo_dialogo[0]:
                            print(char, end='', flush=True)
                            time.sleep(0.05)
                        print("\n")
                    else:
                        print("Novo diálogo não encontrado.")
                    break  # Sai do loop após exibir o novo diálogo
            else:
                print("Escolha inválida. Por favor, digite 1 ou 2.")

    except Exception as e:
        print(f"Erro ao recuperar diálogo: {e}")
    finally:
        db_controller.close()
        
def exibir_dialogo_toriel(db_controller: DatabaseController, id_dialogo: int):
    # Conecta ao banco de dados
    db_controller.connect()
    
    try:
        # Exibe o diálogo inicial do Flowey
        dialogo = db_controller.get_dialog_by_id(id_dialogo)
        if dialogo:
            conteudo = dialogo[0]
            for char in conteudo:
                print(char, end='', flush=True)
                time.sleep(0.05)
            print("\n")
        else:
            print("Diálogo não encontrado.")
            return

    except Exception as e:
        print(f"Erro ao recuperar diálogo: {e}")
    finally:
        db_controller.close()

