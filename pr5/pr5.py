import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

user_data = {
    'age': 37,
    'workclass': 'Private',
    'fnlwgt': 284582,
    'education': 'Bachelors',
    'education-num': 13,
    'marital-status': 'Married-civ-spouse',
    'occupation': 'Exec-managerial',
    'relationship': 'Husband',
    'race': 'White',
    'sex': 'Male',
    'capital-gain': 0,
    'capital-loss': 0,
    'hours-per-week': 45,
    'native-country': 'United-States'
}

user_df = pd.DataFrame([user_data])

columns = [
    'age', 'workclass', 'fnlwgt', 'education', 'education-num', 
    'marital-status', 'occupation', 'relationship', 'race', 'sex', 
    'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income'
]

df = pd.DataFrame(pd.read_csv('adult.data', header=None, names=columns, skipinitialspace=True))

encoders = {}

for col in df.columns:
    if df[col].dtype == 'str':
        le = LabelEncoder() 
        df[col] = le.fit_transform(df[col])
        encoders[col] = le
        
X = df.drop('income', axis=1)
y = df['income']

clf = RandomForestClassifier(max_depth=20, random_state=0)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)
print(f"Точність моделі: {accuracy:.2%}")
  
for col in user_df.columns:
    if col in encoders:
        user_df[col] = encoders[col].transform(user_df[col])      
        
prediction = clf.predict(user_df)

income_label = encoders['income'].inverse_transform(prediction)
print("Прогноз:", income_label[0])