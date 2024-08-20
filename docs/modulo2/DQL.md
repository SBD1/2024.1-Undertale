
# Data Query Language (DQL)
## Introdução

DQL é a sigla para Data Query Language. É uma linguagem de consulta de dados que permite aos usuários recuperar dados de um banco de dados. O DQL é usado para consultar os dados armazenados em um banco de dados, como recuperar informações específicas de uma tabela ou visualização. O DQL é uma parte importante do projeto físico do banco de dados, pois permite recuperar os dados armazenados no banco de dados.

#### Consulta de Dados

```sql
-- Consultar a sala atual do jogador
SELECT sala_atual
FROM Jogador
WHERE id_jogador = 1;

-- Consultar as conexões disponíveis a partir da sala atual
SELECT Conexao.id_sala_destino, Conexao.direcao, Sala.nome_sala
FROM Conexao
JOIN Sala ON Conexao.id_sala_destino = Sala.id_sala
WHERE Conexao.id_sala_origem = (
    SELECT sala_atual
    FROM Jogador
    WHERE id_jogador = 1
);

-- Atualizar a sala atual do jogador após a escolha de direção
UPDATE Jogador
SET sala_atual = (
    SELECT id_sala_destino
    FROM Conexao
    WHERE id_sala_origem = (
        SELECT sala_atual
        FROM Jogador
        WHERE id_jogador = 1
    )
    AND direcao = 'Norte' 
)
WHERE id_jogador = 1;


-- Consultar nome de todos os jogadores
SELECT nome FROM Jogador;

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

-- Consultar o inventário de um jogador específico
SELECT Jogador.nome, Inventario.qtd_item, Inventario.tamanho_total, Inventario.qtd_gold
FROM Inventario
JOIN Jogador ON Inventario.id_jogador = Jogador.id_jogador
WHERE Jogador.nome = 'NomeDoJogador';

-- Consultar os itens que um jogador específico tem equipado
SELECT Jogador.nome, Item.nome AS item_equipado
FROM Jogador
JOIN Item ON Jogador.item_equipado = Item.id_item
WHERE Jogador.nome = 'NomeDoJogador';

-- Consultar a rota seguida por cada jogador
SELECT nome, tipo_rota
FROM Jogador;

-- Consultar todas as salas e os NPCs que estão nelas
SELECT Sala.nome_sala, NPC.nome AS npc_nome
FROM Sala
LEFT JOIN NPC ON Sala.id_sala = NPC.sala;

-- Consultar diálogos possíveis a partir de uma escolha específica
SELECT EscolhaDialogo.escolha, Dialogo.texto AS prox_dialogo_texto
FROM EscolhaDialogo
JOIN Dialogo ON EscolhaDialogo.prox_dialogo = Dialogo.id_dialogo
WHERE EscolhaDialogo.id_dialogo = 1;

-- Consultar o total de XP acumulado por um jogador
SELECT nome, SUM(qtd_xp) AS total_xp
FROM Jogador
GROUP BY nome;

-- Consultar todas as portas trancadas em uma sala específica
SELECT Porta.id_porta, Sala.nome_sala
FROM Porta
JOIN Sala ON Porta.sala = Sala.id_sala
WHERE Porta.status = 'Trancada' AND Sala.id_sala = 1;

-- Consultar jogadores que possuem afinidade máxima
SELECT Jogador.nome, Afinidade.qtd_atual, Afinidade.qtd_max
FROM Jogador
JOIN Afinidade ON Jogador.afinidade = Afinidade.id_afinidade
WHERE Afinidade.qtd_atual = Afinidade.qtd_max;

-- Consultar todos os itens em uma loja específica
SELECT Loja.id_loja, Item.nome AS item_nome, Item.valor
FROM Loja
JOIN Item ON Loja.item = Item.id_item
WHERE Loja.id_loja = 1;

-- Consultar todas as interações entre um jogador e um NPC específico
SELECT Jogador.nome AS jogador_nome, NPC.nome AS npc_nome, Dialogo.texto AS dialogo
FROM Interacao
JOIN Jogador ON Interacao.jogador = Jogador.id_jogador
JOIN NPC ON Interacao.npc = NPC.id_npc
LEFT JOIN Dialogo ON Interacao.dialogo = Dialogo.id_dialogo
WHERE NPC.nome = 'NomeDoNPC' AND Jogador.nome = 'NomeDoJogador';

--- Consultar Lojas e Seus respectivos Mercadores
SELECT loja.nome, mercador.nome
FROM loja 
JOIN mercador ON id_loja = loja;

```

### Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 18/08/2024 | Criação do documento  | [Marcos Castilhos](https://github.com/Marcosatc147) e [Bianca Castro](https://github.com/BiancaPatrocinio7) |   