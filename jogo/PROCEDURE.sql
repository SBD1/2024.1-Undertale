
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
    -- Obter a sala atual do jogador
    SELECT sala_atual INTO v_id_sala_origem
    FROM Jogador
    WHERE id_jogador = p_id_jogador;

    -- Verificar se a conexão entre as salas existe
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

    -- Atualizar a sala atual do jogador
    UPDATE Jogador
    SET sala_atual = p_id_sala_destino
    WHERE id_jogador = p_id_jogador;

    -- Lógica adicional, como triggers ou eventos, pode ser adicionada aqui
END;
$$;

CREATE OR REPLACE PROCEDURE atualizar_porta_status(id_missao INT, id_conexao INT)
AS $$
BEGIN
    -- Atualiza o status da porta para 'Aberta' quando a missão está concluída
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
