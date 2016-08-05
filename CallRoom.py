import requests

url = "https://api.tropo.com/1.0/sessions"

querystring = {"action":"create","token":"58457a4f4a58704e687873666f41524e6b747778796576767845726755504d71586143414e76695347625167","numbertodial":"86879050@ciscospark.com"}

headers = {
    'cache-control': "no-cache",
    'postman-token': "73dad72f-0962-de88-8701-73557b38315b"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)