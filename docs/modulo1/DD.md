# DD - Dicionário de Dados

## Introdução

Um dicionário de dados é um recurso essencial na área da ciência de dados e da informática. Ele funciona como um catálogo ou compilação de informações sobre os dados utilizados em um sistema, banco de dados, projeto de pesquisa ou qualquer contexto em que a manipulação e interpretação de dados sejam necessárias.


## Entidade: Exemplo

**Descrição**: Esta entidade serve como um modelo para ilustrar como as informações são organizadas e descritas em um banco de dados. Inclui variáveis típicas, tipos de dados, valores permitidos e restrições.

**Observação**: Esta tabela é usada para exemplificar como preencher um dicionário de dados. Os valores e descrições são fictícios.

| Nome Variável     | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|--------------------------------------------|--------------------|------------------------|
| id-exemplo        | int        | Código de identificação do exemplo           | 1-1000             | PK, Not Null           |
| nome              | varchar(50)| Nome associado ao exemplo                  | a-z, A-Z           | Not Null               |
| data-criacao      | date       | Data em que o exemplo foi criado            | Data válida        | Not Null               |
| valor             | decimal(10,2)| Valor numérico do exemplo                   | 0.00-9999.99       | Not Null, Check (>= 0) |
| ativo             | boolean    | Indicador se o exemplo está ativo ou não    | True, False        | Not Null               |

  <font size="3"><p style="text-align: center"><b>Autores:</b> <a href="https://github.com/BiancaPatrocinio7">Bianca Castro</a>, <a href="https://github.com/Marcosatc147">Marcos Castilhos</a>, 2024</p></font>

<details>
  <summary>Descrição de cada título da coluna</summary>

- "Nomes das variáveis": Identificadores específicos para cada conjunto de dados na tabela, como "id-exemplo" e "nome".<br>

- "Descrições das variáveis": Explicações sobre o que cada variável representa, como "Código de identificação do exemplo" e "Nome associado ao exemplo".<br>

- "Tipos de dados": Tipos de informações armazenadas, como inteiro, texto, data e decimal.<br>

- "Valores permitidos" : Intervalos ou opções permitidas para as variáveis, como "1-1000" para um identificador ou "True, False" para um indicador booleano.<br>

- "Restrições de Domínio": Inclui as restrições adicionais aplicáveis, como "PK" (chave primária), "Not Null" (não pode ser nulo), e "Check" (restrições de valor, como valores mínimos e máximos).


  <font size="3"><p style="text-align: center"><b>Autor:</b> <a href="https://github.com/BiancaPatrocinio7">Bianca Castro</a>, 2024</p></font>
</details>


### **Entidade: Jogador**

| Nome Variável     | Tipo       | Descrição                                   | Valores Permitidos  | Restrições de Domínio |
|-------------------|------------|---------------------------------------------|---------------------|------------------------|
| id-jogador                | int        | Código de identificação do jogador          | 1-5000              | PK, Not Null           |
| nome              | varchar(50)| Nome do jogador                            | a-z, A-Z            | Not Null               |
| item-equipado     | int        | Identificador do item equipado              | 1-5000              | FK                     |
| nivel             | int        | Nível do jogador                            | 1-100               | Not Null, Check (1-100)|
| qtd-xp            | int        | Quantidade de experiência do jogador        | 0-1000              | Not Null, Check (0-1000)|
| vida-maxima       | int        | Limite de vida do jogador                   | 1-1000              | Not Null, Check (1-1000)|
| vida-atual        | int        | Quantidade de vida atual do jogador         | 0-1000              | Not Null, Check (0-1000)|
| afinidade      | int        | Identificador da afinidade do jogador       | 1-5000              | FK, Not Null               |
| tipo-rota         | varchar(50)| Tipo de rota do jogador (Pacifista, Genocida e Neutra)                     | a-z, A-Z            | Not Null               |

---

### **Entidade: Missão**

| Nome Variável      | Tipo        | Descrição                                   | Valores Permitidos  | Restrições de Domínio |
|--------------------|-------------|---------------------------------------------|---------------------|------------------------|
| id-missao          | int         | Código de identificação da missão           | 1-5000              | PK, Not Null           |
| nome               | varchar(50) | Nome da missão                             | a-z, A-Z            | Not Null               |
| descricao   | varchar(150)| Descrição da missão                        | a-z, A-Z            |                        |
| status             | varchar(50) | Status da missão (ativa, concluída, etc.)   | a-z, A-Z            | Not Null               |

---

### **Entidade: Inventário**

| Nome Variável      | Tipo        | Descrição                                   | Valores Permitidos  | Restrições de Domínio |
|--------------------|-------------|---------------------------------------------|---------------------|------------------------|
| qtd-item           | int         | Quantidade de itens no inventário           | 0-10000             | Not Null, Check (0-10000)|
| tamanho-total      | decimal(10,2)| Tamanho total do inventário em unidades    | 0.00-10000.00       | Not Null, Check (>= 0) |
| qtd-gold           | int         | Quantidade de ouro do jogador              | 0-10000             | Not Null, Check (>= 0) |
| id-jogador         | int         | Identificador do jogador                    | 1-5000              | PK, FK, Not Null       |

