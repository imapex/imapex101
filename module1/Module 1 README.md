[Class Contents](../README.md)

# Module 1: General Development Skills

* 12 Factor Concepts
  * Secret Management
* Basic Linux Tools
  * curl
  * bash scripts
  * awk
  * grep
  * sed
* Markdown
* Vagrant
* OpenSource Licenses
* Extra Python Skills
  * Virtual Environments
  * pip and dependencies
* Writing and Using Test Cases
* Linting
* Boiler Plate Application
  * README.md
  * license
  * hello_world.py
  * test cases
  * requirements.txt
  * Dockerfile
  * Vagrantfile
  * .drone.yml
  * drone-secrets-sample.yml

# 12 Factor Concepts

## What is a "12 Factor" App and where did it come from

The 12 Factor Application is a methodology proposed in the early 2010s by core members of the Heroku team.  It is a well circulated and read proposal that focuses on "Cloud Native" application design concepts, however it is not perfect or univerally accepted.  Most will agree that it provides an ideal to strive towards, and a _violation_ of a factor should be done consciously and with reason.  

It is not the only _manifesto_ on Cloud Native development, but it is worth having exposure and understanding of.  

Full details at [12Factor.net](http://12factor.net) 

## The Factors 

### I. [Codebase](http://12factor.net/codebase)
One codebase tracked in revision control, many deploys

### II. [Dependencies](http://12factor.net/dependencies)
Explicitly declare and isolate dependencies

### III. [Config](http://12factor.net/config)
Store config in the environment

### IV. [Backing services](http://12factor.net/backing-services)
Treat backing services as attached resources

### V. [Build, release, run](http://12factor.net/build-release-run)
Strictly separate build and run stages

### VI. [Processes](http://12factor.net/processes)
Execute the app as one or more stateless processes

### VII. [Port binding](http://12factor.net/port-binding)
Export services via port binding

### VIII. [Concurrency](http://12factor.net/concurrency)
Scale out via the process model

### IX. [Disposability](http://12factor.net/disposability)
Maximize robustness with fast startup and graceful shutdown

### X. [Dev/prod parity](http://12factor.net/dev-prod-parity)
Keep development, staging, and production as similar as possible

### XI. [Logs](http://12factor.net/logs)
Treat logs as event streams

### XII. [Admin processes](http://12factor.net/admin-processes)
Run admin/management tasks as one-off processes

## A Stateless Aspiration

The 12 Factor Application describes a goal of a **stateless application**.  The refers to the goal that applications (and their components) should be able to come and go without any overall impact to the user or data.  This is core to the ablity to be fully "cloud native" and drive towards fully automated operations and portablity.  

This is a great target goal, and for many applications, or microservices within an application, it is useful and practical.  But as an overall strategy it has some significant problems that are important to be aware of.  

### Where's the data?

Nearly every application of significance has a need to gather, manipulate, store, and report on data.  At it's core, the 12 Factor principals do not accomidate for how to deal with data. 


## Why do we Care? 

Software development is like any other area of IT.  There are basic capabilities and technologies, then there are strategies for using them.  When we want to be relevant to network engineers, we study strategies and design with "3 Tier Network Architectures" and more recently "Spine-Leaf" in mind.  When we want to be relevant to software developers, we need to understand the common practices and methods to engage in discussions.  

## A sidebar on "Secrets"

In development a "secret" can loosely be defined as anything you wouldn't want everyone else in the world to know.  This includes the obvious things like: 

* Passwords 
* Authentication Tokens
* Usernames 
* Credit Card
* Account Information 

But it can also include things that aren't as directly damaging if they are lost such as: 

* Application and Server Names 
* API Endpoints and addresses 
* Email Addresses 
* IP Addresses and Port Numbers
* Domain Names 
* just about anythind descriptive about your environment... 

Factor III: Config talks about NOT including environment details in your code, but rather in the environment.  In many cases the "environment details" also qualify as **secrets** and you need to take care about how you are storing and transporting them throughout application development and deployment process.  It is very easy to commit secrets into a codebase (ie GitHub) and mistakeningly make your usernames and passwords publicly available on GitHub.  

* Example of what can happen: [$6,000 AWS Bill Overnight](https://wptavern.com/ryan-hellyers-aws-nightmare-leaked-access-keys-result-in-a-6000-bill-overnight)
* Handy reference on what to do: [Remove sensitve data from GitHub](https://help.github.com/articles/remove-sensitive-data/)

## Handy Links 

* [http://12factor.net](http://12factor.net)
* [http://pivotal.io/beyond-the-twelve-factor-app](http://pivotal.io/beyond-the-twelve-factor-app)
* [https://cncf.io](https://cncf.io)
* [https://en.wikipedia.org/wiki/Conway%27s_law](https://en.wikipedia.org/wiki/Conway%27s_law)
* [http://www.thepathtoagility.com/wp-content/uploads/2012/03/steveriley2.pdf](http://www.thepathtoagility.com/wp-content/uploads/2012/03/steveriley2.pdf)

# Basic Linux Tools

Some of the most difficult parts of developing are often less about coding, and more about operational tasks.  But sense the big theme in development these days is **Dev_Ops_** we can't get away from those tasks.  

Scripting has long been the swiss army knife for operations, and it continues to be valuable today.  There are several common Linux utilities that having a basic fundamental knowledge of will help you greatly as you work to develop and package your applications for others to use.  

## Example Prep

The following examples leverage the Weather.com API.  Developer access to the API is free and accounts can be created at [wunderground](https://www.wunderground.com/weather/api/).  You will need an API key to follow along with the examples.  

Once you have your API key, run this command at your command line to store your API key as a local environment variable.  

```
export WEATHER_API_KEY=<YOUR KEY>
```

The following examples will use the Cisco Spark API.  You'll need to have access to your Spark Developer Token to complete the exercises.  Find it at [developer.ciscospark.com](https://developer.ciscospark.com).  

Once you have your API key, run these commands at your command line to store your API key and some other details as a local environment variable.  

```
export SPARK_TOKEN=<YOUR TOKEN>
export MY_EMAIL=<YOUR EMAIL>
export PARTNER_EMAIL=<A LAB PARTNERS EMAIL>
```


## curl

curl is a general purpose command line utility for making requests to web servers.  It is often used for testing REST API calls, verifying a site is up and operational, or as part of bash scripts.  The number of potential arguments and options to curl can be mind-boggling, however knowing the following subset can be highly valuable as you get started.  

### Examples and Exercises 

* Basic curl request
  
  ```
  # List the Spark Teams you are a member of
  curl https://api.ciscospark.com/v1/teams
  
  # No data should be returned... 
  ```

* Inspect the HTTP Headers with `-v` to find out what happened... 
  
  ```
  curl -v https://api.ciscospark.com/v1/teams
  
	*   Trying 104.239.247.152...
	* Connected to api.ciscospark.com (104.239.247.152) port 443 (#0)
	* TLS 1.2 connection using TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384
	* Server certificate: *.ciscospark.com
	* Server certificate: Go Daddy Secure Certificate Authority - G2
	* Server certificate: Go Daddy Root Certificate Authority - G2
	> GET /v1/teams HTTP/1.1
	> Host: api.ciscospark.com
	> User-Agent: curl/7.43.0
	> Accept: */*
	>
	< HTTP/1.1 401 Unauthorized
	< Content-Length: 0
	< Date: Tue, 26 Jul 2016 20:32:26 GMT
	< Server: Redacted
	< Trackingid: NA_69b0048b-3bab-4175-a2c0-f9272ba99c2d
	< X-Cf-Requestid: 9b78f835-9d29-46a9-5211-27c5cf34f59e
	< Content-Type: text/plain; charset=utf-8
	<
	* Connection #0 to host api.ciscospark.com left intact  
  ```  
  * Lines beginning with `>` indicate outgoing **REQUEST** headers while those with `<` are for incoming **RESPONSE** headers
  * The first **RESPONSE** header `HTTP/1.1 401 Unauthorized` indicates the problem.  We are _Unauthorized_. 
  * Most APIs require authentication/authorization
* Cisco Spark, and many other services, use Request Headers to provide authenticaiton information.  
	* Set a Request Header with `-H "<Header-Name>: <Value>` argument.  Multiple `-H` arguments are supported.
	* OAUTH2 is a common mechanism used for authentication, and is used by Cisco Spark.  It leverages a Request Header called **Authorization** with a value of _Bearer \<TOKEN\>_

	```
	curl -H "Authorization: Bearer $SPARK_TOKEN" https://api.ciscospark.com/v1/teams	
	
	{"items":[{"id":"...","name":"MidW/A imapex","created":"2016-06-29T13:29:05.416Z"}]}
	```
* curl will simply write out the data as returned by the server, and it isn't always in a handy format, particularly when returned as raw JSON.  You can "pipe" JSON data to an included python module to make it more readable.  

	```
	curl -H "Authorization: Bearer $SPARK_TOKEN" https://api.ciscospark.com/v1/teams | python -m json.tool
	  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
	                                 Dload  Upload   Total   Spent    Left  Speed
	100   904  100   904    0     0    428      0  0:00:02  0:00:02 --:--:--   428
	{
	    "items": [
	        {
	            "created": "2016-06-29T13:29:05.416Z",
	            "id": "...",
	            "name": "MidW/A imapex"
	        }
	    ]
	}
	```  
* Some other sites leverage Basic Authenticaiton with usernames and passwords.  These can be used with curl using the `-u <username>:<password>` format.  
	
	```
	# Example using basic authentication with a ficticious site
	curl -u admin:password http://api.basicauth.com
	```
* You can capture the returned data (not headers, just data) using the `-o <file>` option to curl.  
	* _You can use `-o /dev/null` as a shortcut to drop any returned data if only interested in headers or testing_

	```
	curl -H "Authorization: Bearer $SPARK_TOKEN" https://api.ciscospark.com/v1/teams -o teams.json
	
	ls -l 	
	-rw-r--r--  1 user123  staff  904 Jul 26 15:49 teams.json
	
	```	
	
* If you want to capture the Headers to a file, use the `-D <file>` argument. 

	```
	curl -H "Authorization: Bearer $SPARK_TOKEN" https://api.ciscospark.com/v1/teams -D headers.txt
	
	ls -l
	total 16
	-rw-r--r--  1 user123  staff  296 Jul 26 16:10 headers.txt
	```

* By default curl sends an HTTP **GET** method.  To send other methods, use the `-X` option.  

	```
	curl -X POST -H "Authorization: Bearer $SPARK_TOKEN" https://api.ciscospark.com/v1/messages 
	
	{"message":"Required request body is missing","errors":[{"description":"Required request body is missing"}],"trackingId":"NA_c4d9d517-3617-4b6a-a521-dc2a26334dd6"}
	
	# When POSTING, you often have to include data, as the error message indicates
	```

* With curl you can send data to a server as part of an API request as well.  The `-d` flag is used, and several options exist for providing the data.  You'll often need to include a `-H "Content-type: application/json"` header as well indicating the type of data being sent.  
	* Inline 

	```	
	# When sending JSON data, you need to escape inner quotes
	curl -X POST -H "Authorization: Bearer $SPARK_TOKEN" -H "Content-type: application/json" https://api.ciscospark.com/v1/messages -d "{\"toPersonEmail\": \"$PARTNER_EMAIL\",\"text\": \"Test message from lab\"}"
	
	{"id":"...","roomId":"...","toPersonEmail":"...","roomType":"direct","text":"Test message from lab","personId":"...","personEmail":"...","created":"2016-07-26T21:05:00.330Z"}
	
	
	```

* If you are making a request to an HTTPs site, but one that lacks a fully verifiable certificate, curl will by default throw an error.  You can use the `-k` option to allow insecure connections.  

	```
	# Example command 
	curl -k https://badsecurity.com
	```  
	
* If you need to leverage a proxy server to access the site, use `-x <proxy>`

	```
	# Example command 
	curl -x "https://myproxyserver.com:8080" http://internet.com 
	```

### Links 

* [http://www.thegeekstuff.com/2012/04/curl-examples/](http://www.thegeekstuff.com/2012/04/curl-examples/)
* [http://www.slashroot.in/curl-command-tutorial-linux-example-usage](http://www.slashroot.in/curl-command-tutorial-linux-example-usage)
* [https://www.cheatography.com/ankushagarwal11/cheat-sheets/curl-cheat-sheet/](https://www.cheatography.com/ankushagarwal11/cheat-sheets/curl-cheat-sheet/)

### Go do it exercises 

Use curl to complete the following exercises

* Interact with the Weather.com API to find the Weather for San Francisco
* Use the Spark API to create a new room and add 3 of your fellow classmates to the room.  
	* Send a message to the room
	* Retrieve the messages from the room
		
### Helpful Hints and Gotchas

* Escaping command characters


## awk

awk is a very powerful pattern matching and processing program for lines of text.  Becoming a power user of awk will take years, but even a little bit of capability can be very helpful for processing text files (or more commonly, data returned from other programs).  

Here is a very basic awk command to disect

```
awk '/hello/ { print $2 }' hello.txt
```

* `awk` - the program to run 
* `'/hello/ { print $2 }'` - the action awk is being instructed to do
	* `/hello/` - the first part indicates the **match** part of the command using regular expressions.  In this case, match any line containing 'hello'
	* `{ print $2 }` - the second part is what to do with the match lines.  Here we are asking to print out the second field.  By default, awk considers whitespace to be field delimeters. 
* `hello.txt` - the file to process

### Experiments part 1

* Create a file called `hello.txt` that contains this data 
	
	```
	hello world
	goodbye world
	good morning
	good evening
	life is a box of chocolates
	you never know what you're going to get
	```

* Print the first word in each sentance 

	```
	awk '{ print $1 }' hello.txt
	
	hello
	goodbye
	good
	good
	life
	you
	```	

* Print the second word in all lines containing the word 'good'

	```
	awk '/good/ { print $2 }' hello.txt
	
	world
	morning
	evening
	
	# what if we don't want "goodbye" to match 
	awk '/good / { print $2 }' hello.txt
	
	morning
	evening
	```

* Count the number of lines containing 'world'

	```
	awk '/world/{++cnt} END {print "Count = ", cnt}' hello.txt
	```
	
### Links 

The above examples just introduce what awk can do.  Here are some links for when you need some more advanced details. 

* [http://www.tutorialspoint.com/awk/awk_basic_examples.htm](http://www.tutorialspoint.com/awk/awk_basic_examples.htm)
* [http://www.catonmat.net/download/awk.cheat.sheet.pdf](http://www.catonmat.net/download/awk.cheat.sheet.pdf)

### Go Do it Exercises 

* Download the text of Hamlet for the following exercies 

	```
	wget https://archive.org/download/hamlet01524gut/2ws2610.txt
	```

* Print out all lines containing the word 'Hamlet'
* Count the lines containing 'Death'
* Print all lines containing both 'Death' and 'Hamlet'


## grep



## sed

## bash scripts
