SELECT 
    vd.nmvdd AS vendedor,
    SUM(v.qtd * v.vrunt) AS valor_total_vendas,
    ROUND(SUM(v.qtd * v.vrunt) * vd.perccomissao / 100, 2) AS comissao
FROM tbvendas v
JOIN tbvendedor vd ON v.cdvdd = vd.cdvdd
WHERE v.status = 'Concluído'
GROUP BY vd.nmvdd
ORDER BY comissao DESC;

-- A obtenção do valor total de vendas e a comissão do vendedor foi calculado conforme descrito abaixo:
-- Valor total de vendas é igual: 
--      somatório da quantidade vendida do produto * o valor unitário do produto.
--   Comissão de um vendedor é igual:
--      Valor total de vendas * percentual da comissão do vendedor / 100, arredondado a duas casas decimais.
-- O valor total de vendas e a comissão foram agrupados pelo nome do vendedor.
-- Foram selecionadas somente as vendas com o estado concluído e os dados ordenados em ordem descendente de comissão de 
-- vendedor. 