from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS

# Load the trained model
model = joblib.load('ev_range_model.pkl')

# Features expected in the input
features = [
    'Battery_Capacity_kWh',
    'State_of_Charge_%',
    'Energy_Consumption_Rate_kWh/km',
    'Temperature_C',
    'Wind_Speed_m/s',
    'Precipitation_mm',
]

@app.route('/')
def home():
    return render_template('index.html')  # Render the HTML template

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = request.get_json()

        # Ensure all required features are present
        if not all(feature in input_data for feature in features):
            return jsonify({"error": "Missing required features in input data"}), 400

        # Extract feature values
        feature_values = [input_data[feature] for feature in features]
        
        # Convert to numpy array for prediction
        feature_values = np.array(feature_values).reshape(1, -1)
        
        # Predict range
        predicted_range = model.predict(feature_values)[0]

        return jsonify({"predicted_range_km": predicted_range})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
