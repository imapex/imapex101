var request = require("request");

var options = { method: 'GET',
  url: 'https://api.ciscospark.com/v1/messages',
  qs: { roomId: 'Y2lzY29zcGFyazovL3VzL1JPT00vYTliZTQyZTAtMzY3OS0xMWU2LTliNmItZTcxYjVhMmYyMzEy' },
  headers: 
   { 'postman-token': 'c850d810-4350-9012-ded1-6e23fd28f5cc',
     'cache-control': 'no-cache',
     authorization: 'Bearer NTIyN2U5NGQtY2JjZi00NGYxLWE0OTMtYzMwYTY3OWQzMDljOGE0YzA3ZTctNjY1',
     'content-type': 'application/json; charset=utf-8' } };

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
