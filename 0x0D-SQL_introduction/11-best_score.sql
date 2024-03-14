-- list records above 10  in second_table
-- results should be in descending order and include score and name
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
