# Linguagem de Manipulação de Dados (MDL)

## Introdução

A Data Manipulation Language (DML), ou Linguagem de Manipulação de Dados, é uma parte essencial do SQL (Structured Query Language), utilizada para gerenciar e manipular dados dentro de um banco de dados relacional. Os comandos DML permitem que os desenvolvedores e administradores de banco de dados realizem tarefas essenciais como inserção, atualização, remoção e consulta de dados. Esses comandos são fundamentais para garantir que as informações sejam mantidas atualizadas e precisas, permitindo assim que as aplicações que dependem desses dados funcionem corretamente.


#### 1. Inserção de Dados

```sql
-- Inserir um novo jogador
INSERT INTO Jogador (nome, item_equipado, nivel, qtd_xp, vida_maxima, vida_atual, afinidade, tipo_rota)
VALUES ('Frisk', NULL, 1, 0, 100, 100, 0, 'Pacifista');

-- Inserir uma nova missão
INSERT INTO Missao (nome, descricao, status)
VALUES ('Resolva o puzzle', 'Resolva o puzzle das Ruinas para liberar a porta para a outra sala', 'ativa');

-- Inserir um novo item
INSERT INTO Item (nome, descricao, valor, tipo)
VALUES ('Bandana Viril', '7DF - Tem abdominais nela', 50.00, 'Armadura');

-- Inserir uma nova sala
INSERT INTO Sala (nome_sala, descricao, x_coord, y_coord)
VALUES ('Ruinas', 'A entrada principal do mundo subterraneo', 0, 0);

-- Inserir uma nova conexão entre salas
INSERT INTO Conexao (id_sala_origem, id_sala_destino, direcao, descricao_conexao)
VALUES (1, 2, 'Norte', 'Caminho que leva ao centro das ruinas');

-- Inserir um novo NPC
INSERT INTO NPC (nome, sala, tipo)
VALUES ('Flowey', 1, 'Aliado');

-- Inserir um novo mercador
INSERT INTO Mercador (loja)
VALUES (1);

-- Inserir um novo aliado
INSERT INTO Aliado (id_npc, gold_drop, xp_drop, dano_ataque)
VALUES (1, 10, 20, 5);

-- Inserir um novo monstro
INSERT INTO Monstro (id_npc, dano_ataque, xp_drop, gold_drop, item_drop)
VALUES (2, 15, 30, 10, 1);

-- Inserir uma nova defesa
INSERT INTO Defesa (id_instancia, protecao)
VALUES (1, 10);

-- Inserir um novo consumível
INSERT INTO Consumivel (id_instancia, qtd_cura)
VALUES (2, 20);

-- Inserir um novo ataque
INSERT INTO Ataque (id_instancia, dano)
VALUES (3, 25);

-- Inserir uma nova porta
INSERT INTO Porta (status, sala)
VALUES ('Fechada', 1);

-- Inserir um novo baú
INSERT INTO Bau (sala, capacidade, item)
VALUES (1, 5, 1);

-- Inserir uma nova afinidade
INSERT INTO Afinidade (qtd_atual, qtd_max)
VALUES (0, 100);

-- Inserir uma nova loja
INSERT INTO Loja (mercador, sala, item)
VALUES (1, 1, 1);

-- Inserir uma nova interação
INSERT INTO Interacao (npc, jogador, dialogo)
VALUES (1, 1, 1);
```

#### 2. Atualização de Dados

```sql
-- Atualizar o nível do jogador
UPDATE Jogador
SET nivel = 2
WHERE id_jogador = 1;

-- Atualizar o status da missão
UPDATE Missao
SET status = 'concluída'
WHERE id_missao = 1;

-- Atualizar a descrição de um item
UPDATE Item
SET descricao = 'Espada de ferro com lâmina afiada.'
WHERE id_item = 1;

-- Atualizar a quantidade de cura de um consumível
UPDATE Consumivel
SET qtd_cura = 30
WHERE id_instancia = 2;
```

#### 3. Exclusão de Dados

```sql
-- Excluir um jogador
DELETE FROM Jogador
WHERE id_jogador = 1;

-- Excluir uma missão
DELETE FROM Missao
WHERE id_missao = 1;

-- Excluir um item
DELETE FROM Item
WHERE id_item = 1;

-- Exclusão em cascata com relação às chaves estrangeiras

-- Excluir uma sala e suas conexões
DELETE FROM Sala
WHERE id_sala = 1;
```

#### 4. Consulta de Dados

```sql
-- Consultar todos os jogadores
SELECT * FROM Jogador;

-- Consultar todas as missões ativas
SELECT * FROM Missao
WHERE status = 'ativa';

-- Consultar todos os itens do tipo 'Armadura'
SELECT * FROM Item
WHERE tipo = 'Armadura';

-- Consultar todos os NPCs em uma sala específica
SELECT * FROM NPC
WHERE sala = 1;

-- Consultar todas as conexões entre salas
SELECT * FROM Conexao;

-- Consultar todos os aliados e suas características
SELECT * FROM Aliado;

-- Consultar todos os monstros e seus itens de drop
SELECT * FROM Monstro
JOIN Item ON Monstro.item_drop = Item.id_item;
```

<center>


### Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 07/08/2024 | Criação do documento  | [Bianca Castro](https://github.com/BiancaPatrocinio7) |   
| `1.1`  | 17/08/2024 | Primeira versão do DML | [Bianca Castro](https://github.com/BiancaPatrocinio7) |
</center>