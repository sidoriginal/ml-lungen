from flask import Flask,request,jsonify
import numpy as np
import pickle
model = pickle.load(open('model.pkl','rb'))
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello world"
@app.route('/predict',methods=['POST'])
def predict():
    gender= request.form.get('gender')
    age = request.form.get('age')
    smoke = request.form.get('smoke')
    yellow = request.form.get('yellow')
    anxiety= request.form.get('anxiety')
    peer = request.form.get('peer')
    chronic = request.form.get('chronic')
    fatigue = request.form.get('fatigue')
    allergy = request.form.get('allergy')
    wheezing = request.form.get('wheezing')
    alcohol = request.form.get('alcohol')
    cough = request.form.get('cough')
    breath = request.form.get('breath')
    swallow = request.form.get('swallow')
    chest = request.form.get('chest')
    Ma=""
    Fe=""
    if(gender=='M'):
        Ma="1"
        Fe="0"
    else:
        Fe="1"
        Ma="1"
    input_query = np.array([[Fe,Ma,age,smoke,yellow,anxiety,peer,chronic,fatigue,allergy,wheezing,alcohol,cough,breath,swallow,chest]])
    result = model.predict(input_query)[0]
    return jsonify({'cancer':str(result)})
if __name__ == '__main__':
    app.run(debug=True)