# MER - Modelo Entidade Relacionamento

## Introdução

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
	- **Instância-item**
	     - **Defesa**
	     - **Consumível**
	    - **Ataque**
- **Sala**
- **Afinidade**
- **Baú**
- **Porta**
- **Loja**
- **Interação** 

## Atributos

- *Jogador*: {<ins>id</ins>, nome, item-equipado, nivel, qtd-xp, vida-maxima, vida-atual, afinidade-id, tipo-rota}
- *Missão*: {<ins>id-missao</ins>, nome, descricao-missao, status}
- *Inventário*: {<ins>id-jogador</ins>, qtd-item, tamanho-total, qtd-gold }
- *Loja*: {<ins>id-loja</ins>, mercador-id , sala-id, item-id }
- *Diálogo*: {<ins>id-dialogo</ins>, texto-dialogo, interacao-id }
- *NPC*: {<ins>id-npc</ins>, nome, dialogo-npc, tipo, sala-id }
    - *Mercador*: {id-loja}
    - *Aliado*: {gold-drop, xp-drop, dano-ataque}
    - *Monstro*: {dano-ataque, xp-drop, gold-drop, item-drop }
- *Item*: {<ins>id-item</ins>, nome, descricao-item, valor-item, tipo}
	- *Instância-item*: {id-instancia}
	    - *Defesa*: {protecao}
	    - *Consumível*: {qtd-cura}
	    - *Ataque*: {dano}
- *Sala*: {<ins>id-sala</ins>, nome, descricao, porta-id }
- *Porta*: {<ins>id-porta</ins>, status, sala-id }
- *Baú*: {<ins>id-bau</ins>, capacidade, sala-id, item-id}
- *Afinidade*: {<ins>id-afinidade</ins>, qtd-atual, qtd-max}
- *Interação*: {<ins>id-interação</ins>, id-npc, id-jogador, dialogo}


## Relacionamentos

- **Jogador _está_ em Sala**
  - (1,1) Jogador está em uma sala
  - (0,N) Sala pode conter vários jogadores

- **Interação _possui_ Diálogo**
  - (0,N) Interação pode possuir vários diálogos
  - (1,1) Diálogo pertence a uma interação

- **Jogador _realiza_ Missão**
  - (0,N) Jogador pode realizar várias missões
  - (1,N) Missão é realizada por vários jogadores

- **Jogador _possui_ Inventário**
  - (1,1) Jogador possui um inventário
  - (1,1) Inventário pertence a um jogador

- **Jogador _encontra_ Npc**
  - (0,N) Jogador pode encontrar vários NPCS
  - (0,N) NPC se encontra com vários jogadores

- **Jogador _possui_ Afinidade**
  - (1,1) Jogador possui afinidade
  - (1,1) Afinidade pertence a um jogador
 
- **Sala _possui_ Porta**
  - (0,N) Sala pode possuir várias portas
  - (1,1) Porta está em uma sala
 
- **Sala _possui_ Baú**
  - (0,1) Sala pode possuir um baú
  - (1,1) Baú está em uma sala

- **Sala _possui_ Loja**
  - (0,1) Sala pode possuir uma loja
  - (1,1) Loja está em uma sala
    
- **Missão _está disponível_ em Sala**
  - (1,3) Missão está disponível em um a três Salas
  - (0,N) Sala contém várias missões

- **Missão _desbloqueia_ Porta**
  - (1,1) Missão desloqueia uma Porta
  - (0,1) Porta é desbloqueada por uma missão

- **Inventário _possui_ Item**
  - (0,N) Inventário pode possuir vários itens
  - (0,N) Item pode aparecer em vários inventários
  
  **Item _possui_ Instância-Item**
  - (1,N) Item pode possuir várias instâncias
  - (1,1) Instância pertence a um item

- **Item _possui Instância-item**
  - (1,N) Item possui várias instâncias
  - (1,1) Instância está relacionada a um item

- **Mercador _vende_ Item**
  - (0,N) Mercador pode negociar vários itens
  - (1,N) Item pode ser negociado por vários mercadores

- **Loja _possui_ Mercador**
  - (1,1) Loja possui um mercador
  - (1,1) Mercador possui uma loja

- **Loja _possui_ Item**
  - (0,N) Loja possui vários itens
  - (0,N) Item está em várias lojas

- **Item _possui exclusivamente_ tipos**
  - (1,1) Item pode ser classificado apenas como Defesa, Consumível ou Ataque

- **NPC _possui exclusivamente_ tipos**
  - (1,1) NPC pode ser classificado apenas como Mercador, Aliado ou Monstro

<center>

## Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 21/04/2024 | Primeira versão  do MER  | [Bianca Castro](https://github.com/BiancaPatrocinio7) e [Samara Letícia](https://github.com/samarawwleticia) |       
| `1.1`  | 21/07/2024 | Atualizando os atributos e relacionamentos | [Bianca Castro](https://github.com/BiancaPatrocinio7)  |                                                              
| `1.2`  | 22/07/2024 | V1 MR       | [Diego Carlito](https://github.com/DiegoCarlito) e [Bianca Castro](https://github.com/BiancaPatrocinio7)|    
| `1.3` | 13/08/2024 | V2 MER | [Marcos Castilhos](https://github.com/Marcosatc147) e [Bianca Castro](https://github.com/BiancaPatrocinio7) |
</center>
