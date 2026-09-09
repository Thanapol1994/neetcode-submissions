-- Write your query below
WITH total_order AS (
    SELECT
        customer_id,
        COUNT(id) AS total_order_per_customer
    FROM orders
    GROUP BY customer_id
)

SELECT c.name
FROM customers c
LEFT JOIN total_order t
    ON c.id = t.customer_id
WHERE t.total_order_per_customer IS NULL;