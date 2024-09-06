import psycopg2
from psycopg2 import sql

class DatabaseController:
    def __init__(self, dbname="Undertale6", user="postgres", password="admin", host="localhost", port="5432"):
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
           # print(f"Conectado ao banco de dados {self.dbname} com sucesso na porta {self.port}!")
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados {self.dbname} na porta {self.port}: {e}")

    def close(self):
        """Fecha a conexão com o banco de dados."""
        if self.connection:
            self.connection.close()
           # print(f"Conexão com o banco de dados {self.dbname} foi fechada.")

    def create_schema(self, schema_name="undertale_schema"):
        """Cria um schema no banco de dados."""
        if self.connection is None or self.connection.closed:
            self.connect()

        cursor = self.connection.cursor()
        try:
            # Cria o schema se não existir
            cursor.execute(sql.SQL("CREATE SCHEMA IF NOT EXISTS {}").format(sql.Identifier(schema_name)))
            self.connection.commit()
            print(f"Schema '{schema_name}' criado com sucesso!")
        except Exception as e:
            print(f"Erro ao criar o schema: {e}")
            self.connection.rollback()
        finally:
            cursor.close()



    def get_registered_players(self, schema_name="undertale_schema"):
        """Retorna os jogadores registrados no banco de dados."""
        if self.connection is None or self.connection.closed:
            self.connect()

        cursor = self.connection.cursor()
        try:
            cursor.execute(sql.SQL("SELECT nome FROM Jogador;").format(sql.Identifier(schema_name)))
            jogadores = [row[0] for row in cursor.fetchall()]
          #  print("Jogadores registrados:", jogadores)
            return jogadores
        except Exception as e:
            print(f"Erro ao buscar jogadores registrados: {e}")
            return []
        finally:
            cursor.close()

    def add_player(self, jogador_nome, schema_name="undertale_schema"):
        """Adiciona um novo jogador à tabela Jogador."""
        if self.connection is None or self.connection.closed:
            self.connect()

        cursor = self.connection.cursor()
        try:
            # Inserir na tabela Afinidade e obter o id_afinidade recém-criado
            cursor.execute(
                sql.SQL("INSERT INTO Afinidade (qtd_atual, qtd_max) VALUES (%s, %s) RETURNING id_afinidade;")
                .format(sql.Identifier(schema_name)),
                (0, 50)
            )
            id_afinidade = cursor.fetchone()[0]

            # Inserir na tabela Jogador usando o id_afinidade obtido
            cursor.execute(
                sql.SQL("INSERT INTO Jogador (nome, nivel, qtd_xp, vida_maxima, vida_atual, afinidade, tipo_rota) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s);")
                .format(sql.Identifier(schema_name)),
                (jogador_nome, 1, 0, 100, 100, id_afinidade, 'Pacifista')
            )

            self.connection.commit()
         #   print(f"Jogador '{jogador_nome}' adicionado com sucesso!")
        except Exception as e:
            print(f"Erro ao adicionar jogador: {e}")
            self.connection.rollback()
        finally:
            cursor.close()


    def get_dialog_by_id(self, id_dialogo, schema_name="undertale_schema"):
        """Retorna um diálogo específico pelo ID."""
        if self.connection is None or self.connection.closed:
            self.connect()

        cursor = self.connection.cursor()
        try:
            cursor.execute(
                sql.SQL("SELECT texto FROM {}.Dialogo WHERE id_dialogo = %s;")
                .format(sql.Identifier(schema_name)),
                (id_dialogo,)
            )
            dialogo = cursor.fetchone()
            return dialogo[0] if dialogo else None
        except Exception as e:
            print(f"Erro ao buscar diálogo: {e}")
            return None
        finally:
            cursor.close()

    def get_choices_for_dialog(self, id_dialogo, schema_name="undertale_schema"):
        """Retorna as escolhas para um diálogo específico."""
        if self.connection is None or self.connection.closed:
            self.connect()

        cursor = self.connection.cursor()
        try:
            cursor.execute(
                sql.SQL("SELECT escolha_id, escolha, prox_dialogo FROM {}.EscolhaDialogo WHERE id_dialogo = %s;")
                .format(sql.Identifier(schema_name)),
                (id_dialogo,)
            )
            escolhas = cursor.fetchall()
            return escolhas
        except Exception as e:
            print(f"Erro ao buscar escolhas para o diálogo: {e}")
            return []
        finally:
            cursor.close()