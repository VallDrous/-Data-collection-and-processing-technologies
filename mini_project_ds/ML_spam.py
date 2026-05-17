import pandas as pd
import time

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import accuracy_score, f1_score

df = pd.read_csv("dataset_cr_email.csv").dropna()

X = df["text"]
y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = Pipeline([
    ("tfidf", TfidfVectorizer(
        analyzer="char",
        ngram_range=(3, 5)
    )),
    ("nb", MultinomialNB())
])

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, average="weighted")

AUTO_REPLIES = {
    "spam": "Це повідомлення визначено як спам і буде проігноровано.",
    "ham": "Ваш лист отримано. Ми відповімо найближчим часом."
}

def generate_reply(label: str):
    label = label.lower().strip()
    return AUTO_REPLIES.get(label, "Повідомлення прийнято в обробку.")

app = FastAPI(title="Агент обробки електронної пошти")


class Email(BaseModel):
    text: str


@app.get("/")
def info():
    return {
        "status": "active",
        "accuracy": float(accuracy),
        "f1_score": float(f1)
    }


@app.post("/process")
def process_email(email: Email):

    start = time.time()

    label = model.predict([email.text])[0]

    reply = generate_reply(label)

    latency = time.time() - start

    return {
        "text": email.text,
        "label": label,
        "auto_reply": reply,
        "latency_sec": round(latency, 4)
    }

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)