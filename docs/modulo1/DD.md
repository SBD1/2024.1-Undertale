# DD - Dicionário de Dados
---
Um dicionário de dados é um recurso essencial na área da ciência de dados e da informática. Ele funciona como um catálogo ou compilação de informações sobre os dados utilizados em um sistema, banco de dados, projeto de pesquisa ou qualquer contexto em que a manipulação e interpretação de dados sejam necessárias.

> O dicionário de dados contém uma série de elementos que descrevem de forma detalhada e organizada os dados utilizados, como:<br>

> **Nomes das variáveis**: São os identificadores dados a cada conjunto de dados específico. Por exemplo, em uma tabela de vendas, poderíamos ter variáveis como "ID do cliente", "Data da compra", "Valor total", etc.<br>
> **Descrições das variáveis**: Oferecem uma explicação sobre o significado e o propósito de cada variável. Por exemplo, para a variável "Valor total" na tabela de vendas, a descrição poderia indicar que se refere ao montante financeiro total de cada transação.<br>
> **Tipos de dados**: Indicam o tipo de informação que cada variável contém, como texto, número inteiro, número decimal, data, etc.<br>
> **Valores permitidos**: Especificam os valores possíveis que cada variável pode assumir. Por exemplo, uma variável tipo inteiro de 1 a 10.<br>
> **Permite valores nulos?**: Indica se a variável pode ter valores nulos ou vazios.<br>
> **É chave?**: Informa se a variável é uma chave primária ou estrangeira em um banco de dados relacional, ou se desempenha um papel crucial na estruturação e organização dos dados.<br>


## Entidade: Jogador

**Descrição**: A entidade Jogador descreve as informações ligadas ao personável jogável, como: seu número de identificação, o local onde está, a região onde está, a estação atual do seu jogo, a missão que está fazendo, seu nome, seu nível de saúde e energia, o dia em que está e a quantidade de ouro que tem.

**Observação**: Essa tabela possui chaves estrangeiras das entidades `Cenário`, `Iventário`,`Item`, `Diálogo` e `Missão`.

| Nome Variável |    Tipo     |             Descrição              | Valores permitidos | Permite valores nulos? | É chave? | 
| :-----------: | :---------: | :--------------------------------: | :----------------: | :--------------------: | :------: | 
|  id-jogador   |     int     | Código de identificação do jogador |       1-5000       |          não           |    PK    |                   
|     nome      | varchar[50] |          Nome do jogador           |      a-z, A-Z      |          não           |          |                   
| item-equipado |      int    |   Itdentificador do equipado       |      1-5000        |          sim           |    FK    |                   
| inventario-jogador |      int    |   Itdentificador do inventário |      1-5000      |         não     |    FK    |                   
|  dialogo-jogador  |     int  |      Identificador do diálogo     |       1-5000       |          sim           |    FK    |                   
| cenario-atual |     int     |   Identificador do cenario-atual   |       1-5000       |          não           |    FK    |                   
| missao-atual  |     int     |   Identificador da missao-atual    |       1-5000       |          sim           |    FK    | 
| afinidade     |     int     |   Identificador da afinidade       |       1-5000       |          sim           |    FK    |                    
|    nivel     |     int     |          Nível do jogador          |       1-100        |          não           |          |                   
|    qtd-xp    |     int     | Quantidade de experiência do jogador  |       1-100        |          não           |          |                   
|   vida-maxima  |     int     |    Limite de vida do jogador      |       1-100        |          não           |          |                   
|   vida-atual  |     int     |    Quantidade de vida atual do jogador      |       1-100        |          não           |          |                   
|   qtd-gold  |     int     |   Quantidade de ouro do jogador    |       min. 0       |          sim           |          |                   


## Entidade: Missão
**Descrição**: A entidade Missão relaciona o número de identificação da missão, seu nome e sua descrição.

| Nome Variável |     Tipo     |             Descrição              | Valores permitidos | Permite valores nulos? | É chave? |
| :-----------: | :----------: | :--------------------------------: | :----------------: | :--------------------: | :------: |
|   id-missao   |     int      | Código de identificação da missão  |       1-5000       |          não           |    PK    |                   |
|     nome      | varchar[50]  |           Nome da missão           |      a-z, A-Z      |          não           |          |                   |
|   descricao-missao   | varchar[150] |        Descrição da missão         |      a-z, A-Z      |          sim           |          |                   |


