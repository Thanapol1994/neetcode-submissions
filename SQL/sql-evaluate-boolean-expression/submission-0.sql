-- Write your query below
-- match variable value to the expressions table
-- compare the left and right values by using CASE

SELECT
    e.left_operand,
    e.operator,
    e.right_operand,
    CASE
        WHEN e.operator = '>' THEN v1.value > v2.value
        WHEN e.operator = '<' THEN v1.value < v2.value
        ELSE v1.value = v2.value
    END AS value
FROM expressions e
LEFT JOIN variables v1
    ON e.left_operand = v1.name
LEFT JOIN variables v2
    ON e.right_operand = v2.name;