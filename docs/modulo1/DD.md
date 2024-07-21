# DD - Dicionário de Dados

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

  <font size="3"><p style="text-align: center"><b>Autor:</b> <a href="https://github.com/BiancaPatrocinio7">Bianca Castro</a>, 2024</p></font>

<details>
  <summary>Descrição de cada título da coluna</summary>

- "Nomes das variáveis": Identificadores específicos para cada conjunto de dados na tabela, como "id-exemplo" e "nome".<br>

- "Descrições das variáveis": Explicações sobre o que cada variável representa, como "Código de identificação do exemplo" e "Nome associado ao exemplo".<br>

- "Tipos de dados": Tipos de informações armazenadas, como inteiro, texto, data e decimal.<br>

- "Valores permitidos" : Intervalos ou opções permitidas para as variáveis, como "1-1000" para um identificador ou "True, False" para um indicador booleano.<br>

- "Restrições de Domínio": Inclui as restrições adicionais aplicáveis, como "PK" (chave primária), "Not Null" (não pode ser nulo), e "Check" (restrições de valor, como valores mínimos e máximos).


  <font size="3"><p style="text-align: center"><b>Autor:</b> <a href="https://github.com/BiancaPatrocinio7">Bianca Castro</a>, 2024</p></font>
</details>



## Entidade: Jogador

**Descrição**: A entidade Jogador descreve as informações ligadas ao personagem jogável, como número de identificação, localização, região, estação do jogo, missão, nome, nível de saúde e energia, data atual e quantidade de ouro.

**Observação**: Esta tabela possui chaves estrangeiras das entidades `Cenário`, `Inventário`, `Item`, `Diálogo` e `Missão`.

| Nome Variável     | Tipo       | Descrição                                 | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|-------------------------------------------|--------------------|------------------------|
| id-jogador        | int        | Código de identificação do jogador         | 1-5000             | PK                     |
| nome              | varchar(50)| Nome do jogador                           | a-z, A-Z           | Not Null               |
| item-equipado     | int        | Identificador do item equipado            | 1-5000             | FK                     |
| inventario-jogador| int        | Identificador do inventário do jogador    | 1-5000             | FK, Not Null           |
| dialogo-jogador*   | int        | Identificador do diálogo do jogador        | 1-5000             | FK                     |
| missao-atual*      | int        | Identificador da missão atual              | 1-5000             | FK                     |
| nivel             | int        | Nível do jogador                           | 1-100              | Not Null, Check (1-100)|
| qtd-xp            | int        | Quantidade de experiência do jogador       | 1-100              | Not Null, Check (1-100)|
| vida-maxima       | int        | Limite de vida do jogador                  | 1-100              | Not Null, Check (1-100)|
| vida-atual        | int        | Quantidade de vida atual do jogador        | 1-100              | Not Null, Check (1-100)|

---

## Relacionamento Jogador_está_em_Cenário

**Descrição**: Relacionamento Jogador está em cenário, a cada vez que o jogador troca de cenário é atualizado o valor de cenário_atual, por isso o atributo se encontra no relacionamento e não na entidade jogador ou cenário.

| Nome Variável     | Tipo       | Descrição                                 | Valores Permitidos | Restrições de Domínio |
|-------------------|------------|-------------------------------------------|--------------------|------------------------|
| cenario-atual     | int        | Identificador do cenário atual             | 1-5000             | FK, Not Null           |

---

## Entidade: Missão

**Descrição**: A entidade Missão relaciona o número de identificação da missão, seu nome e sua descrição.

| Nome Variável      | Tipo       | Descrição                                  | Valores Permitidos | Restrições de Domínio |
|--------------------|------------|--------------------------------------------|--------------------|------------------------|
| id-missao          | int        | Código de identificação da missão           | 1-5000             | PK                     |
| nome               | varchar(50)| Nome da missão                             | a-z, A-Z           | Not Null               |
| descricao-missao   | varchar(150)| Descrição da missão                        | a-z, A-Z           |                        |

---

## Entidade: Inventário

**Descrição**: A entidade Inventário relaciona o número de identificação do jogador, os itens e a quantidade de itens disponíveis no inventário.

**Observação**: Esta tabela possui chave estrangeira da entidade `Item` e `Jogador`.

| Nome Variável      | Tipo       | Descrição                                 | Valores Permitidos | Restrições de Domínio |
|--------------------|------------|-------------------------------------------|--------------------|------------------------|
| id-jogador      | int        | Identificador do inventário                | 1-5000             | PK                     |
| id-item            | int        | Identificador do item                     | 1-5000             | FK, Not Null           |
| qtd-item           | int        | Quantidade do item                        | 1-5000             | Not Null, Check (>= 0) |
| qtd-gold          | int        | Quantidade de ouro do jogador              | Mínimo 0           | Check (>= 0)           |

