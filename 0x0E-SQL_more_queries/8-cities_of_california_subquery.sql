-- list all cities of California found in the hbtn_0d_usa
-- JOIN keyword cannot be used
SELECT cities.id, cities.name
FROM cities
WHERE cities.state_id = (SELECT states.id FROM states WHERE states.name = 'California')
ORDER BY cities.id ASC;
