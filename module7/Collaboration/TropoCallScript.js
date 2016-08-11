// outbound call
//call("sip:timwittb@cisco.com;transport=tcp”);
//call("sip:"+"timwittb@cisco.com");
call("sip:"+numbertodial,{callerID:'9999999999'});
//conference("9999");
wait(60000);