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
        try:
            age = float(request.form['age'])
            job = float(request.form['job'])
            marital = float(request.form['marital'])
            education = float(request.form['education'])
            balance = float(request.form['balance'])
            housing = float(request.form['housing'])
            duration = float(request.form['duration'])
            campaign = float(request.form['campaign'])
            
            # Add index column (0) to match the training data structure
            index_col = 0.0

            features = np.array([[index_col, age, job, marital, education, balance, housing, duration, campaign]])

            prediction = model.predict(features)[0]

            result = "Credit Approved ✅" if prediction == 1 else "Credit Rejected ❌"

            return render_template('result.html', prediction=result)
        except Exception as e:
            # Return error page or handle the error gracefully
            return render_template('result.html', prediction=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