---

### **Entidade: Diálogo**

| Nome Variável      | Tipo        | Descrição                                   | Valores Permitidos  | Restrições de Domínio |
|--------------------|-------------|---------------------------------------------|---------------------|------------------------|
| id-dialogo         | int         | Código de identificação do diálogo          | 1-5000              | PK, Not Null           |
| texto      | varchar(255)| Texto do diálogo                           | a-z, A-Z            | Not Null               |
| id-interação             | int         | Identificador da interação que está o diálogo     | 1-5000              | FK                     |

---

### **Entidade: NPC**

| Nome Variável      | Tipo        | Descrição                                   | Valores Permitidos  | Restrições de Domínio |
|--------------------|-------------|---------------------------------------------|---------------------|------------------------|
| id-npc             | int         | Código de identificação do NPC              | 1-5000              | PK, Not Null           |
| nome               | varchar(50) | Nome do NPC                                | a-z, A-Z            | Not Null               |
| sala            | int         | Identificador da sala onde o NPC está      | 1-5000              | FK, Null               |
| tipo               | varchar(50) | Tipo de NPC (Mercador, Aliado, Monstro)    | Mercador, Aliado, Monstro | Not Null            |

#### **Mercador**

| Nome Variável      | Tipo        | Descrição                                   | Valores Permitidos  | Restrições de Domínio |
|--------------------|-------------|---------------------------------------------|---------------------|------------------------|
| loja            | int         | Identificador da loja do mercador           | 1-5000              | FK, Not Null           |

#### **Aliado**

| Nome Variável      | Tipo        | Descrição                                   | Valores Permitidos  | Restrições de Domínio |
|--------------------|-------------|---------------------------------------------|---------------------|------------------------|
| gold-drop          | int         | Quantidade de ouro que o aliado pode soltar | 0-10000             | Not Null, Check (>= 0) |
| xp-drop            | int         | Quantidade de XP que o aliado pode soltar  | 0-10000             | Not Null, Check (>= 0) |
| dano-ataque        | int         | Dano de ataque do aliado                    | 0-1000              | Not Null, Check (>= 0) |

#### **Monstro**

| Nome Variável      | Tipo        | Descrição                                   | Valores Permitidos  | Restrições de Domínio |
|--------------------|-------------|---------------------------------------------|---------------------|------------------------|
| dano-ataque        | int         | Dano de ataque do monstro                   | 0-1000              | Not Null, Check (>= 0) |
| xp-drop            | int         | Quantidade de XP que o monstro pode soltar | 0-10000             | Not Null, Check (>= 0) |
| gold-drop          | int         | Quantidade de ouro que o monstro pode soltar | 0-10000           | Not Null, Check (>= 0) |
| item-drop           | int         | Identificador do item associado             | 1-5000              | FK, Not Null           |

---

### **Entidade: Item**

| Nome Variável      | Tipo        | Descrição                                   | Valores Permitidos  | Restrições de Domínio |
|--------------------|-------------|---------------------------------------------|---------------------|------------------------|
| id-item            | int         | Código de identificação do item             | 1-5000              | PK, Not Null           |
| nome               | varchar(50) | Nome do item                                | a-z, A-Z            | Not Null               |
| descricao     | varchar(100)| Descrição do item                           | a-z, A-Z            |                        |
| valor        | decimal(10,2)| Valor do item                               | 0.00-1500.00        | Not Null, Check (>= 0) |
| tipo               | varchar(50) | Tipo do item (Armadura, Consumível, etc.)   | Armadura, Consumível, Chave | Not Null         |

### **Entidade: Instância-Item**

| Nome Variável      | Tipo        | Descrição                                   | Valores Permitidos  | Restrições de Domínio |
|--------------------|-------------|---------------------------------------------|---------------------|------------------------|
| id-instancia            | int         | Código de identificação da instancia            | 1-5000              | PK, Not Null           |
| item            | int         | Código identificador do item que a instância está relacionada             | 1-5000              | FK, Not Null           |


##### **Defesa**

| Nome Variável      | Tipo        | Descrição                                   | Valores Permitidos  | Restrições de Domínio |
|--------------------|-------------|---------------------------------------------|---------------------|------------------------|
| protecao           | int         | Quantidade de proteção fornecida            | 0-1000              | Not Null, Check (>= 0) |

##### **Consumível**

| Nome Variável      | Tipo        | Descrição                                   | Valores Permitidos  | Restrições de Domínio |
|--------------------|-------------|---------------------------------------------|---------------------|------------------------|
| qtd-cura           | int         | Quantidade de cura fornecida                | 0-100              | Not Null, Check (>= 0) |

