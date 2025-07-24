from flask import Flask, render_template, request, url_for
import joblib

app = Flask(__name__)
model = joblib.load('model.joblib')

label_dict = {
    0:'apple',
    1:'banana',
    2:'blackgram',
    3:'chickpea',
    4:'coconut',
    5:'coffee',
    6:'cotton',
    7:'grapes',
    8:'jute',
    9:'kidneybeans',
    10:'lentil',
    11:'maize',
    12:'mango',
    13:'mothbeans',
    14:'mungbean',
    15:'muskmelon',
    16:'orange',
    17:'papaya',
    18:'pigeonpeas',
    19:'pomegranate',
    20:'rice',
    21:'watermelon'
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
