import psycopg2
import cmd

class UndertaleGame(cmd.Cmd):
    intro = "Bem-vindo ao jogo! Digite 'ajuda' ou '?' para listar os comandos.\n"
    prompt = "(jogo) "

    def __init__(self, dbname, user, password, host="localhost", port="5432"):
        super().__init__()
        try:
            self.conn = psycopg2.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
                port=port
            )
            self.cursor = self.conn.cursor()
            self.jogador_id = None
            self.sala_atual = 1
            self.inserir_dados_iniciais()  # Adiciona os dados iniciais ao iniciar
        except psycopg2.OperationalError as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            exit(1)

    def inserir_dados_iniciais(self):
        try:
            # Inserir uma nova missão
            self.cursor.execute("""
                INSERT INTO Missao (nome, descricao, status)
                VALUES ('Resolva o puzzle', 'Resolva o puzzle das Ruinas para liberar a porta para a outra sala', 'ativa')
                ON CONFLICT (nome) DO NOTHING
            """)

            # Inserir um novo item
            self.cursor.execute("""
                INSERT INTO Item (nome, descricao, valor, tipo)
                VALUES ('Bandana Viril', '7DF - Tem abdominais nela', 50.00, 'Armadura')
                ON CONFLICT (nome) DO NOTHING
            """)

            # Inserir novas salas
            self.cursor.execute("""
                INSERT INTO Sala (nome_sala, descricao)
                VALUES ('Ruinas', 'A entrada principal do mundo subterraneo')
                ON CONFLICT (nome_sala) DO NOTHING
            """)
            self.cursor.execute("""
                INSERT INTO Sala (nome_sala, descricao)
                VALUES ('Cachoeiras', 'Lugar misterioso protegido por uma poderosa guardiã')
                ON CONFLICT (nome_sala) DO NOTHING
            """)

            # Inserir uma nova conexão entre salas
            self.cursor.execute("""
                INSERT INTO Conexao (id_sala_origem, id_sala_destino, direcao, descricao_conexao)
                VALUES (1, 2, 'Norte', 'Caminho que leva ao centro das ruinas')
                ON CONFLICT (id_sala_origem, id_sala_destino, direcao) DO NOTHING
            """)

            # Inserir aliados
            self.cursor.execute("""
                INSERT INTO Aliado (nome, sala, tipo, gold_drop, xp_drop, dano_ataque)
                VALUES ('Flowey', NULL, 'Aliado', 20, 10, 99)
                ON CONFLICT (nome) DO NOTHING
            """)
            self.cursor.execute("""
                INSERT INTO Aliado (nome, sala, tipo, gold_drop, xp_drop, dano_ataque)
                VALUES ('Toriel', NULL, 'Aliado', 15, 5, 10)
                ON CONFLICT (nome) DO NOTHING
            """)
            self.cursor.execute("""
                INSERT INTO Aliado (nome, sala, tipo, gold_drop, xp_drop, dano_ataque)
                VALUES ('Sans', NULL, 'Aliado', 25, 30, 20)
                ON CONFLICT (nome) DO NOTHING
            """)
            self.cursor.execute("""
                INSERT INTO Aliado (nome, sala, tipo, gold_drop, xp_drop, dano_ataque)
                VALUES ('Papyrus', NULL, 'Aliado', 20, 25, 15)
                ON CONFLICT (nome) DO NOTHING
            """)

            # Inserir monstros
            self.cursor.execute("""
                INSERT INTO Monstro (nome, sala, tipo, dano_ataque, xp_drop, gold_drop, item_drop)
                VALUES ('Napstablook', NULL, 'Monstro', 5, 5, 10, NULL)
                ON CONFLICT (nome) DO NOTHING
            """)
            self.cursor.execute("""
                INSERT INTO Monstro (nome, sala, tipo, dano_ataque, xp_drop, gold_drop, item_drop)
                VALUES ('Doggo', NULL, 'Monstro', 12, 30, 15, NULL)
                ON CONFLICT (nome) DO NOTHING
            """)
            self.cursor.execute("""
                INSERT INTO Monstro (nome, sala, tipo, dano_ataque, xp_drop, gold_drop, item_drop)
                VALUES ('Dogamy e Dogaressa', NULL, 'Monstro', 40, 40, 20, NULL)
                ON CONFLICT (nome) DO NOTHING
            """)
            self.cursor.execute("""
                INSERT INTO Monstro (nome, sala, tipo, dano_ataque, xp_drop, gold_drop, item_drop)
                VALUES ('Dogão', NULL, 'Monstro', 80, 60, 50, NULL)
                ON CONFLICT (nome) DO NOTHING
            """)

            # Inserir mercadores
            self.cursor.execute("""
                INSERT INTO Mercador (nome, sala, tipo, loja)
                VALUES ('Lojista de Nevada', NULL, 'Mercador', 1)
                ON CONFLICT (nome) DO NOTHING
            """)
            self.cursor.execute("""
                INSERT INTO Mercador (nome, sala, tipo, loja)
                VALUES ('Gerson', 2, 'Mercador', 2)
                ON CONFLICT (nome) DO NOTHING
            """)

            # Inserir defesas, consumíveis, ataques e outros
            self.cursor.execute("""
                INSERT INTO Defesa (id_instancia, protecao)
                VALUES (1, 10)
                ON CONFLICT (id_instancia) DO NOTHING
            """)
            self.cursor.execute("""
                INSERT INTO Consumivel (id_instancia, qtd_cura)
                VALUES (2, 20)
                ON CONFLICT (id_instancia) DO NOTHING
            """)
            self.cursor.execute("""
                INSERT INTO Ataque (id_instancia, dano)
                VALUES (3, 25)
                ON CONFLICT (id_instancia) DO NOTHING
            """)
            self.cursor.execute("""
                INSERT INTO Porta (status, sala)
                VALUES ('Fechada', 1)
                ON CONFLICT (status, sala) DO NOTHING
            """)
            self.cursor.execute("""
                INSERT INTO Bau (sala, capacidade, item)
                VALUES (1, 5, 1)
                ON CONFLICT (sala, item) DO NOTHING
            """)
            self.cursor.execute("""
                INSERT INTO Afinidade (qtd_atual, qtd_max)
                VALUES (0, 100)
                ON CONFLICT (qtd_atual, qtd_max) DO NOTHING
            """)
            self.cursor.execute("""
                INSERT INTO Loja (nome, sala, item)
                VALUES ('Loja de Nevada', 1, 1)
                ON CONFLICT (nome, sala, item) DO NOTHING
            """)
            self.cursor.execute("""
                INSERT INTO Loja (nome, sala, item)
                VALUES ('Loja do Gerson', 2, 1)
                ON CONFLICT (nome, sala, item) DO NOTHING
            """)

            # Inserir uma nova interação
            self.cursor.execute("""
                INSERT INTO Interacao (npc, jogador, dialogo)
                VALUES (1, 1, 1)
                ON CONFLICT (npc, jogador, dialogo) DO NOTHING
            """)

            self.conn.commit()
            print("Dados iniciais inseridos com sucesso.")
        except psycopg2.Error as e:
            print(f"Erro ao inserir dados iniciais: {e}")
            self.conn.rollback()

    def do_criar_jogador(self, args):
        """Criar um novo jogador: criar_jogador NomeJogador [id_jogador]"""
        if not args:
            print("Uso incorreto. Exemplo: criar_jogador NomeJogador 1")
            return
        args = args.split()
        if len(args) != 2:
            print("Uso incorreto. Exemplo: criar_jogador NomeJogador 1")
            return
        nome_jogador, jogador_id = args
        try:
            jogador_id = int(jogador_id)
            sala_inicial = 1  # Defina a sala inicial conforme necessário
            self.cursor.execute("""
                INSERT INTO Jogador (id_jogador, nome, item_equipado, nivel, qtd_xp, vida_maxima, vida_atual, afinidade, tipo_rota, sala_atual)
                VALUES (%s, %s, NULL, 1, 0, 100, 100, 0, 'Neutra', %s)
                ON CONFLICT (id_jogador) DO NOTHING
            """, (jogador_id, nome_jogador, sala_inicial))
            self.conn.commit()
            print(f"Jogador '{nome_jogador}' com ID {jogador_id} criado na sala {sala_inicial}.")
        except ValueError:
            print("Erro: ID do jogador deve ser um número inteiro.")
        except psycopg2.Error as e:
            print(f"Erro ao criar jogador: {e}")

    def do_iniciar(self, jogador_id):
        """Iniciar o jogo com um jogador existente: iniciar [id_jogador]"""
        if not jogador_id:
            print("Erro: ID do jogador não fornecido.")
            return
        try:
            jogador_id = jogador_id.strip()  # Remove espaços em branco ao redor
            if not jogador_id:
                print("Erro: ID do jogador não fornecido.")
                return
            self.jogador_id = int(jogador_id)
            print(f"Tentando iniciar o jogo com ID do jogador: {self.jogador_id}")  # Depuração
            self.cursor.execute("""
                SELECT sala_atual FROM Jogador WHERE id_jogador = %s
            """, (self.jogador_id,))
            result = self.cursor.fetchone()
            if result:
                self.sala_atual = result[0]
                print(f"Jogo iniciado! Você está na sala {self.sala_atual}.")
            else:
                print("Jogador não encontrado.")
        except ValueError:
            print("Erro: ID do jogador deve ser um número inteiro.")
        except psycopg2.Error as e:
            print(f"Erro ao iniciar o jogo: {e}")

    def do_sair(self, arg):
        """Sair do jogo"""
        print("Saindo do jogo.")
        return True

if __name__ == '__main__':
    game = UndertaleGame(dbname="undertale", user="seu_usuario", password="sua_senha")
    game.cmdloop()
