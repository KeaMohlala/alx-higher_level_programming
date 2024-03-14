-- create table unique_id if it doesn't exist
-- id field should have a default value of 1 and must be unique
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1,
    name VARCHAR(256),
    UNIQUE (id)
);
