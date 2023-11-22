DROP TABLE IF EXISTS items;

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    item_name VARCHAR(100),
    cost INTEGER
);