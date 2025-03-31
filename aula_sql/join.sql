-- Inner Join = Registro que ambas as tabelas compartilham
-- Left Join = Considera os valores que estão a ESQUERDA
-- Mesmo que não haja registro na outra tabela
-- Right Join = Considera os valores que estão a DIREITA
-- Mesmo que não haja registro na outra tabela

-- Funciona como Inner Join
SELECT u.Id as uid, p.Id as pid, p.Bio as pbio, u.First_name as uname
from Users as u, Profiles as p
where u.Id = p.User_id;

-- Inner Join 
SELECT u.Id as user_id, p.Id as prof_id, p.Bio, u.First_name
FROM Users as u
INNER JOIN Profiles as p
ON u.Id = p.User_id
WHERE u.First_name  LIKE '%a'
ORDER BY u.First_name ASC
LIMIT 5;

-- Left Join (Considera os valores que estão a ESQUERDA)
SELECT u.Id as user_id, p.Id as prof_id, p.Bio, u.First_name
FROM Users as u
LEFT JOIN Profiles as p
ON u.Id = p.User_id;

-- Right Join (Considera os valores que estão a DIREITA)
SELECT u.Id as user_id, p.Id as prof_id, p.Bio, u.First_name
FROM Users as u
RIGHT JOIN Profiles as p
ON u.Id = p.User_id;