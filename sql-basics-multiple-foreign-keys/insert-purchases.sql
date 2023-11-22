/* Create bob's microphone purchase 
and alice's spatula purchase in one single SQL statement */
INSERT INTO purchases (customer_id, quantity, item_id)
VALUES 
(1, 1, 2),
(2, 5, 1),