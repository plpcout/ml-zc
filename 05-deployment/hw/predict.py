import pickle 
import uvicorn

from fastapi import FastAPI
from typing import Dict, Any

app = FastAPI(title="conversion-prediction")

with open('pipeline_v1.bin', 'rb') as f_in:
    pipeline = pickle.load(f_in)


def predict_single(score):
    result = pipeline.predict_proba([score])[0, 1]
    return float(result)

@app.post("/predict")
def predict(score: Dict[str, Any]):
    prob = predict_single(score)

    return prob
    

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9696)