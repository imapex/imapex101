var request = require("request");

var options = { method: 'GET',
  url: 'https://api.tropo.com/1.0/sessions',
  qs: 
   { action: 'create',
     token: '<your Tropo app token>',
     numbertodial: '<your Spark room URI>' },
  headers: 
   { 'postman-token': '21bcef21-2858-ee62-97a9-5f0634c63524',
     'cache-control': 'no-cache' } };

request(options, function (error, response, body) {
  if (error) throw new Error(error);

  console.log(body);
});
