-- Update atualiza valores expecificados (Use sempre o WHERE)

UPDATE Users set First_name = 'Californiano', Last_name  = 'Da Leste'
where Id = 20;

SELECT * from Users where Id = 20;

-- Upgrade & Join
select u.first_name, p.bio from Users u
join Profiles as p
on p.user_id = u.id
where u.first_name = 'Katelyn';

update Users as u
join Profiles as p
on p.user_id = u.id
set p.bio =  CONCAT(p.bio, ' atualizado') 
where u.first_name = 'Katelyn';