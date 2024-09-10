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


-- Função para validar e instanciar um item
CREATE OR REPLACE FUNCTION valida_e_insere_item()
RETURNS TRIGGER AS $$
BEGIN
    -- Insere o item na tabela Instancia_Item e retorna o id gerado
    INSERT INTO Instancia_Item(item)
    VALUES (NEW.id_instancia);

    -- Verifica o tipo do item baseado na tabela que disparou o trigger
    IF TG_TABLE_NAME = 'Consumivel' THEN
        INSERT INTO Instancia_Item(item)
        VALUES (NEW.id_instancia);
    ELSIF TG_TABLE_NAME = 'Defesa' THEN
        INSERT INTO Instancia_Item(item)
        VALUES (NEW.id_instancia);
    ELSIF TG_TABLE_NAME = 'Ataque' THEN
        INSERT INTO Instancia_Item(item)
        VALUES (NEW.id_instancia);
    END IF;

    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


-- Triggers para validar e instanciar itens antes de inserção
-- Triggers para instanciar itens após inserção
CREATE TRIGGER trigger_valida_e_insere_item_consumivel
AFTER INSERT OR UPDATE ON Consumivel
FOR EACH ROW
EXECUTE FUNCTION valida_e_insere_item();

CREATE TRIGGER trigger_valida_e_insere_item_defesa
AFTER INSERT OR UPDATE ON Defesa
FOR EACH ROW
EXECUTE FUNCTION valida_e_insere_item();

CREATE TRIGGER trigger_valida_e_insere_item_ataque
AFTER INSERT OR UPDATE ON Ataque
FOR EACH ROW
EXECUTE FUNCTION valida_e_insere_item();

CREATE OR REPLACE FUNCTION valida_tipo_npc()
RETURNS TRIGGER AS $$
BEGIN
    IF (TG_TABLE_NAME = 'Mercador' AND NEW.tipo != 'Mercador') THEN
        RAISE EXCEPTION 'O tipo de NPC deve ser Mercador para a tabela Mercador';
    ELSIF (TG_TABLE_NAME = 'Aliado' AND NEW.tipo != 'Aliado') THEN
        RAISE EXCEPTION 'O tipo de NPC deve ser Aliado para a tabela Aliado';
    ELSIF (TG_TABLE_NAME = 'Monstro' AND NEW.tipo != 'Monstro') THEN
        RAISE EXCEPTION 'O tipo de NPC deve ser Monstro para a tabela Monstro';
    END IF;
    
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;


