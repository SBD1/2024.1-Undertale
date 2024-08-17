
# Linguagem de Definição de Dados (DDL)

## Introdução

A Linguagem de Definição de Dados (DDL), ou Data Definition Language, é um conjunto de comandos usados em sistemas de gerenciamento de banco de dados (SGBD) para criar, alterar e gerenciar a estrutura dos bancos de dados.

## DDL - Undertale

Após a modelagem criamos todas as tabelas mapeadas com a ajuda do DD (Data Dictionary) para dar progresso ao trabalho.

```sql
-- Tabela: Jogador
CREATE TABLE IF NOT EXISTS Jogador (
    id_jogador SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    item_equipado INT,
    nivel INT NOT NULL CHECK (nivel BETWEEN 1 AND 100),
    qtd_xp INT NOT NULL CHECK (qtd_xp BETWEEN 0 AND 1000),
    vida_maxima INT NOT NULL CHECK (vida_maxima BETWEEN 1 AND 1000),
    vida_atual INT NOT NULL CHECK (vida_atual BETWEEN 0 AND 1000),
    afinidade INT,
    tipo_rota VARCHAR(50) NOT NULL CHECK (tipo_rota IN ('Pacifista', 'Genocida', 'Neutra')),
    FOREIGN KEY (item_equipado) REFERENCES Item(id_item),
    FOREIGN KEY (afinidade) REFERENCES Afinidade(id_afinidade)
);

-- Tabela: Missão
CREATE TABLE IF NOT EXISTS Missao (
    id_missao SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    descricao VARCHAR(150),
    status VARCHAR(50) NOT NULL CHECK (status IN ('ativa', 'concluída', 'pendente'))
);

-- Tabela: Inventário
CREATE TABLE IF NOT EXISTS Inventario (
    qtd_item INT NOT NULL CHECK (qtd_item BETWEEN 0 AND 10000),
    tamanho_total DECIMAL(10,2) NOT NULL CHECK (tamanho_total >= 0),
    qtd_gold INT NOT NULL CHECK (qtd_gold >= 0),
    id_jogador INT PRIMARY KEY,
    FOREIGN KEY (id_jogador) REFERENCES Jogador(id_jogador)
);

-- Tabela: Diálogo
CREATE TABLE IF NOT EXISTS Dialogo (
    id_dialogo SERIAL PRIMARY KEY,
    texto VARCHAR(255) NOT NULL,
    id_interacao INT,
    FOREIGN KEY (id_interacao) REFERENCES Interacao(id_interacao)
);

-- Tabela: NPC
CREATE TABLE IF NOT EXISTS NPC (
    id_npc SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    sala INT,
    tipo VARCHAR(50) NOT NULL CHECK (tipo IN ('Mercador', 'Aliado', 'Monstro')),
    FOREIGN KEY (sala) REFERENCES Sala(id_sala)
);

-- Tabela: Mercador
CREATE TABLE IF NOT EXISTS Mercador (
    loja INT PRIMARY KEY,
    FOREIGN KEY (loja) REFERENCES Loja(id_loja)
);

-- Tabela: Aliado
CREATE TABLE IF NOT EXISTS Aliado (
    gold_drop INT NOT NULL CHECK (gold_drop >= 0),
    xp_drop INT NOT NULL CHECK (xp_drop >= 0),
    dano_ataque INT NOT NULL CHECK (dano_ataque >= 0),
    PRIMARY KEY (id_npc),
    FOREIGN KEY (id_npc) REFERENCES NPC(id_npc)
);

-- Tabela: Monstro
CREATE TABLE IF NOT EXISTS Monstro (
    dano_ataque INT NOT NULL CHECK (dano_ataque >= 0),
    xp_drop INT NOT NULL CHECK (xp_drop >= 0),
    gold_drop INT NOT NULL CHECK (gold_drop >= 0),
    item_drop INT,
    PRIMARY KEY (id_npc),
    FOREIGN KEY (id_npc) REFERENCES NPC(id_npc),
    FOREIGN KEY (item_drop) REFERENCES Item(id_item)
);

-- Tabela: Item
CREATE TABLE IF NOT EXISTS Item (
    id_item SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    descricao VARCHAR(100),
    valor DECIMAL(10,2) NOT NULL CHECK (valor >= 0),
    tipo VARCHAR(50) NOT NULL CHECK (tipo IN ('Armadura', 'Consumível', 'Chave'))
);

-- Tabela: Instância-Item
CREATE TABLE IF NOT EXISTS Instancia_Item (
    id_instancia SERIAL PRIMARY KEY,
    item INT NOT NULL,
    FOREIGN KEY (item) REFERENCES Item(id_item)
);

-- Tabela: Defesa (subentidade de Item)
CREATE TABLE IF NOT EXISTS Defesa (
    id_instancia INT PRIMARY KEY,
    protecao INT NOT NULL CHECK (protecao >= 0),
    FOREIGN KEY (id_instancia) REFERENCES Instancia_Item(id_instancia)
);

-- Tabela: Consumível (subentidade de Item)
CREATE TABLE IF NOT EXISTS Consumivel (
    id_instancia INT PRIMARY KEY,
    qtd_cura INT NOT NULL CHECK (qtd_cura >= 0),
    FOREIGN KEY (id_instancia) REFERENCES Instancia_Item(id_instancia)
);

-- Tabela: Ataque (subentidade de Item)
CREATE TABLE IF NOT EXISTS Ataque (
    id_instancia INT PRIMARY KEY,
    dano INT NOT NULL CHECK (dano >= 0),
    FOREIGN KEY (id_instancia) REFERENCES Instancia_Item(id_instancia)
);

-- Tabela: Sala
CREATE TABLE IF NOT EXISTS Sala (
    id_sala SERIAL PRIMARY KEY,
    nome_sala VARCHAR(255) NOT NULL,
    descricao TEXT,
    x_coord INT NOT NULL,
    y_coord INT NOT NULL
);

-- Tabela: Conexão entre Salas
CREATE TABLE IF NOT EXISTS Conexao (
    id_conexao SERIAL PRIMARY KEY,
    id_sala_origem INT NOT NULL,
    id_sala_destino INT NOT NULL,
    direcao VARCHAR(20) NOT NULL CHECK (direcao IN ('Norte', 'Sul', 'Leste', 'Oeste', 'Noroeste', 'Nordeste', 'Sudoeste', 'Sudeste')),
    descricao_conexao TEXT,
    FOREIGN KEY (id_sala_origem) REFERENCES Sala(id_sala),
    FOREIGN KEY (id_sala_destino) REFERENCES Sala(id_sala)
);

-- Tabela: Porta
CREATE TABLE IF NOT EXISTS Porta (
    id_porta SERIAL PRIMARY KEY,
    status VARCHAR(50) NOT NULL CHECK (status IN ('Aberta', 'Fechada', 'Trancada')),
    sala INT NOT NULL,
    FOREIGN KEY (sala) REFERENCES Sala(id_sala)
);

-- Tabela: Baú
CREATE TABLE IF NOT EXISTS Bau (
    id_bau SERIAL PRIMARY KEY,
    sala INT NOT NULL,
    capacidade INT NOT NULL CHECK (capacidade >= 1),
    item INT,
    FOREIGN KEY (sala) REFERENCES Sala(id_sala),
    FOREIGN KEY (item) REFERENCES Item(id_item)
);

-- Tabela: Afinidade
CREATE TABLE IF NOT EXISTS Afinidade (
    id_afinidade SERIAL PRIMARY KEY,
    qtd_atual INT NOT NULL CHECK (qtd_atual >= 0),
    qtd_max INT NOT NULL CHECK (qtd_max > 0)
);

-- Tabela: Loja
CREATE TABLE IF NOT EXISTS Loja (
    id_loja SERIAL PRIMARY KEY,
    mercador INT NOT NULL,
    sala INT NOT NULL,
    item INT,
    FOREIGN KEY (mercador) REFERENCES NPC(id_npc),
    FOREIGN KEY (sala) REFERENCES Sala(id_sala),
    FOREIGN KEY (item) REFERENCES Item(id_item)
);

-- Tabela: Interação
CREATE TABLE IF NOT EXISTS Interacao (
    id_interacao SERIAL PRIMARY KEY,
    npc INT NOT NULL,
    jogador INT NOT NULL,
    dialogo INT,
    FOREIGN KEY (npc) REFERENCES NPC(id_npc),
    FOREIGN KEY (jogador) REFERENCES Jogador(id_jogador),
    FOREIGN KEY (dialogo) REFERENCES Dialogo(id_dialogo)
);

```

<center>

## Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 07/08/2024 | Primeira versão  do DDL  | [Bianca Castro](https://github.com/BiancaPatrocinio7) |       
| `1.1`  | 17/08/2024 | Correção dos dados do DDL | [Bianca Castro](https://github.com/BiancaPatrocinio7) |
  
</center>

---