---

## Entidade: Diálogo

**Descrição**: A entidade Diálogo relaciona o número de identificação do diálogo e o texto do diálogo.

| Nome Variável      | Tipo       | Descrição                                 | Valores Permitidos | Restrições de Domínio |
|--------------------|------------|-------------------------------------------|--------------------|------------------------|
| id-dialogo         | int        | Identificador do diálogo                   | 1-5000             | PK                     |
| texto-dialogo      | varchar(255)| Texto do diálogo                          | a-z, A-Z           | Not Null               |

---

## Relacionamento Jogador_possui_Afinidade

**Descrição**: Relacionamento Jogador possui afinidade, a cada vez que o jogador adquire mais afinidade é atualizado o valor de qtd_afinidade, por isso o atributo se encontra no relacionamento e não na entidade diálogo ou jogador ou afinidade.

| Nome Variável      | Tipo       | Descrição                                 | Valores Permitidos | Restrições de Domínio |
|--------------------|------------|-------------------------------------------|--------------------|------------------------|
| qtd_afinidade      | int        | Quantidade de afinidade                   | 1-5000             | FK                     |

---

## Entidade: NPC

**Descrição**: A entidade NPC guarda as informações relacionadas aos personagens não-jogáveis, como número de identificação, cenário, nome e diálogos.

**Observação**: Esta tabela possui chaves estrangeiras das entidades `Cenário` e `Diálogo`.

| Nome Variável      | Tipo       | Descrição                                 | Valores Permitidos | Restrições de Domínio |
|--------------------|------------|-------------------------------------------|--------------------|------------------------|
| id-npc             | int        | Código de identificação do NPC             | 1-5000             | PK                     |
| id-cenario         | int        | Identificador do cenário onde o NPC está  | 1-5000             | FK, Not Null           |
| nome               | varchar(50)| Nome do NPC                               | a-z, A-Z           | Not Null               |
| dialogo-npc        | varchar(255)| Diálogo do NPC                            | a-z, A-Z           | FK                     |

---

## Entidade: Aliado

**Descrição**: A entidade Aliado guarda as informações relacionadas aos personagens não-jogáveis que auxiliam o jogador, incluindo número de identificação, cenário, nome, diálogos e itens de recompensa.

**Observação**: Esta tabela herda de `NPC` e possui chaves estrangeiras das entidades `Item`. A `id-aliado` é uma FK referenciando `id-npc`.

| Nome Variável      | Tipo       | Descrição                                 | Valores Permitidos | Restrições de Domínio |
|--------------------|------------|-------------------------------------------|--------------------|------------------------|
| id-aliado          | int        | Código de identificação do aliado           | 1-5000             | PK, FK                 |
| id-npc             | int        | Identificador do NPC                      | 1-5000             | FK, Not Null           |
| recompensa-item    | int        | Código de identificação do item de recompensa | 1-5000        | FK, Not Null           |


---

## Entidade: Monstro

**Descrição**: A entidade Monstro guarda as informações relacionadas aos personagens não-jogáveis que o jogador deve enfrentar, incluindo número de identificação, cenário, nome e pontos de vida.

**Observação**: Esta tabela herda de `NPC` e possui chaves estrangeiras das entidades `Item`. A `id-monstro` é uma FK referenciando `id-npc`.

| Nome Variável      | Tipo       | Descrição                                 | Valores Permitidos | Restrições de Domínio |
|--------------------|------------|-------------------------------------------|--------------------|------------------------|
| id-monstro         | int        | Código de identificação do monstro         | 1-5000             | PK, FK                 |
| id-npc             | int        | Identificador do NPC                      | 1-5000             | FK, Not Null           |
| vida               | int        | Quantidade de vida do monstro             | 1-1000             | Not Null, Check (1-1000)|
| item-derramado     | int        | Identificador do item que o monstro pode derramar | 1-5000     | FK                     |

---

## Entidade: Mercador

**Descrição**: A entidade Mercador guarda as informações relacionadas aos personagens não-jogáveis responsáveis por negociar itens com o jogador.

**Observação**: Esta tabela herda de `NPC` e possui chaves estrangeiras das entidades `Inventário`. A `id-mercador` é uma FK referenciando `id-npc`.

