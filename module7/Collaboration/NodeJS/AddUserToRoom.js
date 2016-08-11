var request = require("request");

var options = { method: 'POST',
  url: 'https://api.ciscospark.com/v1/memberships',
  headers: 
   { 'postman-token': 'a05472ec-0f7f-3f31-6657-378aa9b453d1',
     'cache-control': 'no-cache',
     'content-type': 'application/json',
     authorization: 'Bearer NTIyN2U5NGQtY2JjZi00NGYxLWE0OTMtYzMwYTY3OWQzMDljOGE0YzA3ZTctNjY1' },
  body: 
   { roomId: 'Y2lzY29zcGFyazovL3VzL1JPT00vMzRjNTExZTAtNWIzYS0xMWU2LTlmNTgtYzcwMGY5YjM0YWFl',
     personEmail: 'twittbrod@gmail.com',
     isModerator: false },
  json: true };

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
