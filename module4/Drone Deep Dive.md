# Using Drone as a Build Server

There are many options for Build Servers and CICD tools available.  As with any piece of software, every tool works a little differently, but the concepts are all the same.  Here we will be looking at [Drone.io](http://drone.io) as an example CICD platform that we can use.  

Drone is written in Go, and has been built with microservices and containers in mind.  Drone itself operates as a Docker container, and performs every task inside isolated docker containers making it ideal for using a single server that builds many different projects.  

## Key Concepts and Terms 

### Remote Driver

Drone is tightly integrated with the code repo (ie GitHub) and requires one be identified as the Remote Driver.  The code repository provides the user authentication for Drone, as well as the source for all builds.  

### Plug-Ins 

Drone is a module architecture with every aspect of the build done independently by a _plug-in_.  Exmamples of plug-in tasks are: 

* Publish a Docker Container 
* Send a notification to Spark
* Interact with a Git Repo 
* Interact with AWS, Azure, etc 

There are "official plug-ins" and community created plug-ins available.  

### Build Phases

Drone has 4 main build phases that are leveraged.  Other phases and steps are available, but these four main ones are enough to get started.  

#### Build

Think of this as the "Integration" part of CICD.  In the Build phase you will perform any testing and binary creation/compilation needed.  

#### Publish

Think of this as the "Delivery" part of CICD.  In the Publish phase you would make the artifacts from the Build phase available for use.  A common example would be creating a docker container and pushing it to a registry.  

#### Deploy 

Think of this as the "Deployment" part of CICD.  In the Deploy phase, you would create/update an environment with the newly Published code.  

### .drone.yml 

Drone leverages a file called `.drone.yml` in the repository root to describe the build process.  This is a yaml formated file that describes the Build phases, plug-ins used, etc.  

### Repositories 

Every repostitory in the underlying code repo is visible to a Drone user as "Available Repositories".  Repositories are "Activated" by a user to indicate that Drone should monitor and act on instructions contained.  

### .drone.sec 

Drone will be interacting with external systems on behalf of the user, and to do so needs usernames, account ids, passwords, etc to be available.  These can be provided in clear text within the .drone.yml file, but that is a major security risk.  To provide secret management, drone can encrypt secrets into a file called `.drone.sec` that can be safely commited to a repository.  

## Experiments 

To gain an understanding of using Drone, we will leverage the lab at: [hpreston/cicd\_learning\_lab](https://github.com/hpreston/cicd_learning_lab)

## Links 

* [Drone Usage](http://readme.drone.io/usage/overview/) 
* [Drone Plugins](http://readme.drone.io/plugins/) 
* Example .drone.yml files for actual projects 
	* [myhero_app](https://github.com/hpreston/myhero_app/blob/master/.drone.yml) 

## Why do we care... 

Modern application development is all about automation.  Manual build, test, and publish are rapidly being replaced by CICD tools and processes.  We need to understand, but also have a practical hands on knowledge to truly talk this topic other developers.  

Also, there is the practical reason that we will be building demo apps, and having the ability to use CICD for each demo will make our time usage the most optimal.  

## Go do it exercises 

Continue working on the demoapp used in the experiments section and take the following actions.  

* Replace the WebHook notification at the end and use the [drone-spark](https://hub.docker.com/r/hpreston/drone-spark) plug-in instead.
* Add support for branches by tagging the docker containers differently
	* tag each container with the name of the branch
	* If the branch is "master", also tag it as "latest"
* Publish your containers to quay.io in addition to hub.docker.com 


