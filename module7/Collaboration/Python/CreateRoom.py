import requests

url = "https://api.ciscospark.com/v1/rooms"

payload = "{\n    \"title\": \"API Created Room\"\n}\n"
headers = {
    'authorization': "Bearer NTIyN2U5NGQtY2JjZi00NGYxLWE0OTMtYzMwYTY3OWQzMDljOGE0YzA3ZTctNjY1",
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "f3bb525f-f875-5e61-ab96-02472ae8dc11"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)