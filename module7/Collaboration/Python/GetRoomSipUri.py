import requests

url = "https://api.ciscospark.com/v1/rooms/Y2lzY29zcGFyazovL3VzL1JPT00vMzRjNTExZTAtNWIzYS0xMWU2LTlmNTgtYzcwMGY5YjM0YWFl"

querystring = {"showSipAddress":"true"}

payload = "{\n  \"showSipAddress\": \"true\"\n}"
headers = {
    'authorization': "Bearer NTIyN2U5NGQtY2JjZi00NGYxLWE0OTMtYzMwYTY3OWQzMDljOGE0YzA3ZTctNjY1",
    'cache-control': "no-cache",
    'postman-token': "8386370d-5a45-f517-b347-10577b58f4f6"
    }

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)