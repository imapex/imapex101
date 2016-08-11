import requests

url = "https://api.tropo.com/1.0/sessions"

querystring = {"action":"create","token":"<your Tropo App token>","numbertodial":"<your Spark room URI>"}

headers = {
    'cache-control': "no-cache",
    'postman-token': "73dad72f-0962-de88-8701-73557b38315b"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)