##### **Ataque**

| Nome Variável      | Tipo        | Descrição                                   | Valores Permitidos  | Restrições de Domínio |
|--------------------|-------------|---------------------------------------------|---------------------|------------------------|
| dano               | int         | Dano de ataque do item                      | 0-1000              | Not Null, Check (>= 0) |


---

### **Entidade: Sala**

| Nome Variável      | Tipo        | Descrição                                   | Valores Permitidos  | Restrições de Domínio |
|--------------------|-------------|---------------------------------------------|---------------------|------------------------|
| id-sala            | int         | Código de identificação da sala             | 1-5000              | PK, Not Null           |
| nome               | varchar(50) | Nome da sala                               | a-z, A-Z            | Not Null               |
| descricao          | varchar(150)| Descrição da sala                          | a-z, A-Z            |                        |
| porta           | int         | Identificador das portas na sala              | 1-5000              | FK, Null               |

---

### **Entidade: Porta**

| Nome Variável      | Tipo        | Descrição                                   | Valores Permitidos  | Restrições de Domínio |
|--------------------|-------------|---------------------------------------------|---------------------|------------------------|
| id-porta           | int         | Código de identificação da porta            | 1-5000              | PK, Not Null           |
| status             | varchar(50) | Status da porta (aberta, fechada, trancada) | Aberta, Fechada, Trancada | Not Null           |
| sala            | int         | Identificador da sala que a porta conecta   | 1-5000              | FK, Not Null           |

---

### **Entidade: Baú**

| Nome Variável      | Tipo        | Descrição                                   | Valores Permitidos  | Restrições de Domínio |
|--------------------|-------------|---------------------------------------------|---------------------|------------------------|
| id-bau             | int         | Código de identificação do baú              | 1-5000              | PK, Not Null           |
| sala            | int         | Identificador da sala onde o baú está      | 1-5000              | FK, Not Null           |
| capacidade         | int         | Capacidade máxima de itens do baú           | 1-1000              | Not Null, Check (>= 1) |
| item            | int         | Identificador do item armazenado            | 1-5000              | FK, Null               |

---

### **Entidade: Afinidade**

| Nome Variável      | Tipo        | Descrição                                   | Valores Permitidos  | Restrições de Domínio |
|--------------------|-------------|---------------------------------------------|---------------------|------------------------|
| id-afinidade       | int         | Código de identificação da afinidade        | 1-5000              | PK, Not Null           |
| qtd-atual          | int         | Quantidade atual de afinidade              | 0-1000              | Not Null, Check (>= 0) |
| qtd-max            | int         | Quantidade máxima de afinidade             | 1-1000              | Not Null, Check (> 0)  |

---

### **Entidade: Loja**

| Nome Variável      | Tipo        | Descrição                                   | Valores Permitidos  | Restrições de Domínio |
|--------------------|-------------|---------------------------------------------|---------------------|------------------------|
| id-loja            | int         | Código de identificação da loja              | 1-5000              | PK, Not Null           |
| mercador        | int         | Identificador do mercador associado          | 1-5000              | FK, Not Null           |
| sala            | int         | Identificador da sala onde a loja está      | 1-5000              | FK, Not Null           |
| item            | int         | Identificador do item que a loja possui            | 1-5000              | FK, Null               |

---

### **Entidade: Interação**

| Nome Variável      | Tipo        | Descrição                                   | Valores Permitidos  | Restrições de Domínio |
|--------------------|-------------|---------------------------------------------|---------------------|------------------------|
| id-interação            | int         | Código de identificação da interação              | 1-5000              | PK, Not Null           |
| npc        | int         | Identificador do npc associado          | 1-5000              | FK, Not Null           |
| jogador            | int         | Identificador do jogador que interagiu     | 1-5000              | FK, Not Null           |
| dialogo           | int         | Identificador do dialogo que ocorreu            | 1-5000              | FK, Null               |

---

       
## Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 21/04/2024 | Primeira versão  do DD    | [Bianca Castro](https://github.com/BiancaPatrocinio7) e [Diego Carlito](https://github.com/DiegoCarlito) | 
| `1.1`  | 21/07/2024 | Normalizando as Entidade e formatando as tabelas | [Bianca Castro](https://github.com/BiancaPatrocinio7)  |                                                              
| `1.2`  | 21/07/2024 | Corrige e adiciona atributos de relacionamento | [Marcos Castilhos](https://github.com/Marcosatc147)  | 
| `1.2`  | 21/07/2024 | Corrige e adiciona atributos  | [Marcos Castilhos](https://github.com/Marcosatc147)  | 
| `1.3`  | 22/07/2024 | V1 do DD | [Bianca Castro](https://github.com/BiancaPatrocinio7)  | 
| `1.4` | 13/08/2024 | V2 do DD | [Marcos Castilhos](https://github.com/Marcosatc147) e [Bianca Castro](https://github.com/BiancaPatrocinio7) |
