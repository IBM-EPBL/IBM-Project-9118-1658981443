
import requests
import json
API_KEY = "iFY0zXPpW9WAKkEngxaszWLAMJARuVJzMZgH53lU3o7o"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [['Gender','Married','Dependents','Education','Self_Employed','ApplicantIncome','CoapplicantIncome','LoanAmount','Loan_Amount_Term','Credit_History','Property_Area']], 
                                   "values": [[1,1,0,0,0,4000,1000,120,360,0,0]]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/e858e595-92ed-44da-ba4a-f33d452c403c/predictions?version=2022-11-19', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())
predictions=response_scoring.json()
pred=predictions['predictions'][0]['values'][0][0]

if(pred==0):
    print("Loan Not Approved")
else:
    print("Loan Approved")    