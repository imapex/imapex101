import requests

url = "https://api.ciscospark.com/v1/rooms/<room ID>"

querystring = {"showSipAddress":"true"}

payload = "{\n  \"showSipAddress\": \"true\"\n}"
headers = {
    'authorization': "Bearer <your token>",
    'cache-control': "no-cache",
    'postman-token': "8386370d-5a45-f517-b347-10577b58f4f6"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)