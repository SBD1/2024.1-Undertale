SELECT * FROM NPC;

DELETE FROM Item
WHERE id_item = 8;

DELETE FROM Afinidade
WHERE id_afinidade = 1;

-- Inserir uma nova missão
INSERT INTO Missao (nome, descricao, status)
VALUES ('Resolva o puzzle', 'Resolva o puzzle das Ruinas para liberar a porta para a outra sala', 'ativa');

-- Inserir um novo item
INSERT INTO Item (id_item, nome, descricao, valor, tipo)
VALUES (1, 'Bandana Viril', '7DF - Tem abdominais nela', 50.00, 'Defesa');

-- Inserir um novo item
INSERT INTO Item (id_item, nome, descricao, valor, tipo)
VALUES (2, 'Luva Forte', '5AT Na cara deles.', 50.00, 'Ataque');

-- Inserir um novo item
INSERT INTO Item (id_item, nome, descricao, valor, tipo)
VALUES (3, 'Maçã de Siri', 'CR18 HP (Parece um siri.)', 25.00, 'Consumível');

-- Inserir uma nova sala
INSERT INTO Sala (id_sala, nome_sala, descricao)
VALUES (0, 'Inicio', '...');

INSERT INTO Sala (id_sala, nome_sala, descricao)
VALUES (1, 'Ruinas', 'A entrada principal do mundo subterraneo');

INSERT INTO Sala (id_sala, nome_sala, descricao)
VALUES (2, 'Snowdin', 'Snowdin é um local de clima frio e está praticamente coberto com gelo e neve, bem como várias árvores em toda parte da região.');

INSERT INTO Sala (id_sala, nome_sala, descricao)
VALUES (3, 'Cachoeiras', 'Lugar misterioso protegido por uma poderosa guardiã');

-- Inserir uma nova conexão entre salas
INSERT INTO Conexao (id_sala_origem, id_sala_destino, direcao, descricao_conexao)
VALUES (1, 2, 'Norte', 'Caminho que leva ao centro das ruinas');

-- ALIADOS
--- Inserir Flowey como Aliado
INSERT INTO Aliado (nome, sala, tipo, gold_drop, xp_drop, dano_ataque)
VALUES ('Flowey', NULL, 'Aliado', 20, 10, 99);

-- Inserir Toriel como Aliado
INSERT INTO Aliado (nome, sala, tipo, gold_drop, xp_drop, dano_ataque)
VALUES ('Toriel', NULL, 'Aliado', 15, 5, 10);

-- Inserir Sans como Aliado
INSERT INTO Aliado (nome, sala, tipo, gold_drop, xp_drop, dano_ataque)
VALUES ('Sans', NULL, 'Aliado', 25, 30, 20);

-- Inserir Papyrus como Aliado
INSERT INTO Aliado (nome, sala, tipo, gold_drop, xp_drop, dano_ataque)
VALUES ('Papyrus', NULL, 'Aliado', 20, 25, 15);

-- MONSTROS
-- Inserir Napstablook como Monstro
INSERT INTO Monstro (nome, sala, tipo, dano_ataque, xp_drop, gold_drop, item_drop)
VALUES ('Napstablook', NULL, 'Monstro', 5, 5, 10, NULL);

-- Inserir Doggo como Monstro
INSERT INTO Monstro (nome, sala, tipo, dano_ataque, xp_drop, gold_drop, item_drop)
VALUES ('Doggo', NULL, 'Monstro', 12, 30, 15, NULL);

-- Inserir Dogamy e Dogaressa como Monstros
INSERT INTO Monstro (nome, sala, tipo, dano_ataque, xp_drop, gold_drop, item_drop)
VALUES ('Dogamy e Dogaressa', NULL, 'Monstro', 40, 40, 20, NULL);

-- Inserir Dogão como Monstro
INSERT INTO Monstro (nome, sala, tipo, dano_ataque, xp_drop, gold_drop, item_drop)
VALUES ('Dogão', NULL, 'Monstro', 80, 60, 50, NULL);

-- Inserir uma nova loja
INSERT INTO Loja (id_loja, nome, sala, item)
VALUES (1, 'Loja de Nevada', 1, 1);

INSERT INTO Loja (id_loja, nome, sala, item)
VALUES (2, 'Loja do Gerson', 2, 3);

-- MERCADOR
-- Inserir Lojista de Nevada como Mercador
INSERT INTO Mercador (nome, sala, tipo, loja)
VALUES ('Lojista de Nevada', 1, 'Mercador', 1);

-- Inserir Gerson como Mercador
INSERT INTO Mercador (nome, sala, tipo, loja)
VALUES ('Gerson', 2, 'Mercador', 2);


-- Inserir instâncias
INSERT INTO Instancia_item (id_instancia, item)
VALUES (1, 1);

INSERT INTO Instancia_item (id_instancia, item)
VALUES (2, 2);

INSERT INTO Instancia_item (id_instancia, item)
VALUES (3, 3);


-- Inserir uma nova defesa
INSERT INTO Defesa (id_instancia, protecao)
VALUES (1, 10);

-- Inserir um novo ataque
INSERT INTO Ataque (id_instancia, dano)
VALUES (2, 25);

-- Inserir um novo consumível
INSERT INTO Consumivel (id_instancia, qtd_cura)
VALUES (3, 20);

-- Inserir uma nova porta
INSERT INTO Porta (status, sala)
VALUES ('Fechada', 1);

-- Inserir um novo baú
INSERT INTO Bau (sala, capacidade, item)
VALUES (1, 5, 1);

-- Inserir uma nova afinidade
INSERT INTO Afinidade (qtd_atual, qtd_max)
VALUES (0, 100);

INSERT INTO Jogador (nome, item_equipado, nivel, qtd_xp, vida_maxima, vida_atual, afinidade, tipo_rota)
VALUES ('Frisk', NULL, 1, 0, 100, 100, 1, 'Pacifista');

INSERT INTO Dialogo (texto)
VALUES(
'Ha muito tempo, Humanos e Monstros conviviam juntos em harmonia sobre a Terra. 
Um dia, uma guerra se iniciou entre as duas raças e depois de um longo confronto, os humanos foram vitoriosos. 
Eles confinaram todos os monstros existentes no subterraneo do Monte Ebott com uma barreira magica.
Apenas o poder de 7 almas humanas diferentes poderia romper a barreira permanentemente.
Muito tempo depois, em 201X, uma crianca humana acabou escalando o Monte por razoes desconhecidas e, 
consequentemente, caiu no subterraneo, onde os monstros atualmente residem');

INSERT INTO Dialogo (texto) 
VALUES (
'Opa! Como vai! Eu sou FLOWEY.
FLOWEY a FLOR!

umm...

É sua primeira vez no SUBSOLO, né?
Puxa, Tudo deve parecer tão confuso.

Alguem tem que te ensinar como as coisas funcionam por aqui!
Acho que o bom e velho eu terei que cuidar disso.

Tudo pronto vamos lá!

Pise aqui!

No começo sua alma é fraca , mas com o passar do tempo ela fica forte.

Está vendo esses Mobis? Bom , Eles são ''Petalas da amizade''.

Eles te darão LV. Oque é LV? LOVE, é claro.

Eles te deixarão mais forte.

Vou compartilhar um pouco com você.

Tudo pronto, Mova-se, Pegue o máximo que puder!'
)

