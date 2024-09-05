import psycopg2
from psycopg2 import sql

from jogo.ddl import DatabaseController

class DatabaseControllerDML:
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

    def insert_initial_values(self, schema_name="undertale_schema"):
        """Insere valores iniciais nas tabelas do banco de dados dentro do schema especificado."""
        if self.connection is None or self.connection.closed:
            self.connect()

        cursor = self.connection.cursor()


        mission = [
            # Inserir uma nova missão
            f"""
            INSERT INTO {schema_name}.Missao (nome, descricao, status)
            VALUES ('Resolva o puzzle', 'Resolva o puzzle das Ruinas para liberar a porta para a outra sala', 'ativa')
            
            """
        ]

        itens = [
            # Inserir um novo item
            f"""
            INSERT INTO {schema_name}.Item (nome, descricao, valor, tipo)
            VALUES ('Bandana Viril', '7DF - Tem abdominais nela', 50.00, 'Armadura')
            """
            f"""
            INSERT INTO {schema_name}.Item (nome, descricao, valor, tipo)
            VALUES ('Luva Forte', ' 5AT Na cara deles.', 50.00, 'Defesa')
            """
            f"""
            INSERT INTO {schema_name}.Item (nome, descricao, valor, tipo)
            VALUES ('Luva Forte', ' 5AT Na cara deles.', 50.00, 'Defesa')
            """

        ]

        salas = [
            # Inserir novas salas
            f"""
            INSERT INTO {schema_name}.Sala (nome_sala, descricao)
            VALUES ('Ruinas', 'A entrada principal do mundo subterraneo')
            """,
            f"""
            INSERT INTO {schema_name}.Sala (nome_sala, descricao)
            VALUES ('Cachoeiras', 'Lugar misterioso protegido por uma poderosa guardiã')
            """,

        ]

        aliados = [
            # Inserir aliados
            f"""
            INSERT INTO {schema_name}.Aliado (nome, sala, tipo, gold_drop, xp_drop, dano_ataque)
            VALUES ('Flowey', NULL, 'Aliado', 20, 10, 99)
            
            """,

            f"""
            INSERT INTO {schema_name}.Aliado (nome, sala, tipo, gold_drop, xp_drop, dano_ataque)
            VALUES ('Toriel', NULL, 'Aliado', 15, 5, 10)
            
            """,
            f"""
            INSERT INTO {schema_name}.Aliado (nome, sala, tipo, gold_drop, xp_drop, dano_ataque)
            VALUES ('Sans', NULL, 'Aliado', 25, 30, 20)
            
           """,
            f"""
            INSERT INTO {schema_name}.Aliado (nome, sala, tipo, gold_drop, xp_drop, dano_ataque)
            VALUES ('Papyrus', NULL, 'Aliado', 20, 25, 15)
            
           """

        ] 

        conexao = {
            # Inserir uma nova conexão entre salas
            f"""
            INSERT INTO {schema_name}.Conexao (id_sala_origem, id_sala_destino, direcao, descricao_conexao)
            VALUES (1, 2, 'Norte', 'Caminho que leva ao centro das ruinas')
            """
        }

        monstros = [
            # Inserir monstros
            f"""
            INSERT INTO {schema_name}.Monstro (nome, sala, tipo, dano_ataque, xp_drop, gold_drop, item_drop)
            VALUES ('Napstablook', NULL, 'Monstro', 5, 5, 10, NULL)
            
           """,
            f"""
            INSERT INTO {schema_name}.Monstro (nome, sala, tipo, dano_ataque, xp_drop, gold_drop, item_drop)
            VALUES ('Doggo', NULL, 'Monstro', 12, 30, 15, NULL)
            
           """,
            f"""
            INSERT INTO {schema_name}.Monstro (nome, sala, tipo, dano_ataque, xp_drop, gold_drop, item_drop)
            VALUES ('Dogamy e Dogaressa', NULL, 'Monstro', 40, 40, 20, NULL)
            
           """,
            f"""
            INSERT INTO {schema_name}.Monstro (nome, sala, tipo, dano_ataque, xp_drop, gold_drop, item_drop)
            VALUES ('Dogão', NULL, 'Monstro', 80, 60, 50, NULL)
            
           """
        ]

        mercadores = [
            # Inserir mercadores
            f"""
            INSERT INTO {schema_name}.Mercador (nome, sala, tipo, loja)
            VALUES ('Lojista de Nevada', NULL, 'Mercador', 1)
            
           """,
            f"""
            INSERT INTO {schema_name}.Mercador (nome, sala, tipo, loja)
            VALUES ('Gerson', 2, 'Mercador', 2)
            
           """
        ]

        loja = [
            f"""
            INSERT INTO {schema_name}.Loja (nome, sala, item)
            VALUES ('Loja de Nevada', 1, 1)

           """,
            f"""
            INSERT INTO {schema_name}.Loja (nome, sala, item)
            VALUES ('Loja do Gerson', 2, 1)

           """

        ]

        afinidade = [
            f"""
            INSERT INTO {schema_name}.Afinidade (qtd_atual, qtd_max)
            VALUES (0, 100)

           """
        ]


        outros = [
            # 
            f"""
            INSERT INTO {schema_name}.Porta (status, sala)
            VALUES ('Fechada', 1)
           
           """,
            f"""
            INSERT INTO {schema_name}.Bau (sala, capacidade, item)
            VALUES (1, 5, 1)    
           """


        ]

        interacao =  [
    
            # Inserir uma nova interação
            f"""
            INSERT INTO {schema_name}.Interacao (npc, jogador, dialogo)
            VALUES (1, 1, 1)
           """

        ]

        instancia_item = [
            #falta criar o insert de instancia
            f"""
            INSERT INTO {schema_name}.Defesa (id_instancia, protecao)
            VALUES (1, 10)
            
           """,
            f"""
            INSERT INTO {schema_name}.Consumivel (id_instancia, qtd_cura)
            VALUES (2, 20)
            
           """,
            f"""
            INSERT INTO {schema_name}.Ataque (id_instancia, dano)
            VALUES (3, 25)
            
           """
        ]

        try:
            #estou vendo a ordem deles, pois tem muitos qu existe uma depedência entre eles
            queries = [mission, aliados, monstros, salas, itens, mercadores, outros, interacao, conexao]
            #após encontrar, dá para percorrer por cada um atomaticamente
            for query in salas:
                cursor.execute(query)
            self.connection.commit()
            print("Dados inseridos com sucesso!")
        except Exception as e:
            print(f"Erro ao inserir dados: {e}")
            self.connection.rollback()
        finally:
            cursor.close()


# Exemplo de uso:
if __name__ == "__main__":
    db_controller = DatabaseController()

    # Conectar ao banco
    db_controller.connect()

    # Inserir dados iniciais
    db_controller.insert_initial_values()

    # Fechar a conexão
    db_controller.close()
