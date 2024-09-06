# Linguagem de Manipulação de Dados (MDL)

## Introdução

A Data Manipulation Language (DML), ou Linguagem de Manipulação de Dados, é uma parte essencial do SQL (Structured Query Language), utilizada para gerenciar e manipular dados dentro de um banco de dados relacional. Os comandos DML permitem que os desenvolvedores e administradores de banco de dados realizem tarefas essenciais como inserção, atualização, remoção e consulta de dados. Esses comandos são fundamentais para garantir que as informações sejam mantidas atualizadas e precisas, permitindo assim que as aplicações que dependem desses dados funcionem corretamente.


#### 1. Inserção de Dados

```sql


-- Inserir uma nova missão
INSERT INTO undertale_schema.Missao (nome, descricao, status)
VALUES ('Resolva o puzzle', 'Resolva o puzzle das Ruinas para liberar a porta para a outra sala', 'ativa');

-- Inserir um novo item
INSERT INTO undertale_schema.Item (nome, descricao, valor, tipo)
VALUES ('Bandana Viril', '7DF - Tem abdominais nela', 50.00, 'Defesa');

-- Inserir um novo item
INSERT INTO undertale_schema.Item (nome, descricao, valor, tipo)
VALUES ('Luva Forte', '5AT Na cara deles.', 50.00, 'Ataque');

-- Inserir um novo item
INSERT INTO undertale_schema.Item (nome, descricao, valor, tipo)
VALUES ('Maçã de Siri', 'CR18 HP (Parece um siri.)', 25.00, 'Consumíve');

-- Inserir uma nova sala
INSERT INTO undertale_schema.Sala (nome_sala, descricao)
VALUES ('Ruinas', 'A entrada principal do mundo subterraneo');

INSERT INTO undertale_schema.Sala (nome_sala, descricao)
VALUES ('Cachoeiras', 'Lugar misterioso protegido por uma poderosa guardiã');

-- Inserir uma nova conexão entre salas
INSERT INTO undertale_schema.Conexao (id_sala_origem, id_sala_destino, direcao, descricao_conexao)
VALUES (1, 2, 'Norte', 'Caminho que leva ao centro das ruinas');

-- ALIADOS
--- Inserir Flowey como Aliado
INSERT INTO undertale_schema.Aliado (nome, sala, tipo, gold_drop, xp_drop, dano_ataque)
VALUES ('Flowey', NULL, 'Aliado', 20, 10, 99);

-- Inserir Toriel como Aliado
INSERT INTO undertale_schema.Aliado (nome, sala, tipo, gold_drop, xp_drop, dano_ataque)
VALUES ('Toriel', NULL, 'Aliado', 15, 5, 10);

-- Inserir Sans como Aliado
INSERT INTO undertale_schema.Aliado (nome, sala, tipo, gold_drop, xp_drop, dano_ataque)
VALUES ('Sans', NULL, 'Aliado', 25, 30, 20);

-- Inserir Papyrus como Aliado
INSERT INTO undertale_schema.Aliado (nome, sala, tipo, gold_drop, xp_drop, dano_ataque)
VALUES ('Papyrus', NULL, 'Aliado', 20, 25, 15);

-- MONSTROS
-- Inserir Napstablook como Monstro
INSERT INTO undertale_schema.Monstro (nome, sala, tipo, dano_ataque, xp_drop, gold_drop, item_drop)
VALUES ('Napstablook', NULL, 'Monstro', 5, 5, 10, NULL);

-- Inserir Doggo como Monstro
INSERT INTO undertale_schema.Monstro (nome, sala, tipo, dano_ataque, xp_drop, gold_drop, item_drop)
VALUES ('Doggo', NULL, 'Monstro', 12, 30, 15, NULL);

-- Inserir Dogamy e Dogaressa como Monstros
INSERT INTO undertale_schema.Monstro (nome, sala, tipo, dano_ataque, xp_drop, gold_drop, item_drop)
VALUES ('Dogamy e Dogaressa', NULL, 'Monstro', 40, 40, 20, NULL);

-- Inserir Dogão como Monstro
INSERT INTO undertale_schema.Monstro (nome, sala, tipo, dano_ataque, xp_drop, gold_drop, item_drop)
VALUES ('Dogão', NULL, 'Monstro', 80, 60, 50, NULL);

-- Inserir uma nova loja
INSERT INTO undertale_schema.Loja (nome, sala, item)
VALUES ('Loja de Nevada', 1, 1);

INSERT INTO undertale_schema.Loja (nome, sala, item)
VALUES ('Loja do Gerson', 2, 1);

-- MERCADOR
-- Inserir Lojista de Nevada como Mercador
INSERT INTO undertale_schema.Mercador (nome, sala, tipo, loja)
VALUES ('Lojista de Nevada', NULL, 'Mercador', 1);

-- Inserir Gerson como Mercador
INSERT INTO undertale_schema.Mercador (nome, sala, tipo, loja)
VALUES ('Gerson', 2, 'Mercador', 2);


-- Inserir instâncias
INSERT INTO undertale_schema.Instancia_item (id_instancia, item)
VALUES (1, 1);

-- Inserir uma nova defesa
INSERT INTO undertale_schema.Defesa (id_instancia, protecao)
VALUES (1, 10);

-- Inserir um novo consumível
INSERT INTO undertale_schema.Consumivel (id_instancia, qtd_cura)
VALUES (2, 20);

-- Inserir um novo ataque
INSERT INTO undertale_schema.Ataque (id_instancia, dano)
VALUES (3, 25);

-- Inserir uma nova porta
INSERT INTO undertale_schema.Porta (status, sala)
VALUES ('Fechada', 1);

-- Inserir um novo baú
INSERT INTO undertale_schema.Bau (sala, capacidade, item)
VALUES (1, 5, 1);

-- Inserir uma nova afinidade
INSERT INTO undertale_schema.Afinidade (qtd_atual, qtd_max)
VALUES (0, 100);

INSERT INTO undertale_schema.Jogador (nome, item_equipado, nivel, qtd_xp, vida_maxima, vida_atual, afinidade, tipo_rota)
VALUES ('Frisk', NULL, 1, 0, 100, 100, 0, 'Pacifista');

-- Inserir uma nova interação
INSERT INTO undertale_schema.Interacao (npc, jogador, dialogo)
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

<center>


### Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 07/08/2024 | Criação do documento  | [Bianca Castro](https://github.com/BiancaPatrocinio7) |   
| `1.1`  | 17/08/2024 | Primeira versão do DML | [Bianca Castro](https://github.com/BiancaPatrocinio7) |
| `1.2`  | 18/08/2024 | Adicionando algumas informações do jogo | [Marcos Castilhos](https://github.com/Marcosatc147) |
</center>