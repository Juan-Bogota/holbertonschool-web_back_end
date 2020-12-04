-- MySQl: Best band ever!
-- Script Query table user
select origin, SUM(fans) AS nb_fans from metal_bands GROUP BY origin ASC ORDER BY nb_fans DESC;
