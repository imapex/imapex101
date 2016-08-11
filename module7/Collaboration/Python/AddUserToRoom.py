import requests

url = "https://api.ciscospark.com/v1/memberships"

payload = "{\n  \"roomId\" : \"Y2lzY29zcGFyazovL3VzL1JPT00vMzRjNTExZTAtNWIzYS0xMWU2LTlmNTgtYzcwMGY5YjM0YWFl\",\n  \"personEmail\" : \"twittbrod@gmail.com\",\n  \"isModerator\" : false\n}"
headers = {
    'authorization': "Bearer NTIyN2U5NGQtY2JjZi00NGYxLWE0OTMtYzMwYTY3OWQzMDljOGE0YzA3ZTctNjY1",
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "f253c29e-8987-1e05-976d-ceab2ff2f4de"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)