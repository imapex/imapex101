import requests

url = "https://api.ciscospark.com/v1/messages"

querystring = {"roomId":"Y2lzY29zcGFyazovL3VzL1JPT00vYTliZTQyZTAtMzY3OS0xMWU2LTliNmItZTcxYjVhMmYyMzEy"}

headers = {
    'content-type': "application/json; charset=utf-8",
    'authorization': "Bearer NTIyN2U5NGQtY2JjZi00NGYxLWE0OTMtYzMwYTY3OWQzMDljOGE0YzA3ZTctNjY1",
    'cache-control': "no-cache",
    'postman-token': "a080dc60-da23-c605-c0ca-052d55ff5858"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)