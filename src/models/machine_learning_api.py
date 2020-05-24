from flask import Flask,request
import pandas as pd
import numpy as np
import json 
import pickle
import os

app=Flask(__name__)
model_file_path=os.path.join(os.path.pardir,os.path.pardir,'models','lr_model.pkl')
scaler_file_path=os.path.join(os.path.pardir,os.path.pardir,'models','lr_scaler.pk1')

with open(model_file_path, 'rb') as f:
    model_loaded= pickle.load(f)
with open(scaler_file_path, 'rb') as f:
    scaler_loaded=pickle.load(f)


@app.route('/api',methods=['POST'])
def make_prediction():
    data =json.dumps(request.get_json(force=True))
    df=pd.read_json(data)
    passenger_ids=df['PassengerId'].ravel()
    actuals=df['Survived'].ravel()
    columns_name=[]
    for i in df.columns:
        columns_name.append(i)
    columns_name.remove('PassengerId')
    columns_name.remove('Survived')
    
    X=df[columns_name].values.astype('float')
    X_scaled=scaler_loaded.transform(X)
    predictions=model_loaded.predict(X_scaled)
    df_response = pd.DataFrame({'PassengerId':passenger_ids,'Predicted':predictions,'Actial':actuals})
    return df_response.to_json()

if __name__== '__main__':
    app.run(port=10001,debug=True)
