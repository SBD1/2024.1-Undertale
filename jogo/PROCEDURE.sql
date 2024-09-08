-- Chamada da procedure
--CALL atualizar_item_equipado(1, 2);

CREATE OR REPLACE PROCEDURE adicionar_item_sala(
    p_id_sala INT,
    p_id_item INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    INSERT INTO Bau (sala, item)
    VALUES (p_id_sala, p_id_item);
END;
$$;

-- Chamada da procedure
CALL adicionar_item_sala(1, 3);

CREATE OR REPLACE PROCEDURE listar_jogadores_e_itens()
LANGUAGE plpgsql
AS $$
BEGIN
    PERFORM j.nome AS jogador_nome, i.nome AS item_nome
    FROM Jogador j
    LEFT JOIN Item i ON j.item_equipado = i.id_item;
END;
$$;

-- Chamada da procedure
CALL listar_jogadores_e_itens();

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
        WHERE id_sala_origem = v_id_sala_origem
        AND id_sala_destino = p_id_sala_destino
        AND status = 'Aberta'
    ) INTO v_conexao_existe;

    IF NOT v_conexao_existe THEN
        RAISE EXCEPTION 'Movimento inválido: a conexão entre as salas não existe ou está fechada.';
    END IF;

    -- Atualizar a sala atual do jogador
    UPDATE Jogador
    SET sala_atual = p_id_sala_destino
    WHERE id_jogador = p_id_jogador;

    -- Adicione aqui quaisquer lógicas adicionais, como ativar triggers ou eventos

    COMMIT;
END;
$$;



