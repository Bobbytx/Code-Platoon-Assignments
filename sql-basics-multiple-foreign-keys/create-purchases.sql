DROP TABLE IF EXISTS purchases;

CREATE TABLE purchases (
    id SERIAL PRIMARY KEY,
    quantity INTEGER,
    customer_id INTEGER REFERENCES customers(id),
    item_id INTEGER REFERENCES items(id)
);