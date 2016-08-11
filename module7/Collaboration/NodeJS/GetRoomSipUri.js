var request = require("request");

var options = { method: 'GET',
  url: 'https://api.ciscospark.com/v1/rooms/Y2lzY29zcGFyazovL3VzL1JPT00vMzRjNTExZTAtNWIzYS0xMWU2LTlmNTgtYzcwMGY5YjM0YWFl',
  qs: { showSipAddress: 'true' },
  headers: 
   { 'postman-token': '1379109c-869c-6260-63aa-7ba614e9250e',
     'cache-control': 'no-cache',
     authorization: 'Bearer NTIyN2U5NGQtY2JjZi00NGYxLWE0OTMtYzMwYTY3OWQzMDljOGE0YzA3ZTctNjY1' },
  body: '{\n  "showSipAddress": "true"\n}' };

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
