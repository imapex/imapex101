## Docker build

```
$ docker build -t <your username>/imapex101_dockerfile:latest .

Sending build context to Docker daemon 2.048 kB
Step 1 : FROM debian:latest
latest: Pulling from library/debian
357ea8c3d80b: Pull complete
Digest: sha256:ffb60fdbc401b2a692eef8d04616fca15905dce259d1499d96521970ed0bec36
Status: Downloaded newer image for debian:latest
 ---> 1b01529cc499
Successfully built 1b01529cc499

# Run this command to view your newly created image
$ docker images

REPOSITORY                      TAG                 IMAGE ID            CREATED             SIZE
<your username>/imapex101_dockerfile   latest              1b01529cc499        23 hours ago        125.1 MB
```