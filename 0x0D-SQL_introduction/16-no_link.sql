-- display all records from second_table where name is not null
-- records should show score and name and ordered by score in descending order
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
