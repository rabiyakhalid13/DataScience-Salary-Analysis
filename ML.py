import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import  LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

df = pd.read_csv(r"C:\Users\Dell\Desktop\project\Data-Science-Salaries\cleaned_data.csv")
print("Cleaned Dataset Loaded Successfully!")
#Chaging Data type of work year to int
df['work_year'] = df['work_year'].astype(int)

# FEATURES AND TARGET
X = df[['seniority_score', 'remote_ratio', 'company_size_int','work_year']]
y = df['salary_in_usd']
print("Features Shape:", X.shape)
print("Target Shape:  ", y.shape)

# Using train test split
train_X,val_X,train_y,val_y=train_test_split(X,y,test_size=0.2,random_state=1)
print("Training rows ", train_X.shape[0])
print("Testing rows ", val_X.shape[0])

# MODEL 1 :LINEAR REGRESSION
print("\n LINEAR REGRESSION MODEL")
model=LinearRegression()
# Train model
model.fit(train_X,train_y)
print("Model Trained!")
# Predict
predictions=model.predict(val_X)
print("Predictions Done!")
#Evaluate model
# r2 score tells correct percentage of prediction of model
lr_r2  = r2_score(val_y, predictions)
# mae tells error in average of predictions
lr_mae = mean_absolute_error(val_y, predictions)
print(f"R2 Score: {lr_r2:.2f}")
print(f"MAE:     ${lr_mae:,.0f}")


# MODEL 2: DESCISION TREE REGRESSOR
print("\n DECISION TREE MODEL")
dt_model = DecisionTreeRegressor(random_state=1)
dt_model.fit(train_X, train_y)
print("Model Trained!")
dt_predictions = dt_model.predict(val_X)
print("Predictions Done!")
dt_r2  = r2_score(val_y, dt_predictions)
dt_mae = mean_absolute_error(val_y, dt_predictions)
print(f"R2 Score: {dt_r2:.2f}")
print(f"MAE:     ${dt_mae:,.0f}")


# MODEL 3: RANDOM FOREST
print("\n RANDOM FOREST MODEL")
rf_model=RandomForestRegressor(n_estimators=100,random_state=1)
rf_model.fit(train_X, train_y)
print("Model Trained!")
rf_predictions = rf_model.predict(val_X)
print("Predictions Done!")
rf_r2  = r2_score(val_y, rf_predictions)
rf_mae = mean_absolute_error(val_y, rf_predictions)
print(f"R2 Score: {rf_r2:.2f}")
print(f"MAE:     ${rf_mae:,.0f}")

# MODEL 4: XGBOOST MODEL
print("\n XGBoost MODEL")
xgb_model=XGBRegressor(n_estimators=100,learning_rate=0.1,random_state=1)
xgb_model.fit(train_X,train_y)
print("Model Trained!")
xgb_predictions = xgb_model.predict(val_X)
print("Predictions Done!")
xgb_r2  = r2_score(val_y, xgb_predictions)
xgb_mae = mean_absolute_error(val_y, xgb_predictions)
print(f"R2 Score: {xgb_r2:.2f}")
print(f"MAE:     ${xgb_mae:,.0f}")

# Comparison of above 3 models
print("\n"+"="*45)
print(" MODEL COMPARISON")
print("="*45)
print(f"Linear Regression : R2: {lr_r2:.2f}  MAE: ${lr_mae:,.0f}")
print(f"Decision Tree     : R2: {dt_r2:.2f}  MAE: ${dt_mae:,.0f}")
print(f"Random Forest     : R2: {rf_r2:.2f}  MAE: ${rf_mae:,.0f}")
print(f"XGBoost           → R2: {xgb_r2:.2f}  MAE: ${xgb_mae:,.0f}")
print("="*45)
print("\nBest Model: XGBoost")
print("Note :R2 SCORE IS LOW BECAUSE OF LIMITED FEATURES IN DATASET")

# FEATURE IMPORTANCE PLOT
print(" \n FEATURE IMPORTANCE PLOT")
importance = rf_model.feature_importances_
feature_names = X.columns
plt.figure(figsize=(10,7))
sns.barplot(x=importance,y=feature_names)
plt.title("FEATURE IMPORTANCE", fontsize=16, fontweight='bold')
plt.xlabel("Importance Score", fontsize=12)
plt.ylabel("Features", fontsize=12)
plt.show()

# ACTUAL VS PREDICTED SCATTER PLOT
plt.figure(figsize=(10,7))
# SCATTERPLOT
sns.scatterplot(x=val_y,y=rf_predictions)
# Perfect line
plt.plot([val_y.min(),val_y.max()],
         [val_y.min(),val_y.max()],
         label='perfect_predictions'
         )
plt.title("ACTUAL VS PREDICTED SALARY",
          fontsize=16, fontweight='bold')
plt.xlabel("Actual Salary", fontsize=12)
plt.ylabel("Predicted Salary", fontsize=12)
plt.show()

