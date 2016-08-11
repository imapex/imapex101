var request = require("request");

var options = { method: 'DELETE',
  url: 'https://api.ciscospark.com/v1/messages/Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOWY0Y2E1NTAtNWIzYS0xMWU2LWE5OTMtNzM3YjNhZWMwMmM5',
  headers: 
   { 'postman-token': 'fd0a5c82-05db-6a76-f84a-ac3dad042edb',
     'cache-control': 'no-cache',
     'content-type': 'application/json; charset=utf-8',
     authorization: 'Bearer NTIyN2U5NGQtY2JjZi00NGYxLWE0OTMtYzMwYTY3OWQzMDljOGE0YzA3ZTctNjY1' } };

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
