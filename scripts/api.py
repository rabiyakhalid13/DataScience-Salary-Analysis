from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="Salary Predictor API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("salary_model.pkl")
feature_columns = joblib.load("feature_columns.pkl")

class SalaryInput(BaseModel):
    seniority_score: int      
    remote_ratio: int         
    company_size_int: int     
    work_year: int            

@app.get("/")
def home():
    return {"status": "Salary Predictor API is running"}

@app.post("/predict")
def predict_salary(data: SalaryInput):
    input_df = pd.DataFrame([[
        data.seniority_score,
        data.remote_ratio,
        data.company_size_int,
        data.work_year
    ]], columns=feature_columns)

    prediction = model.predict(input_df)[0]

    return {
        "predicted_salary_usd": round(float(prediction), 2)
    }