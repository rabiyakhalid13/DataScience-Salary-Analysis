import pandas as pd
print(" Library imported successfully!")
df = pd.read_csv(r"C:\Users\Dell\Desktop\project\Data-Science-Salaries\DataScience_salaries_2025.csv")
print("Dataset Loaded Successfully!")

# PHASE 2: DATA CLEANING & FEATURE ENGINEERING
print("PHASE 2: DATA CLEANING & FEATURE ENGINEERING")
print("="*60)

# 1. Remove Duplicates
print("1. Removing duplicates...")
df = df.drop_duplicates()
print("Shape after removing duplicates:", df.shape)

# 2. Experience Feature Engineering
print("\n2. Creating experience features...")

df['experience_category'] = df['experience_level'].map({
    'EN': 'Entry',
    'MI': 'Mid-Level',
    'SE': 'Senior',
    'EX': 'Executive'
})

df['seniority_score'] = df['experience_level'].map({
    'EN': 1,
    'MI': 2,
    'SE': 3,
    'EX': 4
})

# 3. Remote Work Feature
print("\n3. Creating remote work category...")

df['remote_category'] = df['remote_ratio'].map({
    0: 'On-site',
    50: 'Hybrid',
    100: 'Fully Remote'
})


# 4. Company Size Feature
print("\n4. Creating company size category...")

df['company_size_category'] = df['company_size'].map({
    'S': 'Small',
    'M': 'Medium',
    'L': 'Large'
})
# 5. Employement type mapping
print("\n5. Creating employement type full...")

df['employment_type_full'] = df['employment_type'].map({
    'FT': 'Full-Time',
    'PT': 'Part-Time',
    'CT': 'Contract',
    'FL': 'Freelance'
})

print("\n5. Creating Comapny size in integer...")
# Map company size
df['company_size_int']=df['company_size'].map({
    'S':0,
    'M':1,
    'L':2
})

# 6. Job Title Grouping
print("\n6. Grouping rare job titles...")

top_20_titles = df['job_title'].value_counts().head(20).index

df['job_title'] = df['job_title'].apply(
    lambda x: x if x in top_20_titles else 'Other'
)


# 7. Validation Check
print("\n7. Checking transformed features...")

print(df[['experience_level', 'experience_category', 'seniority_score']].head())
print(df[['remote_ratio', 'remote_category']].head())
print(df[['company_size', 'company_size_category']].head())
print(df[['employment_type', 'employment_type_full']].head())
print(df[['company_size', 'company_size_int']].head(10))
# 8. Null values Check
print("\n8. Null values:", df.isnull().sum().sum())

# 9. Data types checking
print("\n9. Checking Data types")
print(df.dtypes)
df['work_year'] = df['work_year'].astype('category')
print("\n After fixing:")
print(df.dtypes)

# 10. Salary Outliers
print("\n 10. Salary Statistics:")
print(df['salary_in_usd'].describe())
Q1=df['salary_in_usd'].quantile(0.25)
Q3=df['salary_in_usd'].quantile(0.75)
IQR=Q3-Q1
lower_bound=Q1-1.5*IQR
upper_bound=Q3+1.5*IQR
df = df[
    (df['salary_in_usd'] >= lower_bound) &
    (df['salary_in_usd'] <= upper_bound)
]
print("Rows after outlier removal: {df.shape}")

# 11. Final Columns Overview
print("\n11. Final dataset columns:")
print(df.columns)

# SAVE CLEANED DATA
print("\nSaving cleaned data...")
df.to_csv(r"C:\Users\Dell\Desktop\project\Data-Science-Salaries\cleaned_data.csv", index=False)
print("Cleaned data saved successfully!")