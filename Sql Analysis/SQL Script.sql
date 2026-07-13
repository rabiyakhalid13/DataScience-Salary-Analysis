CREATE DATABASE salary_project;

CREATE TABLE salary_data (
    work_year INT,
    experience_level VARCHAR(10),
    employment_type VARCHAR(10),
    job_title VARCHAR(100),
    salary INT,
    salary_currency VARCHAR(10),
    salary_in_usd INT,
    employee_residence VARCHAR(10),
    remote_ratio INT,
    company_location VARCHAR(10),
    company_size VARCHAR(10),
    experience_level_full VARCHAR(20),
    seniority_level INT,
    remote_category VARCHAR(20),
    company_size_full VARCHAR(20),
    employment_type_full VARCHAR(20),
    company_size_int INT
);

LOAD DATA INFILE 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/cleaned_data.csv'
INTO TABLE salary_data
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

select count(*) from salary_data;
select * from salary_data;

-- distinct job titles 
SELECT DISTINCT job_title
FROM salary_data;

-- Show all rows where salary is greater than 200,000 USD
SELECT *
FROM salary_data
where salary>200000;

-- Show all Senior level employees sorted by salary (highest to lowest)
SELECT *
from salary_data
where experience_level_full='Senior'
order by salary DESC;

-- Show all fully remote employees (remote_ratio = 100)
SELECT * FROM salary_data WHERE remote_ratio=100;

-- Find the maximum and minimum salary in the dataset
SELECT MAX(salary) AS MAX_SALARY ,MIN(salary) AS MIN_SALARY
FROM salary_data;

-- Count how many employees are at Entry level
SELECT COUNT(*) AS ENTRY_COUNT FROM salary_data WHERE experience_level_full='Entry';

-- Find the average salary across the whole dataset
SELECT AVG(salary) AS AVG_SALARY FROM salary_data;

-- Find average salary for each job title, sorted highest to lowest
SELECT AVG(salary),job_title FROM salary_data GROUP BY job_title ORDER BY AVG(salary) DESC;

-- Find average salary for each experience level (Entry/Mid/Senior)
SELECT AVG(salary),experience_level_full FROM salary_data GROUP BY experience_level_full;

-- Find average salary for each company location (country)
SELECT AVG(salary),company_location FROM salary_data GROUP BY company_location ;

-- Find average salary for each company size (Small/Medium/Large)
SELECT AVG(salary),company_size_full FROM salary_data GROUP BY company_size_full;

-- Find average salary by remote ratio (0%, 50%, 100%)
SELECT AVG(salary),remote_ratio FROM salary_data GROUP BY remote_ratio;

-- Count how many employees exist per job title, only show titles with more than 10 employees
SELECT COUNT(*) AS EMP_COUNT ,job_title FROM salary_data GROUP BY job_title HAVING EMP_COUNT>10;

-- Find average salary by experience level, only for companies based in the US
SELECT AVG(salary),experience_level_full,company_location FROM salary_data WHERE company_location='US' GROUP BY experience_level_full;

-- Find job titles where the average salary is greater than 150,000 USD
SELECT job_title, AVG(salary) FROM salary_data GROUP BY job_title having AVG(salary)>150000;

-- Find the top 5 highest-paying job titles, only among Senior level employees
SELECT job_title , MAX(salary) AS max_salary from salary_data where experience_level_full='Senior' GROUP BY job_title order by max_salary DESC LIMIT 5;
 
-- Find average salary for each year to see if salary trend is increasing or decreasing
SELECT AVG(salary),work_year FROM salary_data group by work_year order by work_year;

-- SUB QUERIES
--  Show all employees whose salary is greater than the overall average salary
Select * FROM salary_data WHERE salary>(SELECT AVG(salary) FROM salary_data);

-- Show all job titles whose average salary is greater than the average salary of "Data Scientist"
Select job_title FROM salary_data group by job_title Having AVG(salary)>(SELECT AVG(salary) FROM salary_data where job_title='Data Scientist');

--  Show the full record of the employee(s) with the highest salary in the dataset
SELECT * FROM salary_data where salary=(select MAX(salary) from salary_data);

-- Show experience levels whose average salary is less than the overall average salary
SELECT experience_level_full 
FROM salary_data 
GROUP BY experience_level_full
HAVING AVG(salary) < (SELECT AVG(salary) FROM salary_data);