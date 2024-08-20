import psycopg2
from psycopg2 import sql

# Conectar ao banco de dados PostgreSQL
def connect_to_db():
    return psycopg2.connect(
        dbname="nome_do_banco",
        user="seu_usuario",
        password="sua_senha",
        host="localhost",
        port="5432"
    )

# Função para criar o esquema e as tabelas
def create_schema_and_tables(conn):
    with conn.cursor() as cur:
        # Criar o esquema
        cur.execute("CREATE SCHEMA IF NOT EXISTS undertale;")
        
        # List of DDL commands
        ddl_commands = [
            """
            CREATE TABLE IF NOT EXISTS undertale.Afinidade (
                id_afinidade SERIAL PRIMARY KEY,
                qtd_atual INT NOT NULL CHECK (qtd_atual >= 0),
                qtd_max INT NOT NULL CHECK (qtd_max > 0)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS undertale.Sala (
                id_sala SERIAL PRIMARY KEY,
                nome_sala VARCHAR(255) NOT NULL,
                descricao TEXT
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS undertale.Jogador (
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
                FOREIGN KEY (item_equipado) REFERENCES undertale.Item(id_item),
                FOREIGN KEY (afinidade) REFERENCES undertale.Afinidade(id_afinidade),
                FOREIGN KEY (sala_atual) REFERENCES undertale.Sala(id_sala),
                CHECK (tipo_rota IN ('Pacifista', 'Genocida', 'Neutra'))
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS undertale.Missao (
                id_missao SERIAL PRIMARY KEY,
                nome VARCHAR(50) NOT NULL,
                descricao VARCHAR(150),
                status VARCHAR(50) NOT NULL,
                CHECK (status IN ('ativa', 'concluída', 'pendente'))
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS undertale.Inventario (
                qtd_item INT NOT NULL CHECK (qtd_item BETWEEN 0 AND 10000),
                tamanho_total DECIMAL(10,2) NOT NULL CHECK (tamanho_total >= 0),
                qtd_gold INT NOT NULL CHECK (qtd_gold >= 0),
                id_jogador INT PRIMARY KEY,
                FOREIGN KEY (id_jogador) REFERENCES undertale.Jogador(id_jogador)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS undertale.Dialogo (
                id_dialogo SERIAL PRIMARY KEY,
                texto VARCHAR(255) NOT NULL,
                id_interacao INT
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS undertale.EscolhaDialogo (
                id_dialogo INT,
                escolha_id INT,
                escolha VARCHAR(50) NOT NULL,
                prox_dialogo INT,
                PRIMARY KEY (id_dialogo, escolha_id),
                FOREIGN KEY (id_dialogo) REFERENCES undertale.Dialogo(id_dialogo),
                FOREIGN KEY (prox_dialogo) REFERENCES undertale.Dialogo(id_dialogo)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS undertale.Loja (
                id_loja SERIAL PRIMARY KEY,
                nome VARCHAR(100),
                sala INT,
                item INT,
                FOREIGN KEY (sala) REFERENCES undertale.Sala(id_sala),
                FOREIGN KEY (item) REFERENCES undertale.Item(id_item)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS undertale.NPC (
                id_npc SERIAL PRIMARY KEY,
                nome VARCHAR(50) NOT NULL,
                sala INT,
                tipo VARCHAR(50) NOT NULL,
                FOREIGN KEY (sala) REFERENCES undertale.Sala(id_sala),
                CHECK (tipo IN ('Mercador', 'Aliado', 'Monstro'))
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS undertale.Mercador (
                loja INT PRIMARY KEY,
                FOREIGN KEY (loja) REFERENCES undertale.Loja(id_loja)
            ) INHERITS (undertale.NPC);
            """,
            """
            CREATE TABLE IF NOT EXISTS undertale.Aliado (
                gold_drop INT NOT NULL CHECK (gold_drop >= 0),
                xp_drop INT NOT NULL CHECK (xp_drop >= 0),
                dano_ataque INT NOT NULL CHECK (dano_ataque >= 0)
            ) INHERITS (undertale.NPC);
            """,
            """
            CREATE TABLE IF NOT EXISTS undertale.Monstro (
                dano_ataque INT NOT NULL CHECK (dano_ataque >= 0),
                xp_drop INT NOT NULL CHECK (xp_drop >= 0),
                gold_drop INT NOT NULL CHECK (gold_drop >= 0),
                item_drop INT
            ) INHERITS (undertale.NPC);
            """,
            """
            CREATE TABLE IF NOT EXISTS undertale.Item (
                id_item SERIAL PRIMARY KEY,
                nome VARCHAR(50) NOT NULL,
                descricao VARCHAR(100),
                valor DECIMAL(10,2) NOT NULL CHECK (valor >= 0),
                tipo VARCHAR(50) NOT NULL,
                CHECK (tipo IN ('Armadura', 'Consumível', 'Chave'))
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS undertale.Instancia_Item (
                id_instancia SERIAL PRIMARY KEY,
                item INT NOT NULL,
                FOREIGN KEY (item) REFERENCES undertale.Item(id_item)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS undertale.Defesa (
                id_instancia INT PRIMARY KEY,
                protecao INT NOT NULL CHECK (protecao >= 0),
                FOREIGN KEY (id_instancia) REFERENCES undertale.Instancia_Item(id_instancia)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS undertale.Consumivel (
                id_instancia INT PRIMARY KEY,
                qtd_cura INT NOT NULL CHECK (qtd_cura >= 0),
                FOREIGN KEY (id_instancia) REFERENCES undertale.Instancia_Item(id_instancia)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS undertale.Ataque (
                id_instancia INT PRIMARY KEY,
                dano INT NOT NULL CHECK (dano >= 0),
                FOREIGN KEY (id_instancia) REFERENCES undertale.Instancia_Item(id_instancia)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS undertale.Conexao (
                id_conexao SERIAL PRIMARY KEY,
                id_sala_origem INT NOT NULL,
                id_sala_destino INT NOT NULL,
                direcao VARCHAR(20) NOT NULL,
                descricao_conexao TEXT,
                FOREIGN KEY (id_sala_origem) REFERENCES undertale.Sala(id_sala),
                FOREIGN KEY (id_sala_destino) REFERENCES undertale.Sala(id_sala),
                CHECK (direcao IN ('Norte', 'Sul', 'Leste', 'Oeste', 'Noroeste', 'Nordeste', 'Sudoeste', 'Sudeste'))
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS undertale.Porta (
                id_porta SERIAL PRIMARY KEY,
                status VARCHAR(50) NOT NULL,
                sala INT NOT NULL,
                FOREIGN KEY (sala) REFERENCES undertale.Sala(id_sala),
                CHECK (status IN ('Aberta', 'Fechada', 'Trancada'))
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS undertale.Bau (
                id_bau SERIAL PRIMARY KEY,
                sala INT NOT NULL,
                capacidade INT NOT NULL CHECK (capacidade >= 1),
                item INT,
                FOREIGN KEY (sala) REFERENCES undertale.Sala(id_sala),
                FOREIGN KEY (item) REFERENCES undertale.Item(id_item)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS undertale.Interacao (
                id_interacao SERIAL PRIMARY KEY,
                npc INT NOT NULL,
                jogador INT NOT NULL,
                dialogo INT,
                FOREIGN KEY (npc) REFERENCES undertale.NPC(id_npc),
                FOREIGN KEY (jogador) REFERENCES undertale.Jogador(id_jogador),
                FOREIGN KEY (dialogo) REFERENCES undertale.Dialogo(id_dialogo)
            );
            """
        ]
        
        # Executar os comandos DDL
        for command in ddl_commands:
            cur.execute(command)
        
        # Confirmar as alterações
        conn.commit()

# Função principal
def main():
    conn = connect_to_db()
    try:
        create_schema_and_tables(conn)
        print("Esquema e tabelas criados com sucesso.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    main()
