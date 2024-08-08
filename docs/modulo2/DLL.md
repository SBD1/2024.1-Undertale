
# Linguagem de Definição de Dados (DDL)

## Introdução

A Linguagem de Definição de Dados (DDL), ou Data Definition Language, é um conjunto de comandos usados em sistemas de gerenciamento de banco de dados (SGBD) para criar, alterar e gerenciar a estrutura dos bancos de dados. 


## DDL - Undertale

Após a modelagem criamos todas as tabelas mapeadas com a ajuda do DD (Data Dictionary) para dar progresso ao trabalho.

```sql
BEGIN;

-- Criação da tabela Jogador
CREATE TABLE Jogador (
    id_jogador INT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    item_equipado INT,
    inventario_jogador INT NOT NULL,
    dialogo_jogador INT,
    missao_atual INT,
    nivel INT NOT NULL CHECK (nivel BETWEEN 1 AND 100),
    qtd_xp INT NOT NULL CHECK (qtd_xp BETWEEN 1 AND 100),
    vida_maxima INT NOT NULL CHECK (vida_maxima BETWEEN 1 AND 100),
    vida_atual INT NOT NULL CHECK (vida_atual BETWEEN 1 AND 100),
    FOREIGN KEY (item_equipado) REFERENCES Item(id_item),
    FOREIGN KEY (inventario_jogador) REFERENCES Inventario(id_jogador),
    FOREIGN KEY (dialogo_jogador) REFERENCES Dialogo(id_dialogo),
    FOREIGN KEY (missao_atual) REFERENCES Missao(id_missao)
);

-- Criação da tabela Missao
CREATE TABLE Missao (
    id_missao INT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    descricao_missao VARCHAR(150)
);

-- Criação da tabela Loja
CREATE TABLE Loja (
    id_loja INT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    id_cenario INT NOT NULL,
    id_item INT NOT NULL,
    FOREIGN KEY (id_cenario) REFERENCES Cenário(id_cenario),
    FOREIGN KEY (id_item) REFERENCES Item(id_item)
);

-- Criação da tabela Inventario
CREATE TABLE Inventario (
    id_jogador INT PRIMARY KEY,
    id_item INT NOT NULL,
    qtd_item INT NOT NULL CHECK (qtd_item >= 0),
    qtd_gold INT CHECK (qtd_gold >= 0),
    FOREIGN KEY (id_item) REFERENCES Item(id_item),
    FOREIGN KEY (id_jogador) REFERENCES Jogador(id_jogador)
);

-- Criação da tabela Dialogo
CREATE TABLE Dialogo (
    id_dialogo INT PRIMARY KEY,
    texto_dialogo VARCHAR(255) NOT NULL
);

-- Criação da tabela NPC
CREATE TABLE NPC (
    id_npc INT PRIMARY KEY,
    id_cenario INT NOT NULL,
    nome VARCHAR(50) NOT NULL,
    dialogo_npc VARCHAR(255),
    FOREIGN KEY (id_cenario) REFERENCES Cenário(id_cenario)
);

-- Criação da tabela Aliado
CREATE TABLE Aliado (
    id_aliado INT PRIMARY KEY,
    id_npc INT NOT NULL,
    recompensa_item INT NOT NULL,
    FOREIGN KEY (id_npc) REFERENCES NPC(id_npc),
    FOREIGN KEY (recompensa_item) REFERENCES Item(id_item)
);

-- Criação da tabela Monstro
CREATE TABLE Monstro (
    id_monstro INT PRIMARY KEY,
    id_npc INT NOT NULL,
    recompensa_xp INT NOT NULL CHECK (recompensa_xp BETWEEN 1 AND 1000),
    recompensa_gold INT NOT NULL CHECK (recompensa_gold BETWEEN 1 AND 1000),
    FOREIGN KEY (id_npc) REFERENCES NPC(id_npc)
);

-- Criação da tabela Mercador
CREATE TABLE Mercador (
    id_mercador INT PRIMARY KEY,
    id_npc INT NOT NULL,
    id_loja INT NOT NULL,
    FOREIGN KEY (id_npc) REFERENCES NPC(id_npc),
    FOREIGN KEY (id_loja) REFERENCES Loja(id_loja)
);

-- Criação da tabela Cenário
CREATE TABLE Cenário (
    id_cenario INT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    descricao_cenario VARCHAR(50) NOT NULL,
    tipo VARCHAR(50) NOT NULL
);

-- Criação da tabela Item
CREATE TABLE Item (
    id_item INT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    valor_item INT NOT NULL CHECK (valor_item BETWEEN 1 AND 1500),
    descricao_item VARCHAR(100)
);

-- Criação da tabela Chave
CREATE TABLE Chave (
    id_chave INT PRIMARY KEY,
    id_item INT NOT NULL,
    cenario_destino INT NOT NULL,
    FOREIGN KEY (id_item) REFERENCES Item(id_item),
    FOREIGN KEY (cenario_destino) REFERENCES Cenário(id_cenario)
);

-- Criação da tabela Armadura
CREATE TABLE Armadura (
    id_armadura INT PRIMARY KEY,
    id_item INT NOT NULL,
    qtd_defesa INT NOT NULL CHECK (qtd_defesa BETWEEN 1 AND 1000),
    FOREIGN KEY (id_item) REFERENCES Item(id_item)
);

-- Criação da tabela Consumível
CREATE TABLE Consumível (
    id_consumivel INT PRIMARY KEY,
    id_item INT NOT NULL,
    qtd_cura INT NOT NULL CHECK (qtd_cura BETWEEN 1 AND 100),
    FOREIGN KEY (id_item) REFERENCES Item(id_item)
);

COMMIT;

```


<center>

## Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 07/08/2024 | Primeira versão  do DDL  | [Bianca Castro](https://github.com/BiancaPatrocinio7) |       
  
</center>