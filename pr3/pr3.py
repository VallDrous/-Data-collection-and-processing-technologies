#Використовуючи Faker, створіть набір випадкових даних для енергетичних показників
#(споживання, генерація) для різних типів споживачів (домогосподарства, підприємства).
# Оцініть коректність та корисність згенерованих даних для тестування алгоритмів прогнозування.

import pandas as pd
import random
import math
from faker import Faker
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

fake = Faker()

records = []
consumer_types = ['household', 'enterprise']

for _ in range(15000):
    consumer_type = random.choice(consumer_types)

    date = fake.date_time_between(start_date='-1y', end_date='now')

    day_of_year = date.timetuple().tm_yday
    season_factor = 1 + 0.3 * math.sin(2 * math.pi * day_of_year / 365)

    hour = date.hour
    if 18 <= hour <= 23:
        daily_factor = 1.3
    elif 0 <= hour <= 6:
        daily_factor = 0.7
    else:
        daily_factor = 1.0

    if consumer_type == 'household':
        base_consumption = random.uniform(2, 6)
        generation = max(0, random.gauss(1.5, 0.8))
    else:
        base_consumption = random.uniform(40, 120)
        generation = max(0, random.gauss(20, 10))

    consumption = base_consumption * season_factor * daily_factor + random.uniform(-0.5, 0.5)

    record = {
        'consumer_id': fake.uuid4(),
        'consumer_type': consumer_type,
        'city': fake.city(),
        'datetime': date,
        'energy_consumption_kwh': round(consumption, 2),
        'energy_generation_kwh': round(generation, 2)
    }

    records.append(record)

df = pd.DataFrame(records)

print(df.head())

df['month'] = df['datetime'].dt.month
df['hour'] = df['datetime'].dt.hour
df['consumer_type_num'] = df['consumer_type'].map({'household': 0, 'enterprise': 1})
df = df.drop(columns=['consumer_id', 'city', 'datetime'])

X = df[['consumer_type_num', 'energy_generation_kwh', 'month', 'hour']]
y = df['energy_consumption_kwh']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)

print('R^2 score:', r2)

print(df.head())