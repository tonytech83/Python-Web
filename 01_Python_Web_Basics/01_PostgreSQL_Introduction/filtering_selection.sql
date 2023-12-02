SELECT last_name
FROM people p
WHERE p.id = 1;

SELECT id,
       first_name,
       last_name
FROM people p
WHERE p.id > 1
  AND p.id < 3;
	