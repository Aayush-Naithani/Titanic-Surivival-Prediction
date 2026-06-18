from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np
import pandas as pd


# load the trrained model
model_path = "pipe.pkl"
with open(model_path, "rb") as file:
 model = pickle.load(file)

app = Flask(__name__)

@app.route("/",methods=["GET"])
def home():
 return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    data = pd.DataFrame({
        "Pclass": [int(request.form["Pclass"])],
        "gender": [request.form["gender"]],
        "Age": [float(request.form["Age"])],
        "SibSp": [int(request.form["SibSp"])],
        "Parch": [int(request.form["Parch"])],
        "Fare": [float(request.form["Fare"])],
        "Embarked": [request.form["Embarked"]]
    })

    prediction = model.predict(data)

    result = "Survived" if prediction[0] == 1 else "Did Not Survive"

    return result

if __name__ == "__main__":
 app.run(debug=True)