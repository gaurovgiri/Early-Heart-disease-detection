import pickle
from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

# load the model
filename = r'model/heart_disease.pkl'
model = pickle.load(open(filename, 'rb'))

@app.route("/")
def home():
    return render_template('/index.html')


@app.route("/result", methods=["POST"])
def submit():
    age = int(request.form['age'])
    sex = int(request.form['sex'] == "male")
    cp = int(request.form['cp'])
    trtbps = int(request.form['trtbps'])
    chol = int(request.form['chol'])
    restecg = int(request.form['restecg'])
    thalachh = int(request.form['thalachh'])
    exng = int(request.form['exng'])
    oldpeak = float(request.form['oldpeak'])
    slp = int(request.form['slp'])
    caa = int(request.form['caa'])
    thall = int(request.form['thall'])
    o2Saturation = float(request.form['o2Saturation'])

    data = np.array([age,sex,cp,trtbps,chol,restecg,thalachh,exng,oldpeak,slp,caa,thall,o2Saturation])
    output = model.predict([data])[0]
    print(output)

    if output == 0:
        return render_template("/result.html", result="Not Risky")
    else:
        return render_template("/result.html", result="Risky")



if __name__ == '__main__':
    app.run(debug=True,user_reloader=True)
