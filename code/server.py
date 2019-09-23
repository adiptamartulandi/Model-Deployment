# Create API of ML model using flask

'''
This code takes the JSON data while POST request an performs the prediction using loaded model and returns
the results in JSON format.
'''

# Import libraries
import numpy as np
from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open('random_forest_model.pkl','rb'))

@app.route('/api', methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)

    # Make prediction using model loaded from disk as per the data.
    prediction = model.predict([np.array([data['LIMIT_BAL'], data['MARRIAGE'], data['EDUCATION'], data['SEX'], data['AGE'], data['PAY_1'], data['PAY_2'], data['PAY_3'], data['BILL_AMT1'], data['BILL_AMT2'], data['BILL_AMT3'], data['PAY_AMT1'], data['PAY_AMT2'], data['PAY_AMT3']])])

    # Take the first value of prediction
    output = int(prediction[0])

    return jsonify(output)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
