import psycopg2
from psycopg2 import sql

class DatabaseController:
    def __init__(self, dbname="undertale1", user="postgres", password="admin", host="localhost", port="5432"):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        """Estabelece a conexão com o banco de dados."""
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados {self.dbname} na porta {self.port}: {e}")

    def close(self):
        """Fecha a conexão com o banco de dados."""
        if self.connection:
            self.connection.close()

    def execute_sql_script(self, script_path):
        """Executa um script SQL a partir de um arquivo."""
        if self.connection is None or self.connection.closed:
            self.connect()

        cursor = self.connection.cursor()
        try:
            with open(script_path, 'r') as file:
                sql_script = file.read()

            cursor.execute(sql_script)
            self.connection.commit()
            print(f"Script SQL '{script_path}' executado com sucesso!")
        except Exception as e:
            print(f"Erro ao executar o script SQL '{script_path}': {e}")
            self.connection.rollback()
        finally:
            cursor.close()

    # Exemplo de modificação para outras funções
    def add_player(self, jogador_nome):
        """Adiciona um novo jogador à tabela Jogador."""
        if self.connection is None or self.connection.closed:
            self.connect()

        cursor = self.connection.cursor()
        try:
            # Inserir na tabela Afinidade e obter o id_afinidade recém-criado
            cursor.execute(
                "INSERT INTO Afinidade (qtd_atual, qtd_max) VALUES (%s, %s) RETURNING id_afinidade;",
                (0, 50)
            )
            id_afinidade = cursor.fetchone()[0]

            # Inserir na tabela Jogador usando o id_afinidade obtido
            cursor.execute(
                "INSERT INTO Jogador (nome, nivel, qtd_xp, vida_maxima, vida_atual, afinidade, tipo_rota, sala_atual) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s);",
                (jogador_nome, 1, 0, 100, 100, id_afinidade, 'Pacifista', 0)
            )

            self.connection.commit()
        except Exception as e:
            print(f"\nErro ao adicionar jogador: {e}")
            self.connection.rollback()
        finally:
            cursor.close()


    def get_registered_players(self):
        """Retorna os jogadores registrados no banco de dados."""
        if self.connection is None or self.connection.closed:
            self.connect()

        cursor = self.connection.cursor()
        try:
            # Removendo a referência ao schema
            cursor.execute("SELECT nome FROM Jogador;")
            jogadores = [row[0] for row in cursor.fetchall()]
            return jogadores
        except Exception as e:
            print(f"Erro ao buscar jogadores registrados: {e}")
            return []
        finally:
            cursor.close()

    def get_dialog_by_id(self, id_dialogo):
        """Retorna um diálogo específico pelo ID."""
        if self.connection is None or self.connection.closed:
            self.connect()

        cursor = self.connection.cursor()
        try:
            # Consulta sem o schema
            cursor.execute("SELECT texto FROM Dialogo WHERE id_dialogo = %s;", (id_dialogo,))
            dialogo = cursor.fetchone()
            return dialogo[0] if dialogo else None
        except Exception as e:
            print(f"Erro ao buscar diálogo: {e}")
            return None
        finally:
            cursor.close()


    def get_choices_for_dialog(self, id_dialogo):
        """Retorna as escolhas para um diálogo específico."""
        if self.connection is None or self.connection.closed:
            self.connect()

        cursor = self.connection.cursor()
        try:
            # Consulta sem o schema
            cursor.execute("SELECT escolha_id, escolha, prox_dialogo FROM EscolhaDialogo WHERE id_dialogo = %s;", (id_dialogo,))
            escolhas = cursor.fetchall()
            return escolhas
        except Exception as e:
            print(f"Erro ao buscar escolhas para o diálogo: {e}")
            return []
        finally:
            cursor.close()

    def move_player(self, jogador_id, sala_destino_id):
        """Move o jogador para uma nova sala."""
        if self.connection is None or self.connection.closed:
            self.connect()

        cursor = self.connection.cursor()
        try:
            cursor.execute("CALL mover_jogador(%s, %s);", (jogador_id, sala_destino_id))
            self.connection.commit()
            print("Jogador movido com sucesso.")
        except Exception as e:
            print(f"A porta está trancada.")
            self.connection.rollback()
        finally:
            cursor.close()

    def get_available_connections(self, id_jogador):
        """Retorna as conexões disponíveis no banco de dados para um jogador específico."""
        if self.connection is None or self.connection.closed == 1:  # Verifica se a conexão está fechada
            self.connect()

        cursor = self.connection.cursor()
        try:
            query = """
            SELECT id_conexao, direcao, descricao_conexao 
            FROM Conexao 
            WHERE id_sala_origem = (SELECT sala_atual FROM Jogador WHERE id_jogador = %s);
            """
            cursor.execute(query, (id_jogador,))  # Passa o id_jogador como uma tupla
            connections = cursor.fetchall()
            return connections
        except Exception as e:
            print(f"Erro ao buscar conexões registradas: {e}")
            return []
        finally:
            cursor.close()


    def get_status(self, id_jogador):
        """Retorna o status do jogador."""
        if self.connection is None or self.connection.closed == 1:  # Verifica se a conexão está fechada
            self.connect()

        cursor = self.connection.cursor()
        try:
            query = """
                SELECT Jogador.nome, Jogador.nivel, Jogador.qtd_xp, Jogador.vida_atual, Jogador.vida_maxima, Jogador.afinidade, Jogador.tipo_rota, Sala.nome_sala
                FROM Jogador
                JOIN Sala ON Sala.id_sala = Jogador.sala_atual
                WHERE id_jogador = %s;
            """
            cursor.execute(query, (id_jogador,))  # Passa o id_jogador como uma tupla
            jogador = cursor.fetchall()
            return jogador
        except Exception as e:
            print(f"Erro ao buscar conexões registradas: {e}")
            return []
        finally:
            cursor.close()

