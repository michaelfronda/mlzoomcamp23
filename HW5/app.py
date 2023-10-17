

import pickle
from flask import Flask, request, jsonify

# Load model and dv
with open("dv.bin.1", "rb") as f_in: 
    dv = pickle.load(f_in)
    
with open("model1.bin.1", "rb") as f_in: 
    model = pickle.load(f_in)

# instantiate
app = Flask('credict_service')

@app.route('/predict', methods=['POST']) # HTTP Request: Post 
def predict():
    # Get data 
    data = request.get_json()

    # Extract features
    X = dv.transform([data])
    
    # Make prediction 
    y_pred = model.predict_proba(X)[0, 1]
    credit = y_pred >= 0.5

    return jsonify({'prob': float(y_pred), 'pred': bool(credit)}) # cast 

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)

