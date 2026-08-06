"""
Converts your EDA.py analysis into a single JSON file that Lovable
can use directly to build charts (no Python needed on the frontend).

Run this AFTER data_cleaning.py has produced cleaned_data.csv.
"""

import pandas as pd
import json

df = pd.read_csv(r"C:\Users\Dell\Desktop\project\DataScience-Salary-Analysis\data\cleaned_data.csv")
print("Cleaned Dataset Loaded Successfully!")

dashboard_data = {}

# 1. Top 10 highest paying job titles
top_jobs = df.groupby('job_title')['salary_in_usd'].mean().nlargest(10)
dashboard_data['top_paying_jobs'] = [
    {"job_title": job, "avg_salary": round(sal, 2)}
    for job, sal in top_jobs.items()
]

# 2. Average salary by experience level
order = ['Entry', 'Mid-Level', 'Senior', 'Executive']
exp_salary = df.groupby('experience_category')['salary_in_usd'].mean()
dashboard_data['salary_by_experience'] = [
    {"level": lvl, "avg_salary": round(exp_salary[lvl], 2)}
    for lvl in order if lvl in exp_salary
]

# 3. Salary distribution by remote category (median, for boxplot-style summary)
order = ['On-site', 'Hybrid', 'Fully Remote']
remote_median = df.groupby('remote_category')['salary_in_usd'].median()
dashboard_data['salary_by_remote_category'] = [
    {"category": cat, "median_salary": round(remote_median[cat], 2)}
    for cat in order if cat in remote_median
]

# 4. Top 10 paying countries
top_pay = df.groupby('employee_residence')['salary_in_usd'].mean().nlargest(10)
dashboard_data['top_paying_countries'] = [
    {"country": country, "avg_salary": round(sal, 2)}
    for country, sal in top_pay.items()
]

# 5. Salary trends by year and experience
salary_trend = df.groupby(['work_year', 'experience_category'])['salary_in_usd'].mean().reset_index()
dashboard_data['salary_trends'] = [
    {
        "year": int(row['work_year']),
        "experience": row['experience_category'],
        "avg_salary": round(row['salary_in_usd'], 2)
    }
    for _, row in salary_trend.iterrows()
]

# 6. Average salary by company size
order = ['Small', 'Medium', 'Large']
size_salary = df.groupby('company_size_category')['salary_in_usd'].mean()
dashboard_data['salary_by_company_size'] = [
    {"size": sz, "avg_salary": round(size_salary[sz], 2)}
    for sz in order if sz in size_salary
]

# 7. Top AI/ML roles comparison
ai_ml_roles = ['Data Scientist', 'Machine Learning Engineer', 'AI Engineer',
               'Data Engineer', 'Research Scientist', 'MLOps Engineer']
ai_df = df[df['job_title'].isin(ai_ml_roles)]
ai_salary = ai_df.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False)
dashboard_data['ai_ml_roles_comparison'] = [
    {"job_title": job, "avg_salary": round(sal, 2)}
    for job, sal in ai_salary.items()
]

# Save everything to one JSON file
with open("dashboard_data.json", "w") as f:
    json.dump(dashboard_data, f, indent=2)

print("Saved dashboard_data.json — upload/paste this into Lovable project.")