## Entidade: Inventário

**Descrição**: A entidade Inventário relaciona o número de identificação do inventário, os seus itens e a quantidade de itens disponíveis no inventário.

**Observação**: Essa tabela possui chave estrangeira da entidade `Item`.

| Nome Variável | Tipo |        Descrição         | Valores permitidos | Permite valores nulos? | É chave? |
| :-----------: | :--: | :----------------------: | :----------------: | :--------------------: | :------: |
|    id-inventario    | int  | Identificador do inventário |       1-5000       |          não           |    PK    |                   |
|     id-item      | int  |  Identificador do item   |       1-5000       |          não           |    FK    |                   |
|     qtd-item      | int  |    Quantidade do item    |       1-5000       |          não           |          |                   |


## Entidade: Diálogo

**Descrição**: A entidade Diálogo relaciona o número de identificação do diálogo e o texto do diálogo.

| Nome Variável | Tipo |        Descrição         | Valores permitidos | Permite valores nulos? | É chave? |
| :-----------: | :--: | :----------------------: | :----------------: | :--------------------: | :------: |
|    id-dialogo    | int  | Identificador do diálogo |       1-5000       |          não           |    PK    |                   |
|     texto-dialogo      | varchar[255]  |  Texto do diálogo   |       a-z, A-Z       |          não           |        |                   |


## Entidade: NPC

**Descrição**: A entidade NPC guarda as informações relacionada aos personagens não-jogáveis, tais como: seu número de identificação, o cenário em que está, seu nome e seus diálogos.

**Observação**: Essa tabela possui chaves estrangeiras das entidades `Cenário` e `Diálogo`.

| Nome Variável |     Tipo     |                Descrição                | Valores permitidos | Permite valores nulos? | É chave? |
| :-----------: | :----------: | :-------------------------------------: | :----------------: | :--------------------: | :------: |
|    id-npc     |     int      |     Código de identificação do npc      |       1-5000       |          não           |    PK    |                   |
|     id-cenario     |     int      | Identificador do cenário onde o NPC está  |       1-5000       |          não           |    FK    |                   |
|     nome      | varchar[50]  |               Nome do npc               |      a-z, A-Z      |          não           |          |                   |
|   dialogo-npc   | varchar[255] |            Diálogo do npc             |      a-z, A-Z      |          não           |     FK     |                   |


## Entidade: Mercador

**Descrição**: A entidade Mercador guarda as informações relacionada aos personagens não-jogáveis responsáveis por negociar itens com o jogador, tais como: seu número de identificação, o cenário em que está, seu nome, seus diálogos e o seu inventário.

**Observação**: Essa tabela possui chaves estrangeiras das entidades `NPC`, `Cenário`, `Diálogo` e `Inventário`.

| Nome Variável |     Tipo     |                Descrição                | Valores permitidos | Permite valores nulos? | É chave? |
| :-----------: | :----------: | :-------------------------------------: | :----------------: | :--------------------: | :------: |
|    id-mercador     |     int      |     Código de identificação do mercador      |       1-5000       |          não           |    FK    |                   |
|     id-cenario     |     int      | Identificador do cenário onde o mercador está  |       1-5000       |          não           |    FK    |                   |
|     nome      | varchar[50]  |               Nome do mercador               |      a-z, A-Z      |          não           |          |                   |
|   dialogo-npc   | varchar[255] |            Diálogo do mercador             |      a-z, A-Z      |          não           |     FK     |                   |
|    inventario-mercador     |     int      |     Código de identificação do inventário do mercador      |       1       |          não           |    FK    |                   |


## Entidade: Aliado

**Descrição**: A entidade Aliado guarda as informações relacionada aos personagens não-jogáveis que auxiliam o jogador, tais como: seu número de identificação, o cenário em que está, seu nome, seus diálogos e os itens que o jogador recebe como recompensa.

