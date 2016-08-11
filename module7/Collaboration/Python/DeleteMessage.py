import requests

url = "https://api.ciscospark.com/v1/messages/<message ID>"

headers = {
    'authorization': "Bearer <your token>",
    'content-type': "application/json; charset=utf-8",
    'cache-control': "no-cache",
    'postman-token': "4cb38dbb-0528-b310-121b-c5d3d6392d4d"
    }

response = requests.request("DELETE", url, headers=headers)

print(response.text)