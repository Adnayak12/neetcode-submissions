-- Write your query below
SELECT P.first_name, P.last_name, COALESCE(A.city, NULL) AS city, COALESCE(A.state, NULL) AS state
FROM person AS P
LEFT JOIN
address AS A
ON P.person_id=A.person_id;