from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle

app = Flask(__name__)
CORS(app)

model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

@app.route('/')
def home():
    return "Fake News Detection Backend Running"

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

if __name__ == '__main__':
    app.run(debug=True)