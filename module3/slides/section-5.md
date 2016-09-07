## docker run


```
$ docker run -it <your username>/imapex101_dockerfile /bin/bash
```

* `-it` attaches to STDIN and creates a tty terminal to use
* `/bin/bash` specifies the command to run inside the container

```
# And you can run this command to start a container based on the image, and access it's shell 
$ docker run -it <your username>/imapex101_dockerfile /bin/bash

# now you're in the container, type exit to stop the container
root@80333d17d6c2:/# exit

# run this command to see the remnants of your container... you could restart it from this state with docker start, but another docker run would create a new one
$ docker ps -a

CONTAINER ID        IMAGE                           COMMAND                  CREATED             STATUS                     PORTS               NAMES
80333d17d6c2        <your username>/imapex101_dockerfile   "/bin/bash"              35 seconds ago      Exited (0) 3 seconds ago                       nauseous_raman
```

