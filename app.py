from flask import Flask,request, make_response
import json
import requests

app= Flask(__name__)

@app.route('/webhook',methods=["POST"])
def webhook():
    req= request.get_json(silent=True,force=True)
    print(json.dumps(req, indent=4))
    res = Currency_conversion(req)
    res = json.dumps(res, indent=4)
   
    a = make_response(res)
    a.headers['Content-Type'] = 'application/json'
    return a

def Currency_conversion(req):
    result= req.get('queryResult')
    paramters= result.get('parameters')
    currency= paramters.get('currency-name')
    
    unit_currency=paramters.get('unit-currency').get('amount')
    currency_name=paramters.get('unit-currency').get('currency')

    
   
    url = "https://api.apilayer.com/currency_data/convert?to="+str(currency_name)+"&from="+str(currency)+"&amount="+str(unit_currency)

    payload = {}
    headers= {
    "apikey": "EZiqhj9tqca6RYmxnmAWS7Vi6FlAaWMO"    
    }

    response = requests.request("GET", url, headers=headers, data = payload)

   
    result = response.json()

    print("----------------------------------------------")
    print(result)
   
    data=result['query']
    other=data['from']
    other1=data['to']
    other2=data['amount']
    quote=result['result']
    

    speech=("The conversion of " + str( other2) + str( other) + " in " + str(other1) + " is " + str(quote))
   
    return {
        "fulfillmentText": speech
    }
    




if __name__ == "__main__":
    app.run(debug=True)
