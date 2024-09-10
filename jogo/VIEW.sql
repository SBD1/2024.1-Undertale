CREATE VIEW itens_em_sala AS
SELECT
    s.nome_sala,
    i.nome AS item_nome,
    b.capacidade
FROM
    Sala s
    LEFT JOIN Bau b ON s.id_sala = b.sala
    LEFT JOIN Item i ON b.item = i.id_item;
    
CREATE VIEW status_missoes AS
SELECT
    nome,
    descricao,
    status
FROM
    Missao;

CREATE VIEW jogadores_afinidade AS
SELECT
    j.nome AS jogador_nome,
    a.qtd_atual AS afinidade_atual,
    a.qtd_max AS afinidade_max
FROM
    Jogador j
    JOIN Afinidade a ON j.afinidade = a.id_afinidade;