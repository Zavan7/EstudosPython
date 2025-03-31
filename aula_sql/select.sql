-- where filtra registros
-- Operadores de comparação: + < <= > >= <> !=
-- Operadores lógicos and e or
-- Between seleciona um range
-- In seleciona elementos entre os valores enviados
-- Like (Parecido) ('%' = Qualquer coisa), ('_' = Um carctere)
-- Order ordena o select
-- Limit (Limita valores) & Offset (Partindo de um ponto determinado).
-- Limit Offset, da para escrever 'limit 2,4',
-- Porém nesse caso o offset vem primeiro

select * from Users u
WHERE id=2
or First_name = "Vitor";

select * from Users u
WHERE id=2
and Last_name = "Zavan";

select * from Users u
WHERE 
Create_at >= '2020-01-21 08:24:40'
and
Create_at <= '2020-02-22 22:36:48';

-- Between
select * from Users u
WHERE Create_at between '2020-01-21 00:00:00'
and
'2020-02-22 23:59:59';

select * from Users u
WHERE Id between 32 and 59;

-- In
select * from Users u
where Id in (5, 10, 15, 20);

-- Like
select * from Users u
WHERE First_name like '%mo%';

select * from Users u
WHERE First_name like '%a%b%';

select * from Users u
WHERE First_name like 'Isab__le';

-- Order
select Id, First_name, Email from Users u
WHERE Id between 32 and 59
order by id asc, u.First_name desc;

-- Limit
select Id, First_name, Email from Users u
WHERE Id between 32 and 59
limit 5 offset 5;

SELECT u.Id as uid, p.Id as pid,
p.Bio as pbio, u.First_name as uname
from Users as u, Profiles as p
where u.Id = p.User_id;

-- Select multiplas planilhas
SELECT
u.Id as userId, u.First_name as user_FN, p.Bio as Prof_bio, r.Name as Role_name
FROM Users u
LEFT JOIN
Profiles p ON u.Id = p.User_id
INNER JOIN Users_roles ur ON u.Id = ur.Users_id
INNER JOIN Roles r ON ur.Roles_id = r.Id
ORDER BY  userId ASC;