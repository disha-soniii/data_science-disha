from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
model = joblib.load('model.joblib')

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/project", methods=["POST", "GET"])
def predict():
    if request.method == "POST":
        age = float(request.form['age'])
        sex = 1 if request.form['sex'] == 'male' else 0
        bmi = float(request.form['bmi'])
        children = int(request.form['children'])
        smoker = 1 if request.form['smoker'] == 'yes' else 0

        region_map = {'southwest': 0, 'southeast': 1, 'northwest': 2, 'northeast': 3}
        region = region_map.get(request.form['region'].lower(), 0)

        features = [[age, sex, bmi, children, smoker, region]]
        prediction = model.predict(features)[0]
        rounded_prediction = round(prediction, 2)

        return render_template("project.html", prediction=rounded_prediction)

    return render_template("project.html")

if __name__ == "__main__":
    app.run(debug=True)
