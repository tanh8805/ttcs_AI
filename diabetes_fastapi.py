import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

model = joblib.load("diabetes_model.pkl")
app = FastAPI()

class InputData(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

@app.get("/health")
def home():
    return {"status": "ok"}

@app.post("/predict")
def predict(data: InputData):
    df = pd.DataFrame([data.dict()])

    pred = int(model.predict(df)[0])
    prob = float(model.predict_proba(df)[0][1])

    if prob >= 0.8:
        risk_level = "Cao"
        label = "Nguy cơ mắc tiểu đường cao. Khuyến nghị đi khám bác sĩ."
    elif prob >= 0.5:
        risk_level = "Trung bình"
        label = "Nguy cơ mắc tiểu đường ở mức trung bình. Nên kiểm tra thêm."
    else:
        risk_level = "Thấp"
        label = "Nguy cơ mắc tiểu đường thấp."

    return {
        "prediction": pred,
        "diagnosis": "Có nguy cơ tiểu đường" if pred == 1 else "Không có nguy cơ tiểu đường",
        "risk_level": risk_level,
        "probability": round(prob, 4),
        "label": label
    }