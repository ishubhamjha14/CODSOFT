from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from model import train_model

app = Flask(__name__)

CORS(app)

model, accuracy = train_model()

@app.route('/')
def home():
    return "Titanic AI Backend Running 🚀"

@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json()

    sample = [[
        data['pclass'],
        data['sex'],
        data['age'],
        data['sibsp'],
        data['parch'],
        data['fare'],
        data['embarked']
    ]]

    result = model.predict(sample)[0]
    probability = model.predict_proba(sample)[0][1]

    return jsonify({
        "result": int(result),
        "probability": float(probability)
    })

if __name__ == '__main__':
    app.run(debug=True)