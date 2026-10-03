-- Write your query below
select employee_id, 
    (case 
        when name like 'M%' then 0
        else (salary * (employee_id % 2))
    end) as bonus 
from employees order by employee_id;