-- TerraOps Fusion — 5 queries demonstrativas

-- Q1: Top 3 talhões por stress
SELECT talhao_id, stress_fusion, categoria
FROM fused_scores
ORDER BY stress_fusion DESC
LIMIT 3;

-- Q2: Talhões com divergência ativa
SELECT talhao_id, stress_fusion
FROM fused_scores
WHERE divergencia_ativa = 1;

-- Q3: Média NDVI orbital
SELECT AVG(ndvi) AS media_ndvi FROM orbital_readings;

-- Q4: Umidade solo por fonte
SELECT fonte, AVG(umidade_solo) AS media_umidade
FROM ground_truth
GROUP BY fonte;

-- Q5: Contagem por categoria de risco
SELECT categoria, COUNT(*) AS total
FROM fused_scores
GROUP BY categoria;
