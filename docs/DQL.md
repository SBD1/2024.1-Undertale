#### Consulta de Dados

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

### Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 18/08/2024 | Criação do documento  | [Marcos Castilhos](https://github.com/Marcosatc147) e [Bianca Castro](https://github.com/BiancaPatrocinio7) |   