import pickle
from fastapi import FastAPI
import uvicorn
from typing import Dict, Any


app = FastAPI(title="lead-scoring-prediction")
file_name = "pipeline_v1.bin"

with open(file_name, 'rb') as f_in:
    pipeline = pickle.load(f_in)


def predict_single(customer):
    result = pipeline.predict_proba(customer)[0, 1]
    return float(result)


@app.post("/predict")
def predict(customer: Dict[str, Any]):
    prob = predict_single(customer)

    return {
        "churn_probability": prob,
        "churn": bool(prob >= 0.5)
    }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)


