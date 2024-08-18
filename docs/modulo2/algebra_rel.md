# Algebra Relacional

## Introdução

DQL é a sigla para Data Query Language. É uma linguagem de consulta de dados que permite aos usuários recuperar dados de um banco de dados. O DQL é usado para consultar os dados armazenados em um banco de dados, como recuperar informações específicas de uma tabela ou visualização. O DQL é uma parte importante do projeto físico do banco de dados, pois permite recuperar os dados armazenados no banco de dados.

### Consultas

Algumas consultas realizadas no projeto:

#### Consultar nome de todos jogadores
```
π_nome(Jogador)

```
---
### Consultar todas missões ativas
```
σ(status = 'ativa')(Missao)

```
---
### Consultar todos os NPCs em uma sala específica
```
σ(sala = 1)(NPC)
```
---
### Consultar todas as conexões entre salas
```
ρ(Conexao)
```
---
### Consultar todos os aliados e suas características
```
ρ(Aliado)
```
---
### Consultar todos os monstros e seus itens de drop

```
Monstro ⨝ Monstro.item_drop = Item.id_item Item
```
---

<center>

### Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 18/08/2024 | Criação do documento  | [Marcos Castilhos](https://github.com/Marcosatc147) |
  
</center>

---