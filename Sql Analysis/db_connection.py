import mysql.connector
import pandas as pd
import warnings

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="P@$$w0rd^M4nager",
    database="salary_project"
)
warnings.filterwarnings('ignore')

def run_query(query):
    df = pd.read_sql(query, conn)
    return df


print("\n===== 1. Distinct Job Titles =====")
df1 = run_query("SELECT DISTINCT job_title FROM salary_data;")
print(df1)

print("\n===== 2. Salary greater than 200,000 USD =====")
df2 = run_query("SELECT * FROM salary_data WHERE salary > 200000;")
print(df2)

print("\n===== 3. Senior level employees sorted by salary =====")
df3 = run_query("SELECT * FROM salary_data WHERE experience_level_full='Senior' ORDER BY salary DESC;")
print(df3)

print("\n===== 4. Fully remote employees =====")
df4 = run_query("SELECT * FROM salary_data WHERE remote_ratio=100;")
print(df4)

print("\n===== 5. Max and min salary =====")
df5 = run_query("SELECT MAX(salary) AS MAX_SALARY, MIN(salary) AS MIN_SALARY FROM salary_data;")
print(df5)

print("\n===== 6. Count of Entry level employees =====")
df6 = run_query("SELECT COUNT(*) AS ENTRY_COUNT FROM salary_data WHERE experience_level_full='Entry';")
print(df6)

print("\n===== 7. Average salary across whole dataset =====")
df7 = run_query("SELECT AVG(salary) AS AVG_SALARY FROM salary_data;")
print(df7)

print("\n===== 8. Average salary per job title (highest to lowest) =====")
df8 = run_query("SELECT AVG(salary), job_title FROM salary_data GROUP BY job_title ORDER BY AVG(salary) DESC;")
print(df8)

print("\n===== 9. Average salary per experience level =====")
df9 = run_query("SELECT AVG(salary), experience_level_full FROM salary_data GROUP BY experience_level_full;")
print(df9)

print("\n===== 10. Average salary per company location =====")
df10 = run_query("SELECT AVG(salary), company_location FROM salary_data GROUP BY company_location;")
print(df10)

print("\n===== 11. Average salary per company size =====")
df11 = run_query("SELECT AVG(salary), company_size_full FROM salary_data GROUP BY company_size_full;")
print(df11)

print("\n===== 12. Average salary by remote ratio =====")
df12 = run_query("SELECT AVG(salary), remote_ratio FROM salary_data GROUP BY remote_ratio;")
print(df12)

print("\n===== 13. Employee count per job title (more than 10) =====")
df13 = run_query("SELECT COUNT(*) AS EMP_COUNT, job_title FROM salary_data GROUP BY job_title HAVING EMP_COUNT > 10;")
print(df13)

print("\n===== 14. Average salary by experience level (US only) =====")
df14 = run_query("SELECT AVG(salary), experience_level_full, company_location FROM salary_data WHERE company_location='US' GROUP BY experience_level_full;")
print(df14)

print("\n===== 15. Job titles with average salary > 150,000 USD =====")
df15 = run_query("SELECT job_title, AVG(salary) FROM salary_data GROUP BY job_title HAVING AVG(salary) > 150000;")
print(df15)

print("\n===== 16. Top 5 highest-paying job titles (Senior level) =====")
df16 = run_query("SELECT job_title, MAX(salary) AS max_salary FROM salary_data WHERE experience_level_full='Senior' GROUP BY job_title ORDER BY max_salary DESC LIMIT 5;")
print(df16)

print("\n===== 17. Average salary per year (trend) =====")
df17 = run_query("SELECT AVG(salary), work_year FROM salary_data GROUP BY work_year ORDER BY work_year;")
print(df17)

print("\n===== Subquery 1: Employees earning above overall average =====")
df_sub1 = run_query("SELECT * FROM salary_data WHERE salary > (SELECT AVG(salary) FROM salary_data);")
print(df_sub1)

print("\n===== Subquery 2: Job titles with avg salary > Data Scientist's avg =====")
df_sub2 = run_query("SELECT job_title FROM salary_data GROUP BY job_title HAVING AVG(salary) > (SELECT AVG(salary) FROM salary_data WHERE job_title='Data Scientist');")
print(df_sub2)

print("\n===== Subquery 3: Highest paid employee(s) full record =====")
df_sub3 = run_query("SELECT * FROM salary_data WHERE salary = (SELECT MAX(salary) FROM salary_data);")
print(df_sub3)

print("\n===== Subquery 4: Experience levels below overall average =====")
df_sub4 = run_query("SELECT experience_level_full FROM salary_data GROUP BY experience_level_full HAVING AVG(salary) < (SELECT AVG(salary) FROM salary_data);")
print(df_sub4)

# CLOSE CONNECTION
conn.close()
print("\nConnection closed. All queries completed.")
