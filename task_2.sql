-- Advanced Data Management - D326

-- User-defined function used to convert TIMESTAMP.

CREATE OR REPLACE FUNCTION month_year_from_timestamp (rental_date TIMESTAMP)
RETURNS TEXT
LANGUAGE plpgsql
AS
$$
DECLARE 
  rental_month_year TEXT;
BEGIN
  rental_month_year := TO_CHAR(rental_date, 'Month YYYY');
  RETURN rental_month_year;
END;
$$;


-- Testing the TIMESTAMP function; will return 'MAY 2007'

SELECT month_year_from_timestamp('2007-05-20');


--  Create a detailed table

CREATE TABLE detailed_categories (
  rental_id INT,
  store_id INT,
  category_id INT,
  category_name VARCHAR(50),
  payment_date VARCHAR(25),
  payment_amount numeric(7,2)
);


--  Create a summary table

CREATE TABLE summary_categories (
  store_id INT,
  payment_month VARCHAR(25),
  category_id INT,
  category_name VARCHAR(50),
  total_revenue numeric(10,2)
);

--  Verify (empty) tables were created

SELECT * FROM summary_categories;
SELECT * FROM detailed_categories;


-- Create a trigger function (and trigger)

CREATE OR REPLACE FUNCTION summary_update_function()
  RETURNS TRIGGER 
  LANGUAGE plpgsql 
AS
$$
BEGIN
DELETE FROM summary_categories;

WITH ranked_categories AS (
  SELECT
    store_id,
    payment_date AS payment_month,
    category_id,
    category_name,
    SUM(payment_amount) AS total_revenue,
    ROW_NUMBER() OVER (PARTITION BY store_id, payment_date ORDER BY SUM(payment_amount) DESC) AS rank
  FROM detailed_categories
  GROUP BY store_id, payment_date, category_id, category_name
)
INSERT INTO summary_categories (store_id, payment_month, category_id, category_name, total_revenue)
SELECT store_id, payment_month, category_id, category_name, total_revenue
FROM ranked_categories
WHERE rank <= 3;

RETURN NEW;
END;
$$;

CREATE OR REPLACE TRIGGER summary_update_trigger
AFTER INSERT
ON detailed_categories
FOR EACH STATEMENT
EXECUTE PROCEDURE summary_update_function();





-- Inserting date into detailed table - This will populate the summary table with data

INSERT INTO detailed_categories (rental_id, store_id, category_id, category_name, payment_date, payment_amount)
SELECT
  p.rental_id,
  s.store_id,
  c.category_id,
  c.name AS category_name,
  month_year_from_timestamp(p.payment_date) AS payment_date,
  p.amount
FROM payment p
JOIN rental r ON p.rental_id = r.rental_id
JOIN inventory i ON r.inventory_id = i.inventory_id
JOIN film_category fc ON i.film_id = fc.film_id
JOIN category c ON fc.category_id = c.category_id
JOIN staff s ON r.staff_id = s.staff_id
ORDER BY s.store_id, payment_date, p.amount;


-- Verify data was added into both tables


SELECT * FROM detailed_categories ORDER BY 2,3 ASC; -- 14596 rows.
SELECT * FROM summary_categories; -- 24 rows.


-- Add additional row to detailed table


INSERT INTO detailed_categories (rental_id, store_id, category_id, category_name, payment_date, payment_amount)
VALUES (100, 1, 5, 'Action', 'June 2023', 10.00);


-- Verify additional data was added to both tables


SELECT * FROM detailed_categories ORDER BY 2,3 ASC; -- 14597 rows.
SELECT * FROM summary_categories; -- 25 rows.


-- Create a precedure to refresh tables


CREATE OR REPLACE PROCEDURE table_refresh_procedure()
LANGUAGE plpgsql
AS $$
BEGIN
  DELETE FROM detailed_categories;
  DELETE FROM summary_categories;

  INSERT INTO detailed_categories (rental_id, store_id, category_id, category_name, payment_date, payment_amount)
  SELECT
    p.rental_id,
    s.store_id,
    c.category_id,
    c.name AS category_name,
    month_year_from_timestamp(p.payment_date),
    p.amount
  FROM payment p
  JOIN rental r ON p.rental_id = r.rental_id
  JOIN inventory i ON r.inventory_id = i.inventory_id
  JOIN film_category fc ON i.film_id = fc.film_id
  JOIN category c ON fc.category_id = c.category_id
  JOIN staff s ON r.staff_id = s.staff_id
  ORDER BY s.store_id, month_year_from_timestamp(p.payment_date), p.amount;

  RETURN;
END;
$$;


-- Call the table refresh procedure

CALL table_refresh_procedure();


-- Confirm tables have been refreshed

SELECT * FROM detailed_categories ORDER BY store_id, payment_date ASC;
SELECT * FROM summary_categories;
