import pandas as pd
import pickle
import os

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Absolute path
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

csv_path = os.path.join(base_dir, "data", "IRIS.csv")

print("Dataset Path:", csv_path)

df = pd.read_csv(csv_path)

X = df.drop("species", axis=1)
y = df["species"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred))

model_path = os.path.join(base_dir, "backend", "iris_model.pkl")

pickle.dump(model, open(model_path, "wb"))

print("Model Saved Successfully!")