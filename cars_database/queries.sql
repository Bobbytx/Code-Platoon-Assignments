-- SELECT advertisement_date, COUNT(*) FROM Advertisement WHERE advertisement_date < '2014-02-01' GROUP BY advertisement_date ORDER BY advertisement_date DESC;

-- SELECT DATE_TRUNC('month', advertisement_date) as Trunc_date, count(advertisement_id) as post_count FROM Advertisement
-- GROUP BY Trunc_date
-- order by post_count DESC;

-- SELECT 
--     EXTRACT(YEAR FROM advertisement_date) AS Year, 
--     EXTRACT(MONTH FROM advertisement_date) AS Month, 
--     COUNT(*) AS NumberOfAdvertisements
-- FROM Advertisement
-- GROUP BY Year, Month
-- ORDER BY Year, Month;

-- SELECT first_name FROM AppUser
--  WHERE account_id IN (
--     SELECT seller_account_id 
--     FROM Advertisement
--  WHERE advertisement_date > '2014-05-31' AND advertisement_date < '2014-07-01');

-- SELECT * FROM advertisement ORDER BY advertisement_date DESC;

SELECT make FROM CarModel WHERE car_model_id IN (
    SELECT car_model_id FROM car WHERE car_id IN(
        SELECT car_id FROM Advertisement WHERE seller_account_id IN (
            SELECT account_id FROM AppUser WHERE first_name = 'Wilda' AND last_name = 'Giguere'
        )
    )
)