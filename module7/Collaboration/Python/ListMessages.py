import requests

url = "https://api.ciscospark.com/v1/messages"

querystring = {"roomId":"<room ID>"}

headers = {
    'content-type': "application/json; charset=utf-8",
    'authorization': "Bearer <your token>",
    'cache-control': "no-cache",
    'postman-token': "a080dc60-da23-c605-c0ca-052d55ff5858"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)