var request = require("request");

var options = { method: 'DELETE',
  url: 'https://api.ciscospark.com/v1/messages/<message ID>',
  headers: 
   { 'postman-token': 'fd0a5c82-05db-6a76-f84a-ac3dad042edb',
     'cache-control': 'no-cache',
     'content-type': 'application/json; charset=utf-8',
     authorization: 'Bearer <your token>' } };

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
