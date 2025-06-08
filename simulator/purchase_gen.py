import json
import random
import time
import os

PATH = "new_purchase.json"
FRAUD_EVERY_X = 5
counter = 0

FRAUDULENT_PURCHASES = [
    [51.188, 2.7825, 4.1587, 1.0, 0.0, 0.0, 1.0],
    [1.6170, 0.3751, 6.8958, 0.0, 1.0, 0.0, 1.0],
    [8.6130, 1.0712, 12.4882, 1.0, 0.0, 0.0, 1.0],
    [0.4260, 0.6167, 4.0798, 0.0, 0.0, 0.0, 1.0],
    [25.3268, 0.0908, 5.3197, 1.0, 1.0, 0.0, 1.0],
]

def generate_fraudulent_purchase():
    base = random.choice(FRAUDULENT_PURCHASES)
    
    return {
        "distance_from_home": round(random.gauss(base[0], base[0] * 0.1), 2),
        "distance_from_last_transaction": round(random.gauss(base[1], base[1] * 0.2 + 0.1), 2),
        "ratio_to_median_purchase_price": round(random.gauss(base[2], base[2] * 0.15), 2),
        "repeat_retailer": int(base[3]),
        "used_chip": int(base[4]),
        "used_pin_number": int(base[5]),
        "online_order": int(base[6])
    }

def generate_legitimate_purchase():
    return {
        "distance_from_home": round(random.uniform(0, 20), 2),
        "distance_from_last_transaction": round(random.uniform(1, 10), 2),
        "ratio_to_median_purchase_price": round(random.uniform(0.3, 1.5), 2),
        "repeat_retailer": 1,
        "used_chip": 1,
        "used_pin_number": 1,
        "online_order": 0
    }

print("🧪 Purchase simulator started...")

while True:
    if not os.path.exists(PATH):
        counter += 1
        if counter % FRAUD_EVERY_X == 0:
            purchase = generate_fraudulent_purchase()
            print("⚠️ Fraudulent purchase simulated:", purchase)
        else:
            purchase = generate_legitimate_purchase()
            print("🛒 Legitimate purchase simulated:", purchase)

        with open(PATH, "w") as f:
            json.dump(purchase, f)

    time.sleep(0.5)