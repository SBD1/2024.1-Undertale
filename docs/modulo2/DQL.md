
# Data Query Language (DQL)
## Introdução

DQL é a sigla para Data Query Language. É uma linguagem de consulta de dados que permite aos usuários recuperar dados de um banco de dados. O DQL é usado para consultar os dados armazenados em um banco de dados, como recuperar informações específicas de uma tabela ou visualização. O DQL é uma parte importante do projeto físico do banco de dados, pois permite recuperar os dados armazenados no banco de dados.

#### Consulta de Dados

```sql
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
```

### Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 18/08/2024 | Criação do documento  | [Marcos Castilhos](https://github.com/Marcosatc147) e [Bianca Castro](https://github.com/BiancaPatrocinio7) |   