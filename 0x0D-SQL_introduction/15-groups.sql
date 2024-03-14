-- list number of records with same score from second_table
-- number of records should be added to new column with name 'number'
-- results should also display the score in descending order
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
