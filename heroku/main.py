from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import uvicorn
import sklearn

app = FastAPI()
model = joblib.load("trained_classifier.joblib")
modeliris = joblib.load("irisclassifier.joblib")

class Tweet(BaseModel):
    tweet = str

class Iris(BaseModel):
    sepal_length = float
    sepal_width = float
    petal_length = float
    petal_width = float

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/tweet")
def class_tweet(txt:Tweet): 
    if (txt.tweet) :
        Y_pred = model.predict_proba(vars()[txt.tweet])[0]

        if Y_pred[0] > Y_pred[1] and Y_pred[0]> Y_pred[2]:
            return("hate_speech")
        elif Y_pred[1] > Y_pred[0] and Y_pred[1]> Y_pred[2] :
            return("offensive_language")
        else :
            return("neither")

@app.post("/iris")
def classiris(iris:Iris):
    X = pd.DataFrame({
    'sepal_length': [iris.sepal_length],
    'sepal_width': [iris.sepal_width],
    'petal_length': [iris.petal_length],
    'petal_width': [iris.petal_width]
    })
    Y_pred = model.predict_proba(X)[0]
    

    if Y_pred[0] > Y_pred[1] and Y_pred[0]> Y_pred[2]:
        return 'setosa'
    elif Y_pred[1] > Y_pred[0] and Y_pred[1]> Y_pred[2] :
        return 'versicolor'
    else :
        return 'virginica'


if __name__ == '__main__' :
    uvicorn.run(app,host="https://fastapimazouzi.herokuapp.com/",port="8000")