import requests
import json

headers = {"Content-Type":"application/json", "Accept":"*/*"}

datas = {"client_id":"YOUR_CLIENT_ID", "client_secret":"YOUR_CLIENT_SECRET", "grant_type":"client_credentials"}
datas = json.dumps(datas)

#making authorization
r = requests.post("https://openapi.airtel.africa/auth/oauth2/token", headers=headers, data=datas)
print(r.json())
access_token = r.json()['access_token']

#cheking ballance
def check_balance(token):
    headers = {"Accept":"*/*", "X-Country":"TZ", "X-Currency":"TZS","Authorization": f"{token}"}
    print(headers)
    r = requests.get('https://openapi.airtel.africa/standard/v1/users/balance', headers = headers)
    print(r.text)

#pust ussd to customer
def push_merchant(token):
    headers = {"Content-Type":"application/json", "Accept": "*/*", "X-Country":"TZ", "X-Currency":"TZS", "Authorization":f"{token}"}
    print(headers)
    data = {"reference":"123456789", "subscriber":{"country":"TZ", "currency":"TZS", "msisdn":"684049052"}, "transaction":{"amount":100, "country":"TZ", "currency":"TZS", "id":"12345567890"}}
    data = json.dumps(data)
    print(data)
    r = requests.post('https://openapi.airtel.africa/merchant/v1/payments/', headers = headers, data=data)
    print(r.json())



push_merchant(access_token)

#check balance after payment is done
check_balance(access_token)
