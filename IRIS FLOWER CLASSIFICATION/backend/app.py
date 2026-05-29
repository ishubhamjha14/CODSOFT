from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np
import os

app = Flask(__name__)
CORS(app)

# Load Model
model_path = os.path.join(
    os.path.dirname(__file__),
    "iris_model.pkl"
)

model = pickle.load(open(model_path, "rb"))

flower_info = {
    "Iris-setosa": {
        "image": "images/setosa.jpg",
        "description": "Small flower with short petals and sepals."
    },

    "Iris-versicolor": {
        "image": "images/versicolor.jpg",
        "description": "Medium-sized flower with beautiful mixed colors."
    },

    "Iris-virginica": {
        "image": "images/virginica.jpg",
        "description": "Large flower with broad petals and elegant appearance."
    }
}


@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    features = np.array([[
        float(data["sepal_length"]),
        float(data["sepal_width"]),
        float(data["petal_length"]),
        float(data["petal_width"])
    ]])

    prediction = model.predict(features)[0]

    confidence = (
        max(model.predict_proba(features)[0]) * 100
    )

    return jsonify({

        "species": prediction,

        "confidence":
        round(confidence, 2),

        "image":
        flower_info[prediction]["image"],

        "description":
        flower_info[prediction]["description"]

    })


if __name__ == "__main__":
    app.run(debug=True)