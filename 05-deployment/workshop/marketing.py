import requests

url = 'http://localhost:9696/predict'

customer = {
    "gender": "male",
    "seniorcitizen": 0,
    "partner": "no",
    "dependents": "yes",
    "phoneservice": "no",
    "multiplelines": "no_phone_service",
    "internetservice": "dsl",
    "onlinesecurity": "no",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
    "tenure": 6,
    "monthlycharges": 29.85,
    "totalcharges": 129.85,
}

response = requests.post(url, json=customer)
response_data = response.json()

print(f"Response from the prediction service: {response_data}")

if response_data['churn'] >= 0.5:
    print(f'Send an email to the customer with a special offer') 
    # Code to send email
else:
    print(f'Action not needed')
    # Code to log the customer information for future reference