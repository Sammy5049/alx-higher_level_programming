-- Show all number of records with the same score second_table.
-- Recorded in descending count.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;