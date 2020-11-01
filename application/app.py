from flask import Flask, render_template, request
import joblib

# __name__ is equal to app.py
app = Flask(__name__)

# load model from model.pck
model = joblib.load('model.pkl')



@app.route("/")
def home():
    return render_template('index.html')



@app.route("/predict", methods=["POST"])
def predict():
	temperature =  request.form['Temperature']
	pressure =  request.form['Pressure']
	humidity =  request.form['Humidity']
	windDirection =  request.form['WindDirection_D']
	speed =  request.form['Speed']
	dayOfYear =  request.form['DayOfYear']
	timeOfDay =  request.form['TimeOfDay_s']

	radiation_amount = round((model.predict([[temperature,pressure, humidity, windDirection, speed, dayOfYear, timeOfDay]])[0]),2)
	return render_template("index.html", radiation_amount=radiation_amount)	




if __name__ == "__main__":
    app.run()
