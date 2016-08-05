var request = require("request");

var options = { method: 'POST',
  url: 'https://api.ciscospark.com/v1/messages',
  headers: 
   { 'postman-token': 'ecf97bb1-2329-26a4-11ef-fbec4d6f8dff',
     'cache-control': 'no-cache',
     'content-type': 'application/json',
     authorization: 'Bearer NTIyN2U5NGQtY2JjZi00NGYxLWE0OTMtYzMwYTY3OWQzMDljOGE0YzA3ZTctNjY1' },
  body: 
   { roomId: 'Y2lzY29zcGFyazovL3VzL1JPT00vMjljMzA0NTAtY2FjNi0xMWU1LWE3NDgtNTNlYzZjNjcyYWJl',
     file: 'https://developer.cisco.com/images/spark/spark-logo.png',
     text: 'Welcome to Spark!' },
  json: true };

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