**Observação**: Essa tabela possui chaves estrangeiras das entidades `NPC`, `Cenário`, `Diálogo` e `Item`.

| Nome Variável |     Tipo     |                Descrição                | Valores permitidos | Permite valores nulos? | É chave? |
| :-----------: | :----------: | :-------------------------------------: | :----------------: | :--------------------: | :------: |
|    id-aliado     |     int      |     Código de identificação do aliado      |       1-5000       |          não           |    FK    |                   |
|     id-cenario     |     int      | Identificador do cenário onde o aliado está  |       1-5000       |          não           |    FK    |                   |
|     nome      | varchar[50]  |               Nome do aliado               |      a-z, A-Z      |          não           |          |                   |
|   dialogo-npc   | varchar[255] |            Diálogo do aliado             |      a-z, A-Z      |          não           |     FK     |                   |
|    recompensa-item     |     int      |     Código de identificação do item de recompensa      |       1-5000       |          não           |    FK    |                   |


## Entidade: Monstro

**Descrição**: A entidade Monstro guarda as informações relacionada aos personagens não-jogáveis que batalham com o jogador, tais como: seu número de identificação, o cenário em que está, seu nome, seus diálogos, dano de ataque, quantidade de gold e a quantidade de xp.

**Observação**: Essa tabela possui chaves estrangeiras das entidades `NPC`, `Cenário` e `Diálogo`.

| Nome Variável |     Tipo     |                Descrição                | Valores permitidos | Permite valores nulos? | É chave? |
| :-----------: | :----------: | :-------------------------------------: | :----------------: | :--------------------: | :------: |
|    id-monstro     |     int      |     Código de identificação do monstro      |       1-5000       |          não           |    FK    |                   |
|     id-cenario     |     int      | Identificador do cenário onde o monstro está  |       1-5000       |          não           |    FK    |                   |
|     nome      | varchar[50]  |               Nome do monstro               |      a-z, A-Z      |          não           |          |                   |
|   dialogo-npc   | varchar[255] |            Diálogo do monstro             |      a-z, A-Z      |          não           |     FK     |                   |
|   dano-ataque  |     int     |   Quantidade de dano do monstro    |       1-25       |          não           |          |
|   recompensa-gold  |     int     |   Quantidade de ouro do monstro    |       1-100       |          não           |          |
|   recompensa-xp  |     int     |   Quantidade de xp do monstro    |       1-100       |          não           |          |


## Entidade: Item

**Descrição**: A entidade Item armazena as informações de identificação do item, nome, descrição e valor.

| Nome Variável |    Tipo     |            Descrição            | Valores permitidos | Permite valores nulos? | É chave? |
| :-----------: | :---------: | :-----------------------------: | :----------------: | :--------------------: | :------: |
|    id-item    |     int     | Código de Identificação do item |       1-5000       |          não           |    PK    |                   |
|     nome      | varchar[50]  |           Nome do item           |      a-z, A-Z      |          não           |          |
|   descricao-item   | varchar[150] |        Descrição do item         |      a-z, A-Z      |          sim           |          |                   |
|   valor-item  |     int     |   Valor em gold do item    |       1-100       |          não           |          |


## Entidade: Armadura

**Descrição**: A entidade Armadura é um item que pode ser equipado pelo jogador e armazena as informações de identificação da armadura, nome, descrição, valor e defesa.

**Observação**: Essa tabela possui chave estrangeira da entidade `Item`.

| Nome Variável |    Tipo     |            Descrição            | Valores permitidos | Permite valores nulos? | É chave? |
| :-----------: | :---------: | :-----------------------------: | :----------------: | :--------------------: | :------: |
|    id-armadura    |     int     | Código de Identificação da armadura |       1-5000       |          não           |    FK    |                   |
|     nome      | varchar[50]  |           Nome da armadura           |      a-z, A-Z      |          não           |          |
|   descricao-item   | varchar[150] |        Descrição da armadura         |      a-z, A-Z      |          sim           |          |                   |
|   valor-item  |     int     |   Valor em gold da armadura    |       1-100       |          não           |          |
|   qtd-defesa  |     int     |   Quantidade de defesa da armadura    |       1-20       |          não           |          |


