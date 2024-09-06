-- Chamada da procedure
CALL atualizar_item_equipado(1, 2);

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
    SELECT j.nome AS jogador_nome, i.nome AS item_nome
    FROM Jogador j
    LEFT JOIN Item i ON j.item_equipado = i.id_item;
END;
$$;

-- Chamada da procedure
CALL listar_jogadores_e_itens();


