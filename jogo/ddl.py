import psycopg2
from psycopg2 import sql

class DatabaseController:
    def __init__(self, dbname="Undertale4", user="postgres", password="admin", host="localhost", port="5432"):
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
            print(f"Conectado ao banco de dados {self.dbname} com sucesso na porta {self.port}!")
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados {self.dbname} na porta {self.port}: {e}")

    def close(self):
        """Fecha a conexão com o banco de dados."""
        if self.connection:
            self.connection.close()
            print(f"Conexão com o banco de dados {self.dbname} foi fechada.")

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

    def create_tables(self, schema_name="undertale_schema"):
        """Cria as tabelas necessárias no banco de dados dentro do schema especificado."""
        if self.connection is None or self.connection.closed:
            self.connect()

        cursor = self.connection.cursor()

        create_table_queries = [
            f"""
            CREATE TABLE IF NOT EXISTS {schema_name}.Afinidade (
                id_afinidade SERIAL PRIMARY KEY,
                qtd_atual INT NOT NULL CHECK (qtd_atual >= 0),
                qtd_max INT NOT NULL CHECK (qtd_max > 0)
            );
            """,
            f"""
            CREATE TABLE IF NOT EXISTS {schema_name}.Sala (
                id_sala SERIAL PRIMARY KEY,
                nome_sala VARCHAR(255) NOT NULL,
                descricao TEXT
            );
            """,
            f"""
            CREATE TABLE IF NOT EXISTS {schema_name}.Missao (
                id_missao SERIAL PRIMARY KEY,
                nome VARCHAR(50) NOT NULL,
                descricao VARCHAR(150),
                status VARCHAR(50) NOT NULL,
                CHECK (status IN ('ativa', 'concluída', 'pendente'))
            );
            """,
            f"""
            CREATE TABLE IF NOT EXISTS {schema_name}.Item (
                id_item SERIAL PRIMARY KEY,
                nome VARCHAR(50) NOT NULL,
                descricao VARCHAR(100),
                valor DECIMAL(10,2) NOT NULL CHECK (valor >= 0),
                tipo VARCHAR(50) NOT NULL,
                CHECK (tipo IN ('Armadura', 'Consumível', 'Defesa'))
            );
            """,
            f"""
            CREATE TABLE IF NOT EXISTS {schema_name}.Instancia_Item (
                id_instancia SERIAL PRIMARY KEY,
                item INT NOT NULL,
                FOREIGN KEY (item) REFERENCES {schema_name}.Item(id_item)
            );
            """,
            f"""
            CREATE TABLE IF NOT EXISTS {schema_name}.Defesa (
                id_instancia INT PRIMARY KEY,
                protecao INT NOT NULL CHECK (protecao >= 0),
                FOREIGN KEY (id_instancia) REFERENCES {schema_name}.Instancia_Item(id_instancia)
            );
            """,
            f"""
            CREATE TABLE IF NOT EXISTS {schema_name}.Consumivel (
                id_instancia INT PRIMARY KEY,
                qtd_cura INT NOT NULL CHECK (qtd_cura >= 0),
                FOREIGN KEY (id_instancia) REFERENCES {schema_name}.Instancia_Item(id_instancia)
            );
            """,
            f"""
            CREATE TABLE IF NOT EXISTS {schema_name}.Ataque (
                id_instancia INT PRIMARY KEY,
                dano INT NOT NULL CHECK (dano >= 0),
                FOREIGN KEY (id_instancia) REFERENCES {schema_name}.Instancia_Item(id_instancia)
            );
            """,
            f"""
            CREATE TABLE IF NOT EXISTS {schema_name}.Porta (
                id_porta SERIAL PRIMARY KEY,
                status VARCHAR(50) NOT NULL,
                sala INT NOT NULL,
                FOREIGN KEY (sala) REFERENCES {schema_name}.Sala(id_sala),
                CHECK (status IN ('Aberta', 'Fechada', 'Trancada'))
            );
            """,
            f"""
            CREATE TABLE IF NOT EXISTS {schema_name}.Bau (
                id_bau SERIAL PRIMARY KEY,
                sala INT NOT NULL,
                capacidade INT NOT NULL CHECK (capacidade >= 1),
                item INT,
                FOREIGN KEY (sala) REFERENCES {schema_name}.Sala(id_sala),
                FOREIGN KEY (item) REFERENCES {schema_name}.Item(id_item)
            );
            """,
            f"""
            CREATE TABLE IF NOT EXISTS {schema_name}.Jogador (
                id_jogador SERIAL PRIMARY KEY,
                nome VARCHAR(50) NOT NULL,
                item_equipado INT,
                nivel INT NOT NULL CHECK (nivel BETWEEN 1 AND 100),
                qtd_xp INT NOT NULL CHECK (qtd_xp BETWEEN 0 AND 1000),
                vida_maxima INT NOT NULL CHECK (vida_maxima BETWEEN 1 AND 1000),
                vida_atual INT NOT NULL CHECK (vida_atual BETWEEN 0 AND 1000),
                afinidade INT NOT NULL CHECK (afinidade BETWEEN 0 AND 100),
                tipo_rota VARCHAR(50) NOT NULL,
                sala_atual INT,
                FOREIGN KEY (item_equipado) REFERENCES {schema_name}.Item(id_item),
                FOREIGN KEY (afinidade) REFERENCES {schema_name}.Afinidade(id_afinidade),
                FOREIGN KEY (sala_atual) REFERENCES {schema_name}.Sala(id_sala),
                CHECK (tipo_rota IN ('Pacifista', 'Genocida', 'Neutra'))
            );
            """,
            f"""
            CREATE TABLE IF NOT EXISTS {schema_name}.Dialogo (
                id_dialogo SERIAL PRIMARY KEY,
                texto VARCHAR(255) NOT NULL,
                id_interacao INT
            );
            """,
            f"""
            CREATE TABLE IF NOT EXISTS {schema_name}.EscolhaDialogo (
                id_dialogo INT,
                escolha_id INT,
                escolha VARCHAR(50) NOT NULL,
                prox_dialogo INT,
                PRIMARY KEY (id_dialogo, escolha_id),
                FOREIGN KEY (id_dialogo) REFERENCES {schema_name}.Dialogo(id_dialogo),
                FOREIGN KEY (prox_dialogo) REFERENCES {schema_name}.Dialogo(id_dialogo)
            );
            """,
            f"""
            CREATE TABLE IF NOT EXISTS {schema_name}.Loja (
                id_loja SERIAL PRIMARY KEY,
                nome VARCHAR(100),
                sala INT,
                item INT,
                FOREIGN KEY (sala) REFERENCES {schema_name}.Sala(id_sala),
                FOREIGN KEY (item) REFERENCES {schema_name}.Item(id_item)
            );
            """,
            f"""
            CREATE TABLE IF NOT EXISTS {schema_name}.NPC (
                id_npc SERIAL PRIMARY KEY,
                nome VARCHAR(50) NOT NULL,
                sala INT,
                tipo VARCHAR(50) NOT NULL,
                FOREIGN KEY (sala) REFERENCES {schema_name}.Sala(id_sala),
                CHECK (tipo IN ('Mercador', 'Aliado', 'Monstro'))
            );
            """,
            f"""
            CREATE TABLE IF NOT EXISTS {schema_name}.Mercador (
                loja INT PRIMARY KEY,
                FOREIGN KEY (loja) REFERENCES {schema_name}.Loja(id_loja)
            ) INHERITS ({schema_name}.NPC);
            """,
            f"""
            CREATE TABLE IF NOT EXISTS {schema_name}.Aliado (
                gold_drop INT NOT NULL CHECK (gold_drop >= 0),
                xp_drop INT NOT NULL CHECK (xp_drop >= 0),
                dano_ataque INT NOT NULL CHECK (dano_ataque >= 0)
            ) INHERITS ({schema_name}.NPC);
            """,
            f"""
            CREATE TABLE IF NOT EXISTS {schema_name}.Monstro (
                dano_ataque INT NOT NULL CHECK (dano_ataque >= 0),
                xp_drop INT NOT NULL CHECK (xp_drop >= 0),
                gold_drop INT NOT NULL CHECK (gold_drop >= 0),
                item_drop INT
            ) INHERITS ({schema_name}.NPC);
            """,
            f"""
            CREATE TABLE IF NOT EXISTS {schema_name}.Inventario (
                qtd_item INT NOT NULL CHECK (qtd_item BETWEEN 0 AND 10000),
                tamanho_total DECIMAL(10,2) NOT NULL CHECK (tamanho_total >= 0),
                qtd_gold INT NOT NULL CHECK (qtd_gold >= 0),
                id_jogador INT PRIMARY KEY,
                FOREIGN KEY (id_jogador) REFERENCES {schema_name}.Jogador(id_jogador)
            );
            """,
            f"""
            CREATE TABLE IF NOT EXISTS {schema_name}.Interacao (
                id_interacao SERIAL PRIMARY KEY,
                npc INT NOT NULL,
                jogador INT NOT NULL,
                dialogo INT,
                FOREIGN KEY (npc) REFERENCES {schema_name}.NPC(id_npc),
                FOREIGN KEY (jogador) REFERENCES {schema_name}.Jogador(id_jogador),
                FOREIGN KEY (dialogo) REFERENCES {schema_name}.Dialogo(id_dialogo)
            );
            """,
            f"""
            CREATE TABLE IF NOT EXISTS {schema_name}.Conexao (
                id_conexao SERIAL PRIMARY KEY,
                id_sala_origem INT NOT NULL,
                id_sala_destino INT NOT NULL,
                direcao VARCHAR(20) NOT NULL,
                descricao_conexao TEXT,
                FOREIGN KEY (id_sala_origem) REFERENCES {schema_name}.Sala(id_sala),
                FOREIGN KEY (id_sala_destino) REFERENCES {schema_name}.Sala(id_sala),
                CHECK (direcao IN ('Norte', 'Sul', 'Leste', 'Oeste', 'Noroeste', 'Nordeste', 'Sudoeste', 'Sudeste'))
            );
            """
        ]


        try:
            for query in create_table_queries:
                cursor.execute(query)
            self.connection.commit()
            print("Tabelas criadas com sucesso!")
        except Exception as e:
            print(f"Erro ao criar tabelas: {e}")
            self.connection.rollback()
        finally:
            cursor.close()

    def get_registered_players(self, schema_name="undertale_schema"):
        """Retorna os jogadores registrados no banco de dados."""
        if self.connection is None or self.connection.closed:
            self.connect()

        cursor = self.connection.cursor()
        try:
            cursor.execute(sql.SQL("SELECT nome FROM {}.Jogador;").format(sql.Identifier(schema_name)))
            jogadores = [row[0] for row in cursor.fetchall()]
            print("Jogadores registrados:", jogadores)
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
                sql.SQL("INSERT INTO {}.Afinidade (qtd_atual, qtd_max) VALUES (%s, %s) RETURNING id_afinidade;")
                .format(sql.Identifier(schema_name)),
                (0, 50)
            )
            id_afinidade = cursor.fetchone()[0]

            # Inserir na tabela Jogador usando o id_afinidade obtido
            cursor.execute(
                sql.SQL("INSERT INTO {}.Jogador (nome, nivel, qtd_xp, vida_maxima, vida_atual, afinidade, tipo_rota) "
                        "VALUES (%s, %s, %s, %s, %s, %s, %s);")
                .format(sql.Identifier(schema_name)),
                (jogador_nome, 1, 0, 100, 100, id_afinidade, 'Pacifista')
            )

            self.connection.commit()
            print(f"Jogador '{jogador_nome}' adicionado com sucesso!")
        except Exception as e:
            print(f"Erro ao adicionar jogador: {e}")
            self.connection.rollback()
        finally:
            cursor.close()

# Exemplo de uso:
if __name__ == "__main__":
    db_controller = DatabaseController()

    # Conectar ao banco
    db_controller.connect()

    # Criar schema
    db_controller.create_schema()

    # Criar tabelas dentro do schema
    db_controller.create_tables()

    # Adicionar um jogador
    db_controller.add_player("Frisk")

    # Buscar jogadores registrados
    jogadores = db_controller.get_registered_players()
    print("Jogadores:", jogadores)

    # Fechar a conexão
    db_controller.close()
