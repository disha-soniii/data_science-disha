from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

# Load your trained model
model = joblib.load('model.joblib')  

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route('/project')
def project():
    return render_template('project.html')



@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        age = float(request.form['age'])
        weight = float(request.form['weight'])
        height = float(request.form['height'])
        family_history = int(request.form['family_history'])
        menstrual_irregularity = int(request.form['menstrual_irregularity'])
        hormonal_imbalance = int(request.form['hormonal_imbalance'])
        hyperandrogenism = int(request.form['hyperandrogenism'])
        hirsutism = int(request.form['hirsutism'])
        mental_health = int(request.form['mental_health'])
        insulin_resistance = int(request.form['insulin_resistance'])
        diabetes = int(request.form['diabetes'])
        exercise_frequency = int(request.form['exercise_frequency'])
        exercise_type = int(request.form['exercise_type'])
        exercise_duration = float(request.form['exercise_duration'])
        sleep_hours = float(request.form['sleep_hours'])
        stress_level = int(request.form['stress_level'])
        smoking = int(request.form['smoking'])

        features = np.array([[age, weight, height, family_history, menstrual_irregularity,
                              hormonal_imbalance, hyperandrogenism, hirsutism, mental_health,
                              insulin_resistance, diabetes, exercise_frequency, exercise_type,
                              exercise_duration, sleep_hours, stress_level, smoking]])

        prediction = model.predict(features)[0]

        result = "High Risk of PCOS" if prediction == 1 else "Low Risk of PCOS"

        return render_template('result.html', prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
