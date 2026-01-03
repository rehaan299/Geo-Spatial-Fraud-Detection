import uuid
import random
import csv
import datetime

city_coords = {
    "Toronto": (43.65, -79.38),
    "Vancouver": (49.28, -123.12),
    "Montreal": (45.50, -73.57),
    "Calgary": (51.05, -114.07),
    "New York": (40.71, -74.00)
}

merchants = [
    "CoffeeShop",
    "ElectronicsStore",
    "GroceryMart",
    "OnlineRetailer",
    "GasStation"
]

NUM_RECORDS = 10000
FRAUD_RATIO = 0.02

num_frauds = int(NUM_RECORDS * FRAUD_RATIO)
num_legit = NUM_RECORDS - num_frauds

transactions = []

def random_timestamp():
    return datetime.datetime(
        2025,
        random.randint(1, 12),
        random.randint(1, 28),
        random.randint(0, 23),
        random.randint(0, 59),
        random.randint(0, 59)
    ).isoformat()

# Fraudulent transactions
for _ in range(num_frauds):
    city = random.choice(list(city_coords.keys()))
    lat, lon = city_coords[city]

    transactions.append([
        str(uuid.uuid4()),
        random.randint(10000, 99999),
        round(random.uniform(300, 2000), 2),
        random_timestamp(),
        random.choice(merchants),
        city,
        round(lat + random.uniform(-0.1, 0.1), 6),
        round(lon + random.uniform(-0.1, 0.1), 6),
        1
    ])

# Legitimate transactions
for _ in range(num_legit):
    city = random.choice(list(city_coords.keys()))
    lat, lon = city_coords[city]

    transactions.append([
        str(uuid.uuid4()),
        random.randint(10000, 99999),
        round(random.uniform(5, 500), 2),
        random_timestamp(),
        random.choice(merchants),
        city,
        round(lat + random.uniform(-0.1, 0.1), 6),
        round(lon + random.uniform(-0.1, 0.1), 6),
        0
    ])

random.shuffle(transactions)

with open("data/transactions.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "TransactionID",
        "UserID",
        "Amount",
        "Timestamp",
        "MerchantName",
        "City",
        "Latitude",
        "Longitude",
        "IsFraud"
    ])
    writer.writerows(transactions)

print("✅ Generated transactions.csv with 10,000 records")
