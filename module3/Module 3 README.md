[Class Contents](../README.md)

# Module 3: Advanced Docker and Docker Hub

* [Dockerfile Creation](#dockerfile-creation)
* [Trusted Registries](#trusted-registries)
* [Public vs Private](#public-vs-private) 
* [Tags](#tags)
* [Manual vs Auto-Build Repos](#manual-vs-auto-build-repos)

# Why... 

Containers, and Docker containers specifically, are rapidly becoming a common way to package and distribute applications.  No longer are installation files, or binaries to download considered an optimal way to recieve and consume software.  The ability to easily contain (no pun intended) and isolate everything needed for an applciaiton, and make it easy to standup in *any* environment makes it ideal for building demos and sample applications.  

# Dockerfile Creation 

A Docker container is built based on instructions in a Dockerfile.  The Dockerfile begins with a source container image, and then each line in the file adds a new layer onto the starting point until the final container image is created.  Dockerfiles range from very simple, few line descriptions, to very complext files with many layers and configuration elements.  

As you work with Dockerfiles, and create containers for applicaitons that others will use, it can be helpful to keep some best practices and standards in mind.  We'll walk through an example Dockerfile in the experiments section highlighting some best practices and the impacts.  

## Experiments 

*In this section, use whatever text editor you wish when updating the Dockerfile*

* Create a new directory for the Dockerfile practice 
	
	```
	mkdir imapex101_dockerfile
	cd imapex101_dockerfile
	touch Dockerfile
	```
	
* **Dockerfile Content**: Dockerfiles use `FROM` to indicate the base image

	```
	FROM debian:latest
	
	```

	* the `:latest` part indicates the "tag" to use on the image.  Tags will be covered more later, but for now know that "latest" is a well understood standard tag in Docker.  If you do NOT explicitly set a tag, Docker will look for a "latest" tag.  
* `docker build` is the command to build the container image.  When running use `-t <repositoryname>:<tag>` format to provide a repository name and tag for the image.  If you fail to specify, you can only refer to the image by the Image Id.
	* Repository Names are in the format of `<username or org>/<repo-name>`.  This will be required if you plan to `push` your image to a registry.  
	* The last parameter is the location to find the Dockerfile to use.  Specifying `.` looks in the current directory for `Dockerfile`

	```
	docker build -t <your username>/imapex101_dockerfile:latest .
	
	Sending build context to Docker daemon 2.048 kB
	Step 1 : FROM debian:latest
	latest: Pulling from library/debian
	357ea8c3d80b: Pull complete
	Digest: sha256:ffb60fdbc401b2a692eef8d04616fca15905dce259d1499d96521970ed0bec36
	Status: Downloaded newer image for debian:latest
	 ---> 1b01529cc499
	Successfully built 1b01529cc499
	
	# Run this command to view your newly created image
	docker images
	
	REPOSITORY                      TAG                 IMAGE ID            CREATED             SIZE
	<your username>/imapex101_dockerfile   latest              1b01529cc499        23 hours ago        125.1 MB
	
	```

* We won't do this for every version, but run this command to start a container based on your image and enter it's shell.  
	* `-it` attaches to STDIN and creates a tty terminal to use 
	* `/bin/bash` specifies the command to run inside the container

	```
	# And you can run this command to start a container based on the image, and access it's shell 
	docker run -it <your username>/imapex101_dockerfile /bin/bash
	
	# now you're in the container, type exit to stop the container
	root@80333d17d6c2:/# exit
	
	# run this command to see the remnants of your container... you could restart it from this state with docker start, but another docker run would create a new one
	docker ps -a
	CONTAINER ID        IMAGE                           COMMAND                  CREATED             STATUS                     PORTS               NAMES
	80333d17d6c2        <your username>/imapex101_dockerfile   "/bin/bash"              35 seconds ago      Exited (0) 3 seconds ago                       nauseous_raman
	```

* **Dockerfile Content**: Let's add some more parts to the Dockerfile 
	* `MAINTAINER` provides details about the author.  Providing your name and email are typical.  Email address within `< >` symbols.
	* The next layer should install any packages needed.  Use a single `RUN` command and leverage `&&` to string commands together, and `\` to allow readabilty with wrapping

```
FROM debian:latest
MAINTAINER Your Name <email@domain.com>

# You can provide comments in Dockerfiles
# Install any needed packages for your application
RUN apt-get update && apt-get install -y \
    aufs-tools \
    automake \
    build-essential \
    curl \
    dpkg-sig \
    mercurial \
 && rm -rf /var/lib/apt/lists/*
```

* Build a new version of the container
	* Note the references to `Step 2` and `Step 3` and the `running in` comments.  Each command in the file, is a Step, and each step is a new layer.  Minimizing the number of layers created is always a goal in Dockerfile creation

	```
	docker build -t <your username>/imapex101_dockerfile:latest .
	
	Sending build context to Docker daemon 2.048 kB
	Step 1 : FROM debian:latest
	 ---> 1b01529cc499
	Step 2 : MAINTAINER Hank Preston <hank.preston@gmail.com>
	 ---> Using cache
	 ---> 9f7054e99744
	Step 3 : RUN apt-get update && apt-get install -y     aufs-tools     automake     build-essential     curl     dpkg-sig     mercurial  && rm -rf /var/lib/apt/lists/*
	 ---> Running in 11f0aa8fea4c
	Get:1 http://security.debian.org jessie/updates InRelease [63.1 kB]
	Ign http://httpredir.debian.org jessie InRelease
	Get:2 http://httpredir.debian.org jessie-updates InRelease [142 kB]
	Get:3 http://httpredir.debian.org jessie Release.gpg [2373 B]
	Get:4 http://security.debian.org jessie/updates/main amd64 Packages [371 kB]
	Get:5 http://httpredir.debian.org jessie Release [148 kB]
	Get:6 http://httpredir.debian.org jessie-updates/main amd64 Packages [17.6 kB]
	Get:7 http://httpredir.debian.org jessie/main amd64 Packages [9032 kB]
	Fetched 9776 kB in 18s (528 kB/s)
	Reading package lists...
	Reading package lists...
	Building dependency tree...
	Reading state information...
	The following extra packages will be installed:
	  autoconf autotools-dev binutils bzip2 ca-certificates cpp cpp-4.9 dpkg-dev
	  fakeroot file... 

	  ####
	  # output truncated
	  ####
	  
	 ---> 331e39ad1dc4
	Removing intermediate container 11f0aa8fea4c
	Successfully built 331e39ad1dc4  
	``` 

* **Dockerfile Content**:  Use `EXPOSE` to specify what port(s) your container will use to host services externally.  For example, if you are building a Web App Container, you'll likely expose port 80.  

```
FROM debian:latest
MAINTAINER Your Name <email@domain.com>

# You can provide comments in Dockerfiles
# Install any needed packages for your application
RUN apt-get update && apt-get install -y \
    aufs-tools \
    automake \
    build-essential \
    curl \
    dpkg-sig \
    mercurial \
 && rm -rf /var/lib/apt/lists/*
 
EXPOSE 80

```

* Build a new version of the container
	* Note how the process takes much less time and the references to "Using cache".  Because there has been no change in the earlier steps, docker needn't rerun them
	* This is why proper consideration in the order of steps in your container creation is critical.  
	* Keep the steps likely to change (ie Copying in your code) to the end.  

	```
	docker build -t <your username>/imapex101_dockerfile:latest .
	
	Sending build context to Docker daemon 2.048 kB
	Step 1 : FROM debian:latest
	 ---> 1b01529cc499
	Step 2 : MAINTAINER Hank Preston <hank.preston@gmail.com>
	 ---> Using cache
	 ---> 9f7054e99744
	Step 3 : RUN apt-get update && apt-get install -y     aufs-tools     automake     build-essential     curl     dpkg-sig     mercurial  && rm -rf /var/lib/apt/lists/*
	 ---> Using cache
	 ---> 331e39ad1dc4
	Step 4 : EXPOSE 80
	 ---> Running in 67d60d70e80b
	 ---> 788c0d174e3d
	Removing intermediate container 67d60d70e80b
	Successfully built 788c0d174e3d
	```	

* Now we'll create a program to run in the container.  Run these commands to create a basic Hello World shell script.  

```
echo '#!/bin/bash' > hello_world.sh
echo "while [ 0 -eq 0 ]; do" >> hello_world.sh
echo "echo 'Hello World'" >> hello_world.sh
echo "sleep 2" >> hello_world.sh
echo "done" >> hello_world.sh
```

* **Dockerfile Content**: 
	* Use `COPY` to bring in your code to the container.  
	* After copying your code into the container, use `RUN` commands to take whatever actions needed.  
	* Use `CMD` to instruct the container what to do upon execution.  

	```
	FROM debian:latest
	MAINTAINER Your Name <email@domain.com>
	
	# You can provide comments in Dockerfiles
	# Install any needed packages for your application
	RUN apt-get update && apt-get install -y \
	    aufs-tools \
	    automake \
	    build-essential \
	    curl \
	    dpkg-sig \
	    mercurial \
	 && rm -rf /var/lib/apt/lists/*
	 
	EXPOSE 80
	
	COPY hello_world.sh /root/
	RUN chmod +x /root/hello_world.sh
	
	CMD ["/root/hello_world.sh"]
	```

* Build a new version of the container

	```
	docker build -t <your username>/imapex101_dockerfile:latest .
	
	Step 1 : FROM debian:latest
	 ---> 1b01529cc499
	Step 2 : MAINTAINER Hank Preston <hank.preston@gmail.com>
	 ---> Using cache
	 ---> 9f7054e99744
	Step 3 : RUN apt-get update && apt-get install -y     aufs-tools     automake     build-essential     curl     dpkg-sig     mercurial  && rm -rf /var/lib/apt/lists/*
	 ---> Using cache
	 ---> 331e39ad1dc4
	Step 4 : EXPOSE 80
	 ---> Using cache
	 ---> 788c0d174e3d
	Step 5 : COPY hello_world.sh /root/
	 ---> 93105ac34a3b
	Removing intermediate container d973d85f74f2
	Step 6 : RUN chmod +x /root/hello_world.sh
	 ---> Running in 888ee3e0c9fd
	 ---> 2524c6f6b0bb
	Removing intermediate container 888ee3e0c9fd
	Step 7 : CMD /root/hello_world.sh
	 ---> Running in 38a8f37827db
	 ---> afde9a78e299
	Removing intermediate container 38a8f37827db
	Successfully built afde9a78e299
	```

* Run the final container version to execute the program.  We use `-d` to run our container in the background and print out the container id

```
docker run -d --name dockerfile <your username>/imapex101_dockerfile:latest

8b5b52eaa9a7c838c77bed791315a42ac7270e714c5fcd3ffbdbc49ef94b4316
```

* Check out the status of the container with a few commands here

```
# Checkout the status of running containers here 
docker ps 

CONTAINER ID        IMAGE                                         COMMAND                  CREATED              STATUS              PORTS               NAMES
8b5b52eaa9a7        <your username>/imapex101_dockerfile:latest   "/root/hello_world.sh"   About a minute ago   Up About a minute   80/tcp              dockerfile

# Let's see if the container is "running" our application by checking out the logs
docker logs dockerfile 

Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World
Hello World

# Sure enough, it's hello worlding away
# you can stop and start the same container like this
docker stop dockerfile 

# Look at all docker containers and see its stopped
docker ps -a 

CONTAINER ID        IMAGE                                         COMMAND                  CREATED             STATUS                        PORTS               NAMES
8b5b52eaa9a7        <your username>/imapex101_dockerfile:latest   "/root/hello_world.sh"   4 minutes ago       Exited (137) 14 seconds ago                       dockerfile

# Start it back up
docker start dockerfile 

docker ps 

CONTAINER ID        IMAGE                                         COMMAND                  CREATED             STATUS              PORTS               NAMES
8b5b52eaa9a7        <your username>/imapex101_dockerfile:latest   "/root/hello_world.sh"   5 minutes ago       Up 2 seconds        80/tcp              dockerfile

```

## Links 

The experiments were just a walkthrough of the very basics.  Review these links for a more thorough discussion on best practices, and for examples of good Dockerfiles.  

* [https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/)
* [https://github.com/docker-library/golang/blob/7fd2b76513e537343f088da671a51f5b2ea7d4c3/1.5/Dockerfile](https://github.com/docker-library/golang/blob/7fd2b76513e537343f088da671a51f5b2ea7d4c3/1.5/Dockerfile)
* [https://docs.docker.com/engine/reference/builder/](https://docs.docker.com/engine/reference/builder/)
* [http://zeroturnaround.com/wp-content/uploads/2016/03/Docker-cheat-sheet-by-RebelLabs.png](http://zeroturnaround.com/wp-content/uploads/2016/03/Docker-cheat-sheet-by-RebelLabs.png)

## Why do we care 

We'll be creating docker containers for many of our demos.  Though we don't need the level of exactness used in commercial distributions, we do want to make sure we build respectible containers, that follow standards and best practices.  Also, doing what we can to keep them small and quick to build/rebuild will help in our development practices.  

## Go Do it Exercises 

For this exercise, build a new Dockerfile that... 

* Uses an "alpine" image (you'll need to find out what that means) 
* Runs [dbarnett/python-helloworld](https://github.com/dbarnett/python-helloworld) when started

# Trusted Registries 

## Experiments 

## Links 

## Why do we care 

## Go Do it Exercises 


# Public vs Private

## Experiments 

## Links 

## Why do we care 

## Go Do it Exercises 



# Tags 

## Experiments 

## Links 

## Why do we care 

## Go Do it Exercises 


# Manual vs Auto-Build Repos

## Experiments 

## Links 

## Why do we care 

## Go Do it Exercises 

