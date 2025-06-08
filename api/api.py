from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import pickle

model = pickle.load(open("model.pkl", "rb"))

app = FastAPI()

class TransactionDetails(BaseModel):
    distance_from_home: float
    distance_from_last_transaction: float
    ratio_to_median_purchase_price: float
    repeat_retailer: float
    used_chip: float
    used_pin_number: float
    online_order: float

@app.post("/predict")
def predict(transaction_details: TransactionDetails):
    features = np.array([[transaction_details.distance_from_home,
                          transaction_details.distance_from_last_transaction,
                          transaction_details.ratio_to_median_purchase_price,
                          transaction_details.repeat_retailer,
                          transaction_details.used_chip,
                          transaction_details.used_pin_number,
                          transaction_details.online_order]])
    
    prediction = model.predict(features)[0]
    return {"fraude": bool(prediction)}
