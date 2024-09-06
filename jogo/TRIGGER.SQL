CREATE OR REPLACE FUNCTION atualizar_afinidade_jogador()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE Afinidade
    SET qtd_atual = qtd_atual + 1
    WHERE id_afinidade = NEW.afinidade;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_atualizar_afinidade_jogador
AFTER INSERT ON Jogador
FOR EACH ROW
EXECUTE FUNCTION atualizar_afinidade_jogador();


CREATE OR REPLACE FUNCTION verificar_capacidade_bau()
RETURNS TRIGGER AS $$
BEGIN
    IF (SELECT COUNT(*) FROM Bau WHERE sala = NEW.sala) >= (SELECT capacidade FROM Bau WHERE id_bau = NEW.id_bau) THEN
        RAISE EXCEPTION 'Capacidade do baú excedida.';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_verificar_capacidade_bau
BEFORE INSERT ON Bau
FOR EACH ROW
EXECUTE FUNCTION verificar_capacidade_bau();


CREATE OR REPLACE FUNCTION atualizar_status_porta()
RETURNS TRIGGER AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM Bau WHERE sala = OLD.sala) THEN
        UPDATE Porta
        SET status = 'Fechada'
        WHERE sala = OLD.sala;
    END IF;
    RETURN OLD;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_atualizar_status_porta
AFTER DELETE ON Bau
FOR EACH ROW
EXECUTE FUNCTION atualizar_status_porta();

CREATE OR REPLACE PROCEDURE atualizar_item_equipado(
    p_id_jogador INT,
    p_id_item INT
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM Item WHERE id_item = p_id_item) THEN
        UPDATE Jogador
        SET item_equipado = p_id_item
        WHERE id_jogador = p_id_jogador;
    ELSE
        RAISE EXCEPTION 'Item com id "%" não existe.', p_id_item;
    END IF;
END;
$$;

