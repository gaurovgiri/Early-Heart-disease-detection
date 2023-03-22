import pickle
from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

# load the model
filename = r'logistic_regression_model.sav'
model = pickle.load(open(filename, 'rb'))

@app.route("/")
def hello_world():
	return render_template('/index.html')

@app.route("/submit", methods = ["POST"])
def submit():
	if request.method == "POST":
		age = int(request.form["age"])
		
		if request.form["sex"] == "Male":
			sex = 1
		else:
			sex = 0
		
		if request.form['cp'] == 'Typical angina':
			cp = 0
		elif request.form['cp'] == 'Atypical angina':
			cp = 1
		elif request.form['cp'] == 'Non-angina':
			cp = 2
		else:
			cp = 3

		trtbps = int(request.form['trtbps'])

		chol = int(request.form['chol'])

		if request.form['fbs'] == 'True':
			fbs = 1
		else:
			fbs = 0
		
		if request.form['restecg'] == 'Normal':
			restecg = 0
		elif request.form['restecg'] == 'Having ST-T wave abnormality':
			restecg = 1
		else:
			restecg = 2

		thalachh = int(request.form['thalachh'])

		if request.form['exng'] == 'Yes':
			exng = 1
		else:
			exng = 0
		
		oldpeak = float(request.form['oldpeak'])

		if request.form['slp'] == "Unsloping":
			slp = 0
		elif request.form['slp'] == "Flat":
			slp = 1
		else:
			slp = 2

		caa = int(request.form['caa'])

		if request.form['thall'] == 'NULL or no information':
			thall = 0
		elif request.form['thall'] == 'Normal blood flow observed':
			thall = 0
		elif request.form['thall'] == 'Blood flow observed but it is considered to be a defect':
			thall = 0
		else:
			thall = 3
		
		input_list = [age, sex, cp, trtbps, chol, fbs, restecg, thalachh, exng, oldpeak, slp, caa, thall]
		input_array = np.array([input_list])
		print(type(input_array[0]))
		print(input_array)
	return render_template("/submit.html", n = model.predict(input_array))
if __name__ == '__main__':
	app.run(debug=True)
	
