import requests

url = "https://api.ciscospark.com/v1/memberships"

payload = "{\n  \"roomId\" : \"<room ID>\",\n  \"personEmail\" : \"twittbrod@gmail.com\",\n  \"isModerator\" : false\n}"
headers = {
    'authorization': "Bearer <your token>",
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "f253c29e-8987-1e05-976d-ceab2ff2f4de"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)