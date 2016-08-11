import requests

url = "https://api.ciscospark.com/v1/messages"

payload = "{\n  \"roomId\": \"Y2lzY29zcGFyazovL3VzL1JPT00vMjljMzA0NTAtY2FjNi0xMWU1LWE3NDgtNTNlYzZjNjcyYWJl\",\n  \"file\": \"https://developer.cisco.com/images/spark/spark-logo.png\",\n  \"text\": \"Welcome to Spark!\"\n}"
headers = {
    'authorization': "Bearer NTIyN2U5NGQtY2JjZi00NGYxLWE0OTMtYzMwYTY3OWQzMDljOGE0YzA3ZTctNjY1",
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "428367e9-d44a-8015-079d-a9f9561a2664"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)