# 📊 Data Science Salary Analysis (2020–2025)

## About This Project

I worked on this project to understand how salaries in the data science field 
have changed over the last few years, and what actually drives those numbers 
up or down. Using a dataset of over 45,000 salary records collected between 
2020 and 2025, I looked into how things like experience level, job title, 
company size, location, and remote work setup affect how much someone earns 
in this field.

The project is split into three main parts — first, cleaning and exploring 
the data through visualizations to find patterns and trends, second, building 
a few machine learning models to see how well salary could actually be 
predicted from the available features, and third, re-analyzing the same 
dataset using SQL to practice database querying and connecting Python to a 
MySQL database. I also extended the analysis into an interactive Excel 
dashboard for a more visual, filterable view of the data.

## What I Wanted to Find Out

- How have data science salaries trended from 2020 to 2025?
- Which job roles pay the most?
- Does experience level make a big difference in pay?
- How do salaries compare across different countries?
- Does company size matter when it comes to compensation?
- Does working remotely actually affect salary, up or down?
- Can a machine learning model predict salary accurately using this data?

## Dataset Details

- **Records:** 45,523
- **Years Covered:** 2020 to 2025
- **Target Column:** `salary_in_usd`

### Features Used

- Experience Level
- Employment Type
- Job Title
- Company Size
- Remote Ratio
- Company Location

## Tools I Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost

## How I Approached It

### 1. Cleaning and Preparing the Data

Before jumping into analysis, I checked the dataset for missing values, dropped a few columns that weren't useful for this analysis, and encoded the categorical columns so they could be used in the ML models later.

### 2. Exploring the Data

This is where most of the interesting insights came from. I created several visualizations to understand the patterns better:


### Top 10 Highest Paying Job Titles

![Top Job Titles](images/top_10_highest_paying_job_titles.png)

---

### Salary by Experience Level

![Experience Level](images/salary_by_experience_level.png)

---

### Top 10 Paying Countries

![Countries](images/top_10_paying_countries.png)

---

### Salary Trends (2020–2025)

![Trends](images/salary_trends_2020_2025.png)

---

### Correlation Heatmap

![Heatmap](images/correlation_heatmap.png)

---
### 3. Building the Models

Once the EDA part was done, I moved on to building a few regression models to try and predict salary:

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor

To check how well each model performed, I used:

- R² Score
- Mean Absolute Error (MAE)

  ## What I Found

- Applied Scientist roles came out on top in terms of average salary.
- Senior and executive-level professionals earned noticeably more than entry-level employees, which was expected but good to confirm with real data.
- Medium-sized companies, surprisingly, offered some of the most competitive salaries — sometimes even more than large companies.
- There wasn't a huge difference between remote and on-site salaries, which kind of surprised me going in.
- Overall, salaries showed a general upward trend across the years.

## Where the Models Fell Short

Honestly, the prediction models didn't perform as well as I expected. Even with Random Forest and XGBoost, the R² scores stayed on the lower side and the MAE was higher than I'd have liked.

After digging into it, I think the main reason is that the dataset simply doesn't have some of the factors that actually move salary numbers the most, like:

- Educational background
- Actual years of experience (not just experience level buckets)
- Specific technical skills or certifications
- Company revenue or industry type
- Individual performance and negotiation skills

So no matter how advanced the model, it can only work with what's in the data. This was a good reminder that better models can't fix missing or limited features — the data itself sets the ceiling on what's possible.

## Excel Dashboard

Extended this analysis into an interactive Excel dashboard using pivot tables, 
pivot charts, and slicers — allowing users to filter salary data by 
experience level and remote work category.

### Dashboard Overview (No Filters)
![Dashboard Overview](Excel%20Dashboard/dashboard-overview.png)

### Filtered by Senior Experience Level
![Senior Filter](Excel%20Dashboard/dashboard-senior-filter.png)

### Filtered by Fully Remote Category
![Remote Filter](Excel%20Dashboard/dashboard-remote-filter.png)

[Download the Excel file](Excel%20Dashboard/dashboard.xlsx)

## SQL Analysis

To strengthen the database querying side of this analysis, I re-explored 
the same dataset using SQL — importing it into MySQL and writing queries 
to answer many of the same questions I had explored in Python, plus a 
few new ones.

### What I Practiced
- Filtering and sorting data (WHERE, ORDER BY)
- Aggregate functions (AVG, MAX, MIN, COUNT)
- Grouping and conditional grouping (GROUP BY, HAVING)
- Subqueries (e.g., finding employees earning above the overall average salary)
- Connecting Python to MySQL using the DB-API pattern (mysql-connector-python) 
  and running queries via pandas

### Why I Did This Separately from the Python EDA
The Python section focuses on exploration and visualization. This section 
focuses on database querying itself — writing correct, efficient SQL and 
integrating it with Python, which is a distinct skill from pandas-based analysis.

### Sample Insight

Senior-level employees earn significantly above the dataset average, while 
Entry-level salaries fall below it — confirmed independently through SQL 
aggregate queries.

[Download SQL queries](https://github.com/rabiyakhalid13/DataScience-Salary-Analysis/blob/main/Sql%20Analysis/SQL%20Script.sql) | [Python connection script](https://github.com/rabiyakhalid13/DataScience-Salary-Analysis/blob/main/Sql%20Analysis/db_connection.py)

