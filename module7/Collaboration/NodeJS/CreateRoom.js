var request = require("request");

var options = { method: 'POST',
  url: 'https://api.ciscospark.com/v1/rooms',
  headers: 
   { 'postman-token': '7ec3398f-f8c4-8c0b-c6a5-9fdc16af061b',
     'cache-control': 'no-cache',
     'content-type': 'application/json',
     authorization: 'Bearer NTIyN2U5NGQtY2JjZi00NGYxLWE0OTMtYzMwYTY3OWQzMDljOGE0YzA3ZTctNjY1' },
  body: { title: 'API Created Room' },
  json: true };

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
