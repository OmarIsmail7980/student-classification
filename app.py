from flask import Flask, render_template, request
import pickle
import numpy as np


app = Flask(__name__)

model = pickle.load(open('model.plk', 'rb'))


@app.route("/")
def home(): 
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def predict():
    math_score = request.form['math_score']
    reading_score = request.form['reading_score']
    writing_score = request.form['writing_score']
    lunch = request.form['lunch']
    parental_education = request.form['parental_education']
   
    
    arr = np.array([[math_score,reading_score,writing_score,lunch,
                     parental_education]])
    
    prediction=model.predict(arr)
    
    if(prediction==1):
        return render_template("index.html", prediction_text= "You are a female Student")
    else:
        return render_template("index.html", prediction_text= "You are a Male Student")
        
    
if __name__=="__main__":
    app.run(debug=True)
    