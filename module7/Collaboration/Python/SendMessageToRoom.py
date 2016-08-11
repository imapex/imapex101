import requests

url = "https://api.ciscospark.com/v1/messages"

payload = "{\n  \"roomId\": \"<room ID>\",\n  \"file\": \"https://developer.cisco.com/images/spark/spark-logo.png\",\n  \"text\": \"Welcome to Spark!\"\n}"
headers = {
    'authorization': "Bearer <your token>",
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "428367e9-d44a-8015-079d-a9f9561a2664"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)