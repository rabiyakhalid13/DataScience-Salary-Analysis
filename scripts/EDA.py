import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"C:\Users\Dell\Desktop\project\Data-Science-Salaries\cleaned_data.csv")
print("Cleaned Dataset Loaded Successfully!")
# PHASE 3: EDA + Analytics Dashboard
print("PHASE 3: EDA + ANALYTICS DASHBOARD")
print("="*60)

#GRAPH 1
#TOP 10 HIGHEST PAYING JOB TITLES
print("Graph 1: Top 10 highest paying job titles")
#preparng data
top_jobs=df.groupby('job_title')['salary_in_usd'].mean()
plt.figure(figsize=(16, 9))
top_jobs=top_jobs.nlargest(10)
sns.barplot(x=top_jobs.index,y=top_jobs.values)
plt.title("TOP 10 HIGHEST PAYING JOB TITLES",fontsize=16,fontweight='bold')
plt.xlabel("JOB TITLES",fontsize=12)
plt.ylabel("AVERAGE SALARY",fontsize=12)
# X labels not overlap
plt.xticks(rotation=30, ha='right', fontsize=10)
plt.subplots_adjust(bottom=0.25)
plt.savefig("images/top_10_highest_paying_job_titles.png",
            dpi=300,
            bbox_inches='tight')

plt.show()

#GRAPH 2
#Average Salary by Experience level
print("Graph 2: Average Salary by Experience level")
#preparng data
exp_salary = df.groupby('experience_category')['salary_in_usd'].mean()
#Order
order=['Entry', 'Mid-Level','Senior' ,'Executive']
plt.figure(figsize=(16, 9))
sns.barplot(x=order,y=exp_salary[order])
plt.title("Average Salary by Experience level",fontsize=16,fontweight='bold')
plt.xlabel("Experience Levels",fontsize=12)
plt.ylabel("AVERAGE SALARY",fontsize=12)
# X labels not overlap
plt.xticks(rotation=30, ha='right', fontsize=10)
plt.subplots_adjust(bottom=0.25)
plt.savefig("images/salary_by_experience_level.png",
            dpi=300,
            bbox_inches='tight')

plt.show()

# GRAPH 3
# SALARY DISTRIBUTION REMOTE VS HYBRID VS ON-SITE
print("Graph 3: Salary Distribution by Remote Category")
# Order 
order = ['On-site', 'Hybrid', 'Fully Remote']
plt.figure(figsize=(16, 9))
sns.boxplot(data=df,x='remote_category',y='salary_in_usd',order=order)
plt.title("Salary Distribution by Remote Category",fontsize=16,fontweight='bold')
plt.xlabel("Work_category",fontsize=12)
plt.ylabel("SALARY (USD)",fontsize=12)
# X labels not overlap
plt.xticks(rotation=30, ha='right', fontsize=10)
plt.subplots_adjust(bottom=0.25)
plt.savefig("images/salary_distribution_remote_category.png",
            dpi=300,
            bbox_inches='tight')
plt.show()

# GRAPH 4
# Top 10 Paying Countries 
print("Graph 4:Top 10 Paying Countries ")
plt.figure(figsize=(16, 9))
top_pay=df.groupby('employee_residence')['salary_in_usd'].mean()
top_pay=top_pay.nlargest(10)
sns.barplot(x=top_pay.index,y=top_pay.values)
plt.title("Top 10 Paying Countries",fontsize=16,fontweight='bold')
plt.xlabel("Countries",fontsize=12)
plt.ylabel("Average SALARY (USD)",fontsize=12)
# X labels not overlap
plt.xticks(rotation=30, ha='right', fontsize=10)
plt.subplots_adjust(bottom=0.25)
plt.savefig("images/top_10_paying_countries.png",
            dpi=300,
            bbox_inches='tight')
plt.show()

#GRAPH 5
# SALARY TRENDS [2020-2025] BY EXPERIENCE 
print("Graph 5: SALARY TRENDS [2020-2025] BY EXPERIENCE")
plt.figure(figsize=(16, 9))
salary_trend=df.groupby(['work_year','experience_category'])['salary_in_usd'].mean()
salary_trend_df = salary_trend.reset_index()
sns.lineplot(data=salary_trend_df,x='work_year',y='salary_in_usd',
             hue='experience_category')  
plt.title("SALARY TRENDS [2020-2025] BY EXPERIENCE",fontsize=16,fontweight='bold')
plt.xlabel("Year",fontsize=12)
plt.ylabel("Average_Salary",fontsize=12)
# X labels not overlap
plt.xticks(rotation=30, ha='right', fontsize=10)
plt.subplots_adjust(bottom=0.25)
plt.savefig("images/salary_trends_2020_2025.png",
            dpi=300,
            bbox_inches='tight')
plt.show()

# GRAPH 6
# Average Salary by company size
print(" GRAPH 6: Average Salary by company size")
plt.figure(figsize=(16, 9))
order=['Small','Medium','Large']
avg_sal=df.groupby('company_size_category')['salary_in_usd'].mean()
sns.barplot(x=order,y=avg_sal[order])
plt.title("Average Salary by company size",fontsize=16,fontweight='bold')
plt.xlabel("Company Size",fontsize=12)
plt.ylabel("Average SALARY (USD)",fontsize=12)
# X labels not overlap
plt.xticks(rotation=30, ha='right', fontsize=10)
plt.subplots_adjust(bottom=0.25)
plt.savefig("images/salary_by_company_size.png",
            dpi=300,
            bbox_inches='tight')
plt.show()

# Available job titles 
print(df['job_title'].unique())
# GRAPH 7
# TOP AI/ML ROLES SALARY COMPARISON
print("GRAPH 7: Top AI/ML Roles Salary Comparison")
ai_ml_roles = [
    'Data Scientist',
    'Machine Learning Engineer', 
    'AI Engineer',
    'Data Engineer',
    'Research Scientist',
    'MLOps Engineer'
]
ai_df = df[df['job_title'].isin(ai_ml_roles)]
ai_salary = ai_df.groupby('job_title')['salary_in_usd'].mean()
ai_salary = ai_salary.sort_values(ascending=False)
plt.figure(figsize=(12, 7))

sns.barplot(x=ai_salary.index, 
            y=ai_salary.values)

plt.title("TOP AI/ML ROLES SALARY COMPARISON", 
          fontsize=16, fontweight='bold')
plt.xlabel("Job Title", fontsize=12)
plt.ylabel("Average Salary (USD)", fontsize=12)
plt.xticks(rotation=30, ha='right', fontsize=9)
plt.subplots_adjust(bottom=0.25)
plt.show()
plt.savefig("images/ai_ml_roles_salary_comparison.png",
            dpi=300,
            bbox_inches='tight')
plt.show()

# GRAPH 8: CORRELATION HEATMAP
#heatmap only shows relation btw numerical columns
print("GRAPH 8: Correlation Heatmap")
numeric_cols = df[['salary_in_usd', 
                   'seniority_score',
                   'remote_ratio']]
correlation = numeric_cols.corr()
plt.figure(figsize=(16, 9))
sns.heatmap(correlation,
            annot=True)
plt.title("CORRELATION HEATMAP", fontsize=16, fontweight='bold')
plt.savefig("images/correlation_heatmap.png",
            dpi=300,
            bbox_inches='tight')
plt.show()