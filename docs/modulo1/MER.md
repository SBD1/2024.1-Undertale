# MER - Modelo Entidade Relacionamento

O Modelo Entidade Relacionamento de um bancos de dados é um modelo conceitual que descreve as entidades de um domínio de negócios, com seus atributos e seus relacionamentos.

> Entidades: os objetos da realidade a ser modelada.<br>
> Relacionamentos: as associações entre as entidades.<br>
> Atributos: características específicas de uma entidade.<br>


## Entidades

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

## Atributos

- **Jogador**:{<ins>id-jogador</ins>, nome, item-equipado, nivel, qtd-xp, cenario-atual, vida-maxima, vida-atual, dialogo-jogador, inventario-jogador, missao-atual, afinidade}
- **Missão**:{<ins>id-missao</ins>, nome, descricao-missao}
- **Inventário**:{<ins>id-inventario</ins>, qtd-item, id-item, qtd-gold}
- **Loja**:{<ins>id-loja</ins>, nome, id-item, id-cenario}
- **Diálogo**:{<ins>id-dialogo</ins>, texto-dialogo}
- **NPC**:{<ins>id-npc</ins>, nome, id-cenario, dialogo-npc}
     - **Mercador**:{<ins>id-mercador</ins>, id-loja}
     - **Aliado**:{<ins>id-aliado</ins>, recompensa-item}
     - **Monstro**:{<ins>id-monstro</ins>, dano-ataque, recompensa-xp, recompensa-gold}
- **Item**: {<ins>id-item</ins>, nome, descricao-item, valor-item}
     - **Armadura**: {<ins>id-item</ins>, qtd-defesa}
      - **Consumível**: {<ins>id-item</ins>, qtd-cura}
      - **Chave**: {<ins>id-item</ins>, cenario-destino}
- **Cenário**: {<ins>id-cenario</ins>, nome, tipo, descricao-cenario}
- **Afinidade**: {<ins>id-afinidade</ins>, afinidade-atual, afinidade-maxima}

## Relacionamentos

- **Jogador _está_ em Cenário**
  - (1,1) Jogador está em um cenário
  - (0,N) Cenário pode conter vários jogadores

- **Jogador _fala_ Diálogo**
  - (0,N) Jogador pode ter várias falas em um diálogo
  - (1,1) Diálogo pertence a um jogador

- **Jogador _realiza_ Missão**
  - (0,N) Jogador pode realizar várias missões
  - (1,N) Missão é realizada por vários jogadores

- **Jogador _possui_ Item**
  - (0,N) Jogador pode possuir vários itens
  - (1,1) Item pertence a um jogador

- **Jogador _possui_ Inventário**
  - (1,1) Jogador possui um inventário
  - (1,1) Inventário pertence a um jogador

- **Missão _está disponível_ em Cenário**
  - (1,3) Missão está disponível em um a três cenários
  - (1,N) Cenário contém várias missões

- **Missão _libera_ Chave**
  - (1,1) Missão libera uma chave
  - (0,1) Chave é liberada por uma missão

- **Inventário _possui_ Item**
  - (0,N) Inventário pode possuir vários itens
  - (0,N) Item pode aparecer em vários inventários

- **NPC _fala_ Diálogo**
  - (0,N) NPC pode ter várias falas em um diálogo
  - (1,1) Diálogo pertence a um NPC

- **Mercador _negocia_ Item**
  - (1,N) Mercador pode negociar vários itens
  - (1,N) Item pode ser negociado por vários mercadores

- **Monstro _possui_ Afinidade**
  - (1,1) Monstro possui uma afinidade
  - (1,N) Afinidade pode pertencer a vários monstros

- **Item _possui exclusivamente_ tipos**
  - (1,1) Item pode ser classificado apenas como Armadura, Consumível ou Chave

- **NPC _possui exclusivamente_ tipos**
  - (1,1) NPC pode ser classificado apenas como Mercador, Aliado ou Monstro

<center>

## Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 21/04/2024 | Primeira versão  do MER  | [Bianca Castro](https://github.com/BiancaPatrocinio7) e [Samara Letícia](https://github.com/samarawwleticia) |       
| `1.1`  | 21/07/2024 | Atualizando os atributos e relacionamentos | [Bianca Castro](https://github.com/BiancaPatrocinio7)  |                                                              
| `1.2`  | 22/07/2024 | V1 MR       | [Diego Carlito](https://github.com/DiegoCarlito) e [Bianca Castro](https://github.com/BiancaPatrocinio7)|         
</center>