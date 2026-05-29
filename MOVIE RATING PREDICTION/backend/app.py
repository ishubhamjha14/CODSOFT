from flask import Flask, request, jsonify
from flask_cors import CORS

import pandas as pd
import numpy as np
import os

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# =========================
# FLASK
# =========================

app = Flask(__name__)
CORS(app)

# =========================
# LOAD DATASET
# =========================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_path = os.path.join(
    BASE_DIR,
    "..",
    "data",
    "movies.csv"
)

print("Dataset Path:", csv_path)

df = pd.read_csv(csv_path, encoding='latin1')

# =========================
# CLEAN DATA
# =========================

df = df[['Genre', 'Director', 'Actor 1', 'Duration', 'Rating']]

df.dropna(inplace=True)

# remove "min"
df['Duration'] = df['Duration'].astype(str)
df['Duration'] = df['Duration'].str.replace('min', '')
df['Duration'] = df['Duration'].str.strip()

# remove empty rows
df = df[df['Duration'] != '']

# convert duration to integer
df['Duration'] = df['Duration'].astype(int)

# =========================
# LABEL ENCODING
# =========================

genre_encoder = LabelEncoder()
director_encoder = LabelEncoder()
actor_encoder = LabelEncoder()

df['Genre'] = genre_encoder.fit_transform(df['Genre'])
df['Director'] = director_encoder.fit_transform(df['Director'])
df['Actor 1'] = actor_encoder.fit_transform(df['Actor 1'])

# =========================
# FEATURES
# =========================

X = df[['Genre', 'Director', 'Actor 1', 'Duration']]
y = df['Rating']

# =========================
# TRAIN TEST SPLIT
# =========================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# =========================
# MODEL
# =========================

model = RandomForestRegressor()

model.fit(X_train, y_train)

print("✅ Model Trained Successfully!")

# =========================
# API ROUTE
# =========================

@app.route('/predict', methods=['POST'])
def predict():

    data = request.json

    genre = data['genre']
    director = data['director']
    actor = data['actor']
    duration = int(data['duration'])

    try:

        genre_encoded = genre_encoder.transform([genre])[0]
        director_encoded = director_encoder.transform([director])[0]
        actor_encoded = actor_encoder.transform([actor])[0]

    except:

        return jsonify({
            "error": "Unknown Actor / Director / Genre"
        })

    sample = np.array([[
        genre_encoded,
        director_encoded,
        actor_encoded,
        duration
    ]])

    prediction = model.predict(sample)[0]

    return jsonify({
        "rating": round(prediction, 1)
    })

# =========================
# RUN APP
# =========================

if __name__ == '__main__':
    app.run(debug=True)