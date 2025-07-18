from flask import Flask , render_template, request, url_for
import joblib
import csv
import os

model = joblib.load('model.joblib')
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')
@app.route("/contact")
def contact():
    return render_template('contact.html')
@app.route('/about')
def about():
    return render_template('about.html')

@app.route("/history")
def history():
    file_path = "prediction_history.csv"

    # Check if the file exists; if not, return empty history
    if not os.path.exists(file_path):
        historical_data = []
    else:
        with open(file_path, newline='') as f:
            reader = csv.reader(f)
            historical_data = list(reader)

    return render_template("history.html", historical_data=historical_data)

@app.route('/project', methods = ["POST","GET"])
def predict():
    if request.method=='POST':
        brand_name=request.form['brand_name']
        processor_brand = request.form['processor_brand']
        processor_name = request.form['processor_name']
        processor_gnrtn = request.form['processor_gnrtn']
        ram_gb=request.form['ram_gb']
        ram_type=request.form['ram_type']
        ssd=request.form['ssd']
        hdd=request.form['hdd']
        os=request.form['os']
        os_bit=request.form['os_bit']
        graphic_card_gb=request.form['graphic_card_gb']
        warranty=request.form['warranty']
        Touchscreen=request.form['Touchscreen']
        msoffice=request.form['msoffice']
        
        
        # print("My Data >>>>>>>>>>>>>", brand_name,age,owner,power,kms_driven)

    # brand,processor_brand,processor_name,processor_gnrtn,ram_gb,ram_type,ssd,hdd,os,os_bit,graphic_card_gb,warranty,Touchscreen,msoffice {% endcomment %}


        brand_dict={'ASUS':1, 'Lenovo':2, 'acer':3, 'Avita':4, 'HP':5, 'DELL':6, 'MSI':7,'APPLE':8}
        processor_brand_dict={'Intel':1, 'AMD':2, 'M1':3}
        processor_name_dict={'Celeron Dual':1,'Core i3':2,'Core i5':3,'Core i7':4,'Core i9':5,'M1':6,
                      'Pentium Quad':7,'Ryzen 3':8,'Ryzen 5':9,'Ryzen 7':10,'Ryzen 3':11}
        processor_gnrtn_dict={'4th':1, '7th':2, '8th':3, '9th':4, '10th':5, '11th':6, '12th':7,
       'Not Available':8} 
        ram_gb_dict={'4 GB':1,
                     '8 GB':2,
                     '16 GB':3,
                     '32 GB':4}
        ram_type_dict={'DDR3':1, 'DDR4':2, 'DDR5':3, 'LPDDR3':4, 'LPDDR4':5, 'LPDDR4X':6}
        ssd_dict={'0 GB':1, '128 GB':2, '256 GB':3, '512 GB':4, '1024 GB':5, '2048 GB':6,
                    '3072 GB':7}
        hdd_dict={'1024 GB':1, '0 GB':2, '512 GB':3, '2048 GB':4}
        os_dict={'Windows':1, 'DOS':2, 'Mac':3}
        os_bit_dict={'32 bit':1,'64 bit':2}
        graphic_card_gb_dict={'0 GB':1, '2 GB':2, '4 GB':3, '6 GB':4, '8 GB':5}
        warranty_years={'No warranty':1, '1 year':2, '2 years':3,'3 years':4}
        
        
        
        brand_name = brand_dict[brand_name]
        processor_brand = processor_brand_dict[processor_brand]
        processor_name = processor_name_dict[processor_name] 
        processor_gnrtn = processor_gnrtn_dict[processor_gnrtn]
        ram_gb=ram_gb_dict[ram_gb]
        ram_type=ram_type_dict[ram_type]
        ssd=ssd_dict[ssd]
        hdd=hdd_dict[hdd]
        os=os_dict[os]
        os_bit=os_bit_dict[os_bit]
        graphic_card_gb=graphic_card_gb_dict[graphic_card_gb]
        warranty=warranty_years[warranty]
        Touchscreen = 1 if request.form['Touchscreen'] == 'Yes' else 0
        msoffice = 1 if request.form['msoffice'] == 'Yes' else 0


        
        
        
        lst = [[brand_name,processor_brand,processor_name,processor_gnrtn,ram_gb,ram_type,
                ssd,hdd,os,os_bit,graphic_card_gb,warranty,Touchscreen,msoffice]]
        
        prediction = model.predict(lst)
        rounded_prediction = round(prediction[0], 2)
        with open("prediction_history.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([rounded_prediction, brand_name, processor_brand, processor_name, processor_gnrtn, ram_gb,
                     ram_type, ssd, hdd, os, os_bit, graphic_card_gb, warranty, Touchscreen, msoffice])

        
        print("prediction:-", prediction)
        
        # Pass back the input values so they stay in the form after submit
        
        return render_template('project.html', prediction=rounded_prediction, 
            brand_name=request.form['brand_name'],
            processor_brand=request.form['processor_brand'],
            processor_name=request.form['processor_name'],
            processor_gnrtn=request.form['processor_gnrtn'],
            ram_gb=request.form['ram_gb'],
            ram_type=request.form['ram_type'],
            ssd=request.form['ssd'],
            hdd=request.form['hdd'],
            os=request.form['os'],
            os_bit=request.form['os_bit'],
            graphic_card_gb=request.form['graphic_card_gb'],
            warranty=request.form['warranty'],
            Touchscreen=request.form['Touchscreen'],
            msoffice=request.form['msoffice'])

    return render_template('project.html')


#     brand_dict= dt2[brand_name]
#     data = [[brand_name,owner,age,power,kms_driven]]
    


if __name__ == "__main__":
    app.run(debug = True)