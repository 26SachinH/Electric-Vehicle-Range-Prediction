# Electric-Vehicle-Range-Prediction

A full-stack machine learning web application that predicts the estimated driving range of an electric vehicle (EV) based on real-world conditions and vehicle parameters.

📖 Overview
This project enables users to enter key EV and environmental parameters, such as battery capacity, energy consumption rate, temperature, wind speed, and precipitation, to predict the expected driving range in kilometers.

It combines:
A trained regression model (stored as ev_range_model.pkl)
A Flask REST API backend
An interactive Bootstrap-powered frontend
This tool can help EV owners and fleet managers estimate range under varying driving conditions.

✨ Key Features
✅ Machine Learning Model
Predicts EV driving range based on six input features.
Model is pre-trained and serialized with joblib.

✅ REST API Endpoint
/predict accepts JSON POST requests with input parameters.
Returns a JSON response containing the predicted range.

✅ User-Friendly Web Interface
Clean, modern Bootstrap design.
Responsive form to input EV and weather parameters.
Instant results display with clear visualization.

✅ CORS Enabled
Allows integration with external clients (e.g., mobile apps).

🧠 How It Works
1️⃣ Input Parameters
Battery_Capacity_kWh: Battery size in kilowatt-hours.
State_of_Charge_%: Current state of charge in percent.
Energy_Consumption_Rate_kWh/km: Consumption rate per km.
Temperature_C: Ambient temperature.
Wind_Speed_m/s: Wind speed.
Precipitation_mm: Precipitation level.

2️⃣ Prediction Pipeline
Input data is validated and converted to a NumPy array.
The trained model predicts the range.
The range is returned via API and displayed on the frontend.

3️⃣ Frontend Interaction
Users fill out the form.
Submitting sends an Axios POST request to the API.
The predicted range is updated on the page without reload.

🛠️ Tech Stack
Layer	Technologies
Backend	Python, Flask, joblib, NumPy
Frontend	HTML, CSS (Bootstrap), JavaScript
Model	Trained regression model (.pkl)

📂 Project Structure
.
├── app.py                  # Flask backend serving prediction API
├── ev_range_model.pkl      # Pre-trained regression model
├── templates/
│   └── index.html          # Frontend web page


💻 Usage
1.Start the Flask server.
2.Open the frontend in your browser.
3.Enter the EV and environmental parameters.
4.Click Predict Range.
5.View the estimated driving range instantly.


🎯 Use Cases
1.EV Drivers: Estimate range before trips.
2.Fleet Managers: Plan charging and routing.
3.Educators: Demonstrate ML applications in transport.
4.Researchers: Analyze the effect of conditions on range.

🔮 Future Improvements
1.Add support for different vehicle types.
2.Include more environmental factors (road gradient, humidity).
3.Enable user accounts and prediction history.
4.Deploy with Docker and HTTPS.
5.Use deep learning models for improved accuracy.

Contact
Author: Sachin S Hebbalakar
Email: sachinhebbalakar26@gmail.com
