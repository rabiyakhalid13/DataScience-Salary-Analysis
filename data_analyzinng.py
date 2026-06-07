import pandas as pd
print(" Library imported successfully!")
df = pd.read_csv(r"C:\Users\Dell\Desktop\project\Data-Science-Salaries\DataScience_salaries_2025.csv")
print("Dataset Loaded Successfully!")

# PHASE 1: DATA UNDERSTANDING (Clean Version)
print("PHASE 1:DATA ANALYZING")
print("\n" + "="*60)
print(f"Total Rows: {df.shape[0]:,}")
print(f"Total Columns: {df.shape[1]}\n")

print("Column Names:")
print(df.columns.tolist(), "\n")

print("1. Unique Job Titles:", df['job_title'].nunique())
print("\n2. Top 10 Most Common Job Titles:")
print(df['job_title'].value_counts().head(10))

print("\n3. Experience Levels:", sorted(df['experience_level'].unique()))

print("\n4. Company Sizes:", sorted(df['company_size'].unique()))

print("\n5. Remote Ratio Values:", sorted(df['remote_ratio'].unique()))

print("\n6. Years in Dataset:", sorted(df['work_year'].unique()))

print("\n7. Unique Countries:", df['company_location'].nunique())
print("Top 10 Countries:")
print(df['company_location'].value_counts().head(10))

print("\n8. Salary Statistics (USD):")
print(df['salary_in_usd'].describe().round(2))

print("\n9. Missing Values:")
print(df.isnull().sum())

print("\n10. Duplicate Rows:", df.duplicated().sum())

print("\n" + "="*60)
print("PHASE 1 COMPLETED ")