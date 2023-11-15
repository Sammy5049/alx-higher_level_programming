-- Show all number of records with the same score second_table.
-- Recorded in descending count.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC