import requests

url = "https://api.ciscospark.com/v1/messages/Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOWY0Y2E1NTAtNWIzYS0xMWU2LWE5OTMtNzM3YjNhZWMwMmM5"

headers = {
    'authorization': "Bearer NTIyN2U5NGQtY2JjZi00NGYxLWE0OTMtYzMwYTY3OWQzMDljOGE0YzA3ZTctNjY1",
    'content-type': "application/json; charset=utf-8",
    'cache-control': "no-cache",
    'postman-token': "4cb38dbb-0528-b310-121b-c5d3d6392d4d"
    }

response = requests.request("DELETE", url, headers=headers)

print(response.text)