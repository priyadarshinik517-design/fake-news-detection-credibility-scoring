from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import os

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# load model + vectorizer
model = pickle.load(open(os.path.join(BASE_DIR, "model.pkl"), "rb"))
vectorizer = pickle.load(open(os.path.join(BASE_DIR, "vectorizer.pkl"), "rb"))

@app.route("/")
def home():
    return "Fake News API Running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text", "")

    # transform text using vectorizer
    text_vector = vectorizer.transform([text])

    # prediction
    prediction = model.predict(text_vector)[0]

    result = "Real" if prediction == 1 else "Fake"

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)