| Nome Variável      | Tipo       | Descrição                                 | Valores Permitidos | Restrições de Domínio |
|--------------------|------------|-------------------------------------------|--------------------|------------------------|
| id-mercador        | int        | Código de identificação do mercador        | 1-5000             | PK, FK                 |
| id-npc             | int        | Identificador do NPC                      | 1-5000             | FK, Not Null           |
| inventario-mercador| int        | Identificador do inventário do mercador   | 1-5000             | FK, Not Null           |

---


## Entidade: Cenário

**Descrição**: A entidade Cenário descreve as informações relacionadas aos diferentes cenários do jogo, como número de identificação, nome e a região associada.

| Nome Variável      | Tipo       | Descrição                                 | Valores Permitidos | Restrições de Domínio |
|--------------------|------------|-------------------------------------------|--------------------|------------------------|
| id-cenario         | int        | Código de identificação do cenário         | 1-5000             | PK                     |
| nome               | varchar(50)| Nome do cenário                           | a-z, A-Z           | Not Null               |
| regiao             | varchar(50)| Região associada ao cenário               | a-z, A-Z           | Not Null               |

---

## Entidade: Item

**Descrição**: A entidade Item descreve todos os itens disponíveis no jogo, como número de identificação, nome, tipo e descrição.

| Nome Variável      | Tipo       | Descrição                                 | Valores Permitidos | Restrições de Domínio |
|--------------------|------------|-------------------------------------------|--------------------|------------------------|
| id-item            | int        | Código de identificação do item            | 1-5000             | PK                     |
| nome               | varchar(50)| Nome do item                              | a-z, A-Z           | Not Null               |
| tipo-item          | varchar(20)| Tipo do item                              | Armadura, Consumível, Chave | Not Null, Enum        |
| descricao-item     | varchar(100)| Descrição do item                         | a-z, A-Z           |                        |

---

## Entidade: Chave

**Descrição**: A entidade Chave descreve itens que são usados para desbloquear áreas ou itens no jogo.

**Observação**: Esta tabela possui chave estrangeira da entidade `Item`.  A `id-chave` é uma FK referenciando `id-item`.

| Nome Variável      | Tipo       | Descrição                                 | Valores Permitidos | Restrições de Domínio |
|--------------------|------------|-------------------------------------------|--------------------|------------------------|
| id-chave           | int        | Identificador da chave                     | 1-5000             | PK, FK                 |
| id-item            | int        | Identificador do item                      | 1-5000             | FK, Not Null           |

---

## Entidade: Armadura

**Descrição**: A entidade Armadura descreve itens que fornecem proteção ao jogador.

**Observação**: Esta tabela possui chave estrangeira da entidade `Item`. A `id-armadura` é uma FK referenciando `id-item`.

| Nome Variável      | Tipo       | Descrição                                 | Valores Permitidos | Restrições de Domínio |
|--------------------|------------|-------------------------------------------|--------------------|------------------------|
| id-armadura        | int        | Identificador da armadura                 | 1-5000             | PK, FK                 |
| id-item            | int        | Identificador do item                     | 1-5000             | FK, Not Null           |
| protecao           | int        | Quantidade de proteção fornecida           | 1-1000             | Not Null, Check (1-1000) |

---

## Entidade: Consumível

**Descrição**: A entidade Consumível descreve itens que podem ser consumidos pelo jogador para obter um benefício temporário.

**Observação**: Esta tabela possui chave estrangeira da entidade `Item`. A `id-consumivel` é uma FK referenciando `id-item`.

| Nome Variável      | Tipo       | Descrição                                 | Valores Permitidos | Restrições de Domínio |
|--------------------|------------|-------------------------------------------|--------------------|------------------------|
| id-consumivel      | int        | Identificador do consumível                | 1-5000             | PK, FK                 |
| id-item            | int        | Identificador do item                     | 1-5000             | FK, Not Null           |
| efeito             | varchar(100)| Efeito do consumível                      | a-z, A-Z           | Not Null               |
| durabilidade       | int        | Quantidade de uso restante                | 1-100              | Not Null, Check (1-100) |

---

                       
## Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 21/04/2024 | Primeira versão  do DD    | [Bianca Castro](https://github.com/BiancaPatrocinio7) e [Diego Carlito](https://github.com/DiegoCarlito) | 
| `1.1`  | 21/07/2024 | Normalizando as Entidade e formatando as tabelas | [Bianca Castro](https://github.com/BiancaPatrocinio7)  |    
| `1.1.1`  | 21/07/2024 | Corrige e adiciona atributos de relacionamento | [Marcos Castilhos](https://github.com/Marcosatc147)  | 
