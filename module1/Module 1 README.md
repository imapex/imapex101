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
