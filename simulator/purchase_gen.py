import json
import random
import time
import os
from math import exp

PATH = "new_purchase.json"

def generate_purchase():
    online_order = random.choices([0, 1], weights=[0.6, 0.4])[0]
    repeat_retailer = random.choices([0, 1], weights=[0.1, 0.9])[0]
    
    if random.random() < 0.05:
        distance_from_home = round(random.uniform(50, 1000), 2)
    else:
        distance_from_home = round(random.uniform(0, 50), 2)
    
    if random.random() < 0.03:
        distance_from_last = round(random.uniform(50, 1000), 2)
    else:
        distance_from_last = round(random.uniform(0, 20), 2)
    
    if random.random() < 0.04:
        ratio_price = round(random.choices(
            [random.uniform(0.05, 0.3), random.uniform(4, 20)],
            weights=[0.4, 0.6]
        )[0], 2)
    else:
        ratio_price = round(random.uniform(0.3, 3), 2)
    
    used_chip = random.choices([0, 1], weights=[0.4, 0.6])[0]
    if online_order:
        used_pin = 0
    else:
        used_pin = random.choices([0, 1], weights=[0.8, 0.2])[0]
    
    return {
        "distance_from_home": distance_from_home,
        "distance_from_last_transaction": distance_from_last,
        "ratio_to_median_purchase_price": ratio_price,
        "repeat_retailer": repeat_retailer,
        "used_chip": used_chip,
        "used_pin_number": used_pin,
        "online_order": online_order
    }

print("🧪 Enhanced purchase simulator started...")

while True:
    purchase = generate_purchase()
    if not os.path.exists(PATH):
        with open(PATH, "w") as f:
            json.dump(purchase, f)
        print("🛒 New simulated purchase:", purchase)

    time.sleep(0.5)