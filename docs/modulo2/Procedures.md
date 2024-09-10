
# Trigger
## Introdução

Uma **Stored Procedure** é um conjunto de comandos SQL armazenado no banco de dados, que pode ser executado sob demanda pelo SGBD ou por aplicações conectadas a ele. Elas são amplamente utilizadas para automatizar tarefas complexas, melhorar a performance e reduzir o tráfego de rede, executando operações diretamente no servidor. Stored Procedures são úteis para criar rotinas de processamento, realizar tarefas agendadas e garantir consistência ao encapsular a lógica de negócios no banco de dados. São ideais quando múltiplas aplicações, escritas em linguagens diferentes, precisam executar a mesma função de forma centralizada.
#### Consulta de Dados

```sql

CREATE OR REPLACE PROCEDURE listar_jogadores_e_itens()
LANGUAGE plpgsql
AS $$
BEGIN
    PERFORM j.nome AS jogador_nome, i.nome AS item_nome
    FROM Jogador j
    LEFT JOIN Item i ON j.item_equipado = i.id_item;
END;
$$;


CREATE OR REPLACE PROCEDURE mover_jogador(
    p_id_jogador INT,
    p_id_sala_destino INT
)
LANGUAGE plpgsql
AS $$
DECLARE
    v_id_sala_origem INT;
    v_conexao_existe BOOLEAN;
BEGIN
    SELECT sala_atual INTO v_id_sala_origem
    FROM Jogador
    WHERE id_jogador = p_id_jogador;

    SELECT EXISTS(
        SELECT 1 FROM Conexao
        JOIN Porta ON Conexao.porta = Porta.id_porta
        WHERE id_sala_origem = v_id_sala_origem
        AND id_sala_destino = p_id_sala_destino
        AND Porta.status = 'Aberta'
    ) INTO v_conexao_existe;

    IF NOT v_conexao_existe THEN
        RAISE EXCEPTION 'Movimento inválido: a conexão entre as salas não existe ou está fechada.';
    END IF;

    UPDATE Jogador
    SET sala_atual = p_id_sala_destino
    WHERE id_jogador = p_id_jogador;

END;
$$;

CREATE OR REPLACE PROCEDURE atualizar_porta_status(id_missao INT, id_conexao INT)
AS $$
BEGIN

    UPDATE Porta
    SET status = 'Aberta'
    WHERE id_porta = (SELECT porta FROM Conexao WHERE id_conexao = porta)
    AND EXISTS (
        SELECT 1 FROM Missao
        WHERE id_missao = id_missao
        AND status = 'concluída'
    );
END;
$$ LANGUAGE plpgsql;




```

### Histórico de Versão
| Versão | Data | Descrição | Autor(es) |
| :-: | :-: | :-: | :-: | 
| `1.0`  | 08/09/2024 | Criação do documento  | [Marcos Castilhos](https://github.com/Marcosatc147) e [Bianca Castro](https://github.com/BiancaPatrocinio7) |   