## Adding to your Dockerfile

* MAINTAINER: that's you!
* RUN: do any preparation or commands
* EXPOSE: Specify the port(s) your container will use to host services externally.

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