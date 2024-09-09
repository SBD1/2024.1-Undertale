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
