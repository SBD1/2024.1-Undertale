# MER - Modelo Entidade Relacionamento

## Introdução

O Modelo Entidade Relacionamento de um banco de dados é um modelo conceitual que descreve as entidades de um domínio de negócios, com seus atributos e seus relacionamentos.

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

## Atributos

- **Jogador**: {<ins>id-jogador</ins>,sala, missao, inventario, nome, item-equipado, nivel, qtd-xp, vida-maxima, vida-atual, afinidade, tipo-rota}
- **Missão**: {<ins>id-missao</ins>, nome, descricao, status}
- **Inventário**: {qtd-item, tamanho-total, qtd-gold, jogador, item }
- **Loja**: {<ins>id-loja</ins>, mercador , sala }
- **Diálogo**: {<ins>id-dialogo</ins>, texto, npc }
- **NPC**: {<ins>id-npc</ins>, nome, sala, dialogo, tipo, sala, afinidade }
    - **Mercador**: {loja}
    - **Aliado**: {gold-drop, xp-drop, dano-ataque }
    - **Monstro**: {dano-ataque, xp-drop, gold-drop, item-drop  }
- **Item**: {<ins>id-item</ins>, nome, descricao, valor, tipo}
	- **Instância-item**
	    - **Defesa**: {protecao}
	    - **Consumível**: {qtd-cura}
	    - **Ataque**: {dano, item }
- **Sala**: {<ins>id-sala</ins>, nome, descricao, porta }
- **Porta**: {<ins>id-porta</ins>, status, sala }
- **Baú**: {<ins>id-bau</ins>, item, sala, capacidade, sala , item }
- **Afinidade**: {<ins>id-afinidade</ins>, qtd-atual, qtd-max}

## Relacionamentos

- **Jogador _está_ em Sala**
  - (1,1) **Jogador** está em uma **Sala**
  - (0,N) **Sala** pode conter vários **Jogadores**

- **Interação _possui_ Diálogo**
  - (0,N) **Interação** pode possuir vários **Diálogos**
  - (1,1) **Diálogo** pertence a uma **Interação**

- **Jogador _realiza_ Missão**
  - (0,N) **Jogador** pode realizar várias **Missões**
  - (1,N) **Missão** é realizada por vários **Jogadores**

- **Jogador _possui_ Inventário**
  - (1,1) **Jogador** possui um **Inventário**
  - (1,1) **Inventário** pertence a um **Jogador**

- **Missão _está disponível_ em Sala**
  - (1,3) **Missão** está disponível em uma a três **Salas**
  - (1,N) **Sala** contém várias **Missões**

- **Missão _libera_ Porta**
  - (1,1) **Missão** libera uma **Porta**
  - (0,1) **Porta** é liberada por uma **Missão**

- **Inventário _possui_ Item**
  - (0,N) **Inventário** pode possuir vários **Itens**
  - (0,N) **Item** pode aparecer em vários **Inventários**

- **Item _possui_ Instância-Item**
  - (1,N) **Item** pode possuir várias **Instâncias-Item**
  - (1,1) **Instância-Item** pertence a um **Item**

- **NPC _fala_ Diálogo**
  - (0,N) **NPC** pode ter várias falas em um **Diálogo**
  - (1,1) **Diálogo** pertence a um **NPC**

- **Mercador _negocia_ Item**
  - (1,N) **Mercador** pode negociar vários **Itens**
  - (1,N) **Item** pode ser negociado por vários **Mercadores**

- **Monstro _possui_ Afinidade**
  - (1,1) **Monstro** possui uma **Afinidade**
  - (1,N) **Afinidade** pode pertencer a vários **Monstros**

- **Item _possui exclusivamente_ tipos**
  - (1,1) **Item** pode ser classificado apenas como **Defesa**, **Consumível** ou **Ataque**

- **NPC _possui exclusivamente_ tipos**
  - (1,1) **NPC** pode ser classificado apenas como **Mercador**, **Aliado** ou **Monstro**

<center>

## Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 21/04/2024 | Primeira versão do MER | [Bianca Castro](https://github.com/BiancaPatrocinio7) e [Samara Letícia](https://github.com/samarawwleticia) |       
| `1.1`  | 21/07/2024 | Atualizando os atributos e relacionamentos | [Bianca Castro](https://github.com/BiancaPatrocinio7)  |                                                              
| `1.2`  | 22/07/2024 | V1 MR | [Diego Carlito](https://github.com/DiegoCarlito) e [Bianca Castro](https://github.com/BiancaPatrocinio7)|    
| `1.3` | 13/08/2024 | V2 MER | [Marcos Castilhos](https://github.com/Marcosatc147) e [Bianca Castro](https://github.com/BiancaPatrocinio7) |
</center>
