## run it! stop it!

```
$ docker run -d --name dockerfile <your username>/imapex101_dockerfile:latest

8b5b52eaa9a7c838c77bed791315a42ac7270e714c5fcd3ffbdbc49ef94b4316

# Checkout the status of running containers here 
$ docker ps 

CONTAINER ID        IMAGE                                         COMMAND                  CREATED              STATUS              PORTS               NAMES
8b5b52eaa9a7        <your username>/imapex101_dockerfile:latest   "/root/hello_world.sh"   About a minute ago   Up About a minute   80/tcp              dockerfile

$ docker stop dockerfile
```