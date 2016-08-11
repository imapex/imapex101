var request = require("request");

var options = { method: 'GET',
  url: 'https://api.ciscospark.com/v1/rooms/<room ID>',
  qs: { showSipAddress: 'true' },
  headers: 
   { 'postman-token': '1379109c-869c-6260-63aa-7ba614e9250e',
     'cache-control': 'no-cache',
     authorization: 'Bearer <your token>' },
  body: '{\n  "showSipAddress": "true"\n}' };

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
