var request = require("request");

var options = { method: 'POST',
  url: 'https://api.ciscospark.com/v1/memberships',
  headers: 
   { 'postman-token': 'a05472ec-0f7f-3f31-6657-378aa9b453d1',
     'cache-control': 'no-cache',
     'content-type': 'application/json',
     authorization: 'Bearer <your token>' },
  body: 
   { roomId: '<room ID>',
     personEmail: 'twittbrod@gmail.com',
     isModerator: false },
  json: true };

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
