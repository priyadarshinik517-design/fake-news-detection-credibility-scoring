from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

# Load model and vectorizer
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

# Home route
@app.route('/')
def home():
    return "Fake News Detection Backend Running"

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():

    data = request.get_json()

    text = data['text']

    vector = vectorizer.transform([text])

    prediction = model.predict(vector)[0]

    result = "REAL" if prediction == 1 else "FAKE"

    return jsonify({
        'prediction': result
    })

# Run app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)