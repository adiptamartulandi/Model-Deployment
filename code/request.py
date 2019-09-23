import requests

# URL
url = 'http://localhost:5000/api'

# Change the value of experience that you want to test
r = requests.post(url,json={'LIMIT_BAL':30000,
                            'MARRIAGE':1,
                            'EDUCATION':1,
                            'SEX':2,
                            'AGE':40,
                            'PAY_1':0,
                            'PAY_2':0,
                            'PAY_3':3,
                            'BILL_AMT1':24607,
                            'BILL_AMT2':24430,
                            'BILL_AMT3':23881,
                            'PAY_AMT1':1700,
                            'PAY_AMT2':1600,
                            'PAY_AMT3':1287})
print(r.json())