## Entidade: Consumível

**Descrição**: A entidade Consumível é um item que pode ser consumido pelo jogador e armazena as informações de identificação do consumível, nome, descrição, valor e quantidade de cura.

**Observação**: Essa tabela possui chave estrangeira da entidade `Item`.

| Nome Variável |    Tipo     |            Descrição            | Valores permitidos | Permite valores nulos? | É chave? |
| :-----------: | :---------: | :-----------------------------: | :----------------: | :--------------------: | :------: |
|    id-consumivel    |     int     | Código de Identificação do consumível |       1-5000       |          não           |    FK    |                   |
|     nome      | varchar[50]  |           Nome do consumível          |      a-z, A-Z      |          não           |          |
|   descricao-item   | varchar[150] |        Descrição do consumível         |      a-z, A-Z      |          sim           |          |                   |
|   valor-item  |     int     |   Valor em gold do consumível    |       1-100       |          não           |          |
|   qtd-cura  |     int     |   Quantidade de pontos de vida recuperados    |       1-25       |          não           |          |


## Entidade: Chave

**Descrição**: A entidade Chave é um item que pode ser usado pelo jogador para acessar outros cenários e armazena as informações de identificação da chave, nome, descrição, valor e cenário de destino.

**Observação**: Essa tabela possui chaves estrangeiras das entidades `Item` e `Cenário`.

| Nome Variável |    Tipo     |            Descrição            | Valores permitidos | Permite valores nulos? | É chave? |
| :-----------: | :---------: | :-----------------------------: | :----------------: | :--------------------: | :------: |
|    id-chave    |     int     | Código de Identificação da chave |       1-5000       |          não           |    FK    |                   |
|     nome      | varchar[50]  |           Nome da chave          |      a-z, A-Z      |          não           |          |
|   descricao-item   | varchar[150] |        Descrição da chave         |      a-z, A-Z      |          sim           |          |                   |
|   valor-item  |     int     |   Valor em gold da chave    |       1-100       |          não           |          |
|    cenario-destino    |     int     | Código de Identificação do cenário de destino |       1-5000       |          não           |    FK    |


## Entidade: Cenário

**Descrição**: Descreve os cenários disponíveis no jogo, o identificador do cenário, seu nome, tipo e a descrição do cenário.

**Observação**: A entidade Cenário relaciona o número de identificação do Cenário, a descição, nome e o tipo  do Cenário.

| Nome Variável |     Tipo     |                  Descrição                  | Valores permitidos | Permite valores nulos? | É chave? |
| :-----------: | :----------: | :-----------------------------------------: | :----------------: | :--------------------: | :------: |
|  id-cenario   |     int      |          Identificador do cenário           |       1-5000       |          não           |    PK    |                   |
|     nome      | varchar[50]  |               Nome do cenário              |      a-z, A-Z      |          não           |          |                   |
|    tipo       |  int         | Tipo de cenário                             |       1-5000       |          não           |        |                   |
|   descricao-cenario   | varchar[150] |            Descrição do cenário             |      a-z, A-Z      |          sim           |          |                   |


## Entidade: Afinidade

**Descrição**: A entidade Afinidade representa o grau de afinidade do jogador com um personagem não-jogável e armazena as informações de identificação da relação, quatidade atual de afinidade e quantidade máxima de afinidade.

| Nome Variável |     Tipo     |                  Descrição                  | Valores permitidos | Permite valores nulos? | É chave? |
| :-----------: | :----------: | :-----------------------------------------: | :----------------: | :--------------------: | :------: |
|  id-afinidade   |     int      |          Identificador da relação de afinidade           |       1-5000       |          não           |    PK    |                   |
|    afinidade-atual      |  int         | Quantidade atual de afinidade                             |       1-10       |          não           |        |                   |
|    afinidade-maxima      |  int         | Quantidade máxima de afinidade                             |       10       |          não           |        |                   |

## Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 21/04/2024 | Primeira versão  do DD    | [Bianca Castro](https://github.com/BiancaPatrocinio7) e [Diego Carlito](https://github.com/DiegoCarlito) |                                                              
