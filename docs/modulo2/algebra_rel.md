# Algebra Relacional

## Introdução

A álgebra relacional é uma linguagem formal utilizada para manipular e consultar dados em bancos de dados relacionais. Ela fornece um conjunto de operações básicas, como seleção, projeção, união, diferença, produto cartesiano e junção, que permitem extrair e combinar dados de tabelas de forma precisa e matemática. Essas operações são fundamentais para a execução de consultas em SQL, pois definem como os dados devem ser filtrados, transformados e combinados para produzir os resultados desejados. A álgebra relacional serve como base teórica para a implementação e otimização de sistemas de gerenciamento de bancos de dados (SGBDs).

### Consultas

Algumas consultas realizadas no projeto:

Claro! Aqui estão as consultas convertidas para álgebra relacional no formato solicitado:

### 1. Consultar sala atual de um jogador
```π sala_atual (σ id_jogador=1 (Jogador))```

### 2. Consultar conexões disponíveis a partir da sala atual
```π Conexao.id_sala_destino, Conexao.direcao, Sala.nome_sala (σ Conexao.id_sala_origem = π sala_atual (σ id_jogador=1 (Jogador)) (Conexao ⨝ Sala))```

### 3. Atualizar a sala atual do jogador após a escolha de direção
```π id_sala_destino (σ Conexao.id_sala_origem = π sala_atual (σ id_jogador=1 (Jogador)) ∧ direcao='Norte' (Conexao))```

### 4. Consultar nome de todos os jogadores
```π nome (Jogador)```

### 5. Consultar todas as missões ativas
```σ status='ativa' (Missao)```

### 6. Consultar todos os itens do tipo 'Armadura'
```σ tipo='Armadura' (Item)```

### 7. Consultar todos os NPCs em uma sala específica
```σ sala=1 (NPC)```

### 8. Consultar todas as conexões entre salas
```Conexao```

### 9. Consultar todos os aliados e suas características
```Aliado```

### 10. Consultar todos os monstros e seus itens de drop
```Monstro ⨝ Item (Monstro.item_drop = Item.id_item)```

### 11. Consultar o inventário de um jogador específico
```π Jogador.nome, Inventario.qtd_item, Inventario.tamanho_total, Inventario.qtd_gold (σ Jogador.nome='NomeDoJogador' (Inventario ⨝ Jogador (Inventario.id_jogador = Jogador.id_jogador)))```

### 12. Consultar os itens que um jogador específico tem equipado
```π Jogador.nome, Item.nome (σ Jogador.nome='NomeDoJogador' (Jogador ⨝ Item (Jogador.item_equipado = Item.id_item)))```

### 13. Consultar a rota seguida por cada jogador
```π nome, tipo_rota (Jogador)```

### 14. Consultar todas as salas e os NPCs que estão nelas
```π Sala.nome_sala, NPC.nome (Sala ⨝ NPC (Sala.id_sala = NPC.sala))```

### 15. Consultar diálogos possíveis a partir de uma escolha específica
```π EscolhaDialogo.escolha, Dialogo.texto (σ EscolhaDialogo.id_dialogo=1 (EscolhaDialogo ⨝ Dialogo (EscolhaDialogo.prox_dialogo = Dialogo.id_dialogo)))```

### 16. Consultar o total de XP acumulado por um jogador
```γ nome, SUM(qtd_xp)→total_xp (Jogador)```

### 17. Consultar todas as portas trancadas em uma sala específica
```π Porta.id_porta, Sala.nome_sala (σ Porta.status='Trancada' ∧ Sala.id_sala=1 (Porta ⨝ Sala (Porta.sala = Sala.id_sala)))```

### 18. Consultar jogadores que possuem afinidade máxima
```π Jogador.nome, Afinidade.qtd_atual, Afinidade.qtd_max (σ Afinidade.qtd_atual = Afinidade.qtd_max (Jogador ⨝ Afinidade (Jogador.afinidade = Afinidade.id_afinidade)))```

### 19. Consultar todos os itens em uma loja específica
```π Loja.id_loja, Item.nome, Item.valor (σ Loja.id_loja=1 (Loja ⨝ Item (Loja.item = Item.id_item)))```

### 20. Consultar todas as interações entre um jogador e um NPC específico
```π Jogador.nome, NPC.nome, Dialogo.texto (σ NPC.nome='NomeDoNPC' ∧ Jogador.nome='NomeDoJogador' (Interacao ⨝ Jogador (Interacao.jogador = Jogador.id_jogador) ⨝ NPC (Interacao.npc = NPC.id_npc) ⟕ Dialogo (Interacao.dialogo = Dialogo.id_dialogo)))```

### 21. Consultar lojas e seus respectivos mercadores
```π Loja.nome, Mercador.nome (Loja ⨝ Mercador (Loja.id_loja = Mercador.loja))```

<center>

### Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 18/08/2024 | Criação do documento  | [Marcos Castilhos](https://github.com/Marcosatc147) |
| `1.1`  | 19/08/2024 | Atualização das consultas | [Marcos Castilhos](https://github.com/Marcosatc147) |
  
</center>

---