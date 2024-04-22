
# MER - Modelo Entidade Relacionamento

O Modelo Entidade Relacionamento de um bancos de dados é um modelo conceitual que descreve as entidades de um domínio de negócios, com seus atributos e seus relacionamentos.

> Entidades: os objetos da realidade a ser modelada.<br>
> Relacionamentos: as associações entre as entidades.<br>
> Atributos: características específicas de uma entidade.<br>

## 1. Entidades

- **Jogador**
- **Missão**
- **Inventário**
- **Diálogo**
- **NPC**
    - **Mercador**
    - **Aliado**
    - **Monstro**
- **Item**
    - **Armadura**
    - **Consumível**
    - **Chave**
- **Cenário**
- **Afinidade**


## 2. Atributos


- **Jogador**: <ins>id-jogador</ins>, nome, item-equipado, nivel, qtd-xp, cenario-atual, vida-maxima, vida-atual, qtd-gold, dialogo-jogador, inventario-jogador, missao-atual
- **Missão**: <ins>id-missao</ins>, nome, descricao-missao
- **Inventário**: <ins>id-inventario</ins>, qtd-item, id-item
- **Diálogo**: <ins>id-dialogo</ins>, texto-dialogo
- **NPC**: <ins>id-npc</ins>, nome, id-cenario, dialogo-npc
    - **Mercador**: <ins>id-mercador</ins>, nome, id-cenario, dialogo-npc, inventario-mercador
    - **Aliado**: <ins>id-aliado</ins>, nome, id-cenario, dialogo-npc, recompensa-item
    - **Monstro**: <ins>id-monstro</ins>, nome, id-cenario, dialogo-npc,  dano-ataque, recompensa-xp, recompensa-gold
- **Item**: <ins>id-item</ins>, nome, descricao-item, valor-item
    - **Armadura**: <ins>id-armadura</ins>, nome, descricao-item, valor-item, qtd-defesa
    - **Consumível**: <ins>id-consumivel</ins>, nome, descricao-item, valor-item, qtd-cura
    - **Chave**: <ins>id-chave</ins>, nome, descricao-item, valor-item, cenario-destino
- **Cenário:** <ins>id-cenario</ins>, nome, tipo, descricao-cenario
- **Afinidade:**: <ins>id-afinidade</ins>, afinidade-atual, afinidade-maxima



## 3. Relacionamentos

**Jogador _está_ em Cenário**

- O jogador está em apenas um único cenário (1,1)
- O cenário pode conter nenhum ou vários jogadores(0,N)

**Jogador_fala_ Diálogo**

- Um jogador possui nenhuma a várias falas em um diálogo (0, N)
- Um Dialogo pertence a um único jogador(1, 1)


**Jogador _realiza_ Missao**

- O jogador realiza nenhuma ou várias missões (0,N)
- A missão é realizada por apenas um ou vários jogadores (1,N)

**Jogador _possui_ Item**

- O jogador possui de nenhum a vários itens (0,N)
- O item é de apenas um único jogador (1,1)

**Jogador _possui_ Inventário**

- O jogador possui apenas 1 inventário (1,1)
- O inventário é de apenas um único jogador (1,1)


**Missão _está disponível_ em Cenario**

- A missão está disponível em uma ou até dois cenários (1,3)
- O cenário contém de uma a várias missões (1, N)

**Missão _libera_ Chave**

- A missão libera somente uma chave para 


**Inventário _possui_ Item**

- O inventário do jogador pode possuir nenhum a vários itens (0,N)
- O item aparece em nenhum a vários inventários (0, N)


**NPC _fala_ Diálogo**

- Um NPC possui nenhuma a várias falas em um diálogo (0, N)
- Um Dialogo pertence a um único NPC (1, 1)


**Mercador _negocia_ Item**

- O mercador pode negociar uma ou vários itens (1,N)
- O item pode ser neogicado por um ou vários mercadores (1, N)

**Monstro _possui_ Afinidade**

- Monstro possui apenas uma única afinidade (1, 1)
- Uma afinidade faz parte de vários monstros (1, N)



**Item _possui exclusivamente_ tipos**

- Um item pode ser classificado **apenas com uma única** das seguintes categorias: armadura, consumível, chave


**NPC _possui exclusivamente_ tipos**

- Um NPC pode ser classificado **apenas com uma única** das seguintes categorias: mercador, aliado, monstro





## Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 21/04/2024 | Primeira versão  do MER  | [Bianca Castro](https://github.com/BiancaPatrocinio7) e [Samara Letícia](https://github.com/samarawwleticia) |                                                              
