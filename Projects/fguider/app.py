from flask import Flask, render_template, request, url_for
import joblib

app = Flask(__name__)
model = joblib.load('model.joblib')

label_dict = {
    0: 'rice', 1: 'maize', 2: 'wheat', 3: 'cotton', 4: 'barley',
    5: 'pulses', 6: 'groundnut', 7: 'sugarcane', 8: 'millet',
    9: 'oilseeds', 10: 'potato', 11: 'onion', 12: 'banana',
    13: 'tomato', 14: 'grapes', 15: 'apple'
}

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/predict", methods=['POST'])
def predict():
    n = float(request.form['n'])
    p = float(request.form['p'])
    k = float(request.form['k'])
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    ph = float(request.form['ph'])
    rainfall = float(request.form['rainfall'])

    features = [[n, p, k, temperature, humidity, ph, rainfall]]
    prediction = model.predict(features)[0]
    predicted_crop = label_dict.get(prediction, "Unknown Crop")
    
    image_file = f"images/{predicted_crop.lower()}.jpg"

    return render_template('result.html', image_file=image_file, prediction=predicted_crop)



if __name__ == "__main__":
    app.run(debug=True)
