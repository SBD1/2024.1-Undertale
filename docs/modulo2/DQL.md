
# Data Query Language (DQL)
## Introdução

DQL é a sigla para Data Query Language. É uma linguagem de consulta de dados que permite aos usuários recuperar dados de um banco de dados. O DQL é usado para consultar os dados armazenados em um banco de dados, como recuperar informações específicas de uma tabela ou visualização. O DQL é uma parte importante do projeto físico do banco de dados, pois permite recuperar os dados armazenados no banco de dados.

#### Consulta de Dados

1. **Criar banco de dados:**
   ```sql
   CREATE DATABASE {dbname};
   ```

2. **Inserir afinidade:**
   ```sql
   INSERT INTO Afinidade (qtd_atual, qtd_max) VALUES (%s, %s) RETURNING id_afinidade;
   ```

3. **Inserir jogador:**
   ```sql
   INSERT INTO Jogador (nome, nivel, qtd_xp, vida_maxima, vida_atual, afinidade, tipo_rota, sala_atual, viu_introducao) 
   VALUES (%s, %s, %s, %s, %s, %s, %s, %s, FALSE);
   ```

4. **Selecionar jogadores registrados:**
   ```sql
   SELECT nome FROM Jogador;
   ```

5. **Selecionar diálogo por ID:**
   ```sql
   SELECT texto FROM Dialogo WHERE id_dialogo = %s;
   ```

6. **Selecionar escolhas para um diálogo:**
   ```sql
   SELECT escolha_id, escolha, prox_dialogo FROM EscolhaDialogo WHERE id_dialogo = %s;
   ```

7. **Mover jogador:**
   ```sql
   CALL mover_jogador(%s, %s);
   ```

8. **Selecionar conexões disponíveis:**
   ```sql
   SELECT id_sala_destino, direcao, descricao_conexao 
   FROM Conexao 
   WHERE id_sala_origem = (SELECT sala_atual FROM Jogador WHERE id_jogador = %s);
   ```

9. **Selecionar status do jogador:**
   ```sql
   SELECT Jogador.nome, Jogador.nivel, Jogador.qtd_xp, Jogador.vida_atual, Jogador.vida_maxima, Jogador.afinidade, Jogador.tipo_rota, Sala.nome_sala
   FROM Jogador
   JOIN Sala ON Sala.id_sala = Jogador.sala_atual
   WHERE id_jogador = %s;
   ```

10. **Selecionar se o jogador viu introdução:**
    ```sql
    SELECT viu_introducao FROM Jogador WHERE id_jogador = %s;
    ```

11. **Marcar introdução como vista:**
    ```sql
    UPDATE Jogador SET viu_introducao = TRUE WHERE id_jogador = %s;
    ```

12. **Criar interação com Flowey:**
    ```sql
    INSERT INTO Interacao (npc, jogador, dialogo) VALUES ('Flowey', %s, 2);
    ```

13. **Criar interação com Toriel:**
    ```sql
    INSERT INTO Interacao (npc, jogador, dialogo) VALUES ('Toriel', %s, 7);
    ```

14. **Atualizar status da porta:**
    ```sql
    CALL atualizar_porta_status(%s, %s);
    ```

15. **Atualizar status da missão:**
    ```sql
    UPDATE Missao SET status = TRUE WHERE id_missao = %s;

    
    ```

### Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 18/08/2024 | Criação do documento  | [Marcos Castilhos](https://github.com/Marcosatc147) e [Bianca Castro](https://github.com/BiancaPatrocinio7) |   