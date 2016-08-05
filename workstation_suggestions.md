[Class Contents](README.md)

# Personal Workstation Suggestions

Modern developers expect some freedom in their laptop/desktop setups.  What Operating System, Editors, GUI/CLI, etc are all choices a developer can make across a number of free and commercial tools today.  As long as the created product meets the needs of the overall project, and can be distributed adequately, the details of how the developer worked is less relevant.  

So that means, outside of some corporate policy, there is no _right_ way to work.  However, if you are new to being a _developer_ you might feel overwhelmed and not sure where to start.  Here we will compile a list of some suggestions and lessons learned...

* [Operating Systems](#operating-systems)
	* [MacOS](#mac-os)
	* [Linux](#linux)
	* [Windows](#windows)
* [Must-Have Utilities](#must-have-utilities)
	* [Source Control](#source-control)
	* [Working Environment](#working-environment)
	* [Configuration Mangaement](#configuration-management)
	* [IaaS Tools](#iaas-tools)
	* [IDEs and Editors](#ides-and-editors)
	* [Other](#other)
* [Services and Accounts](#services-and-accounts)
	* [IaaS and PaaS Platforms](#iaas-and-paas-platforms)
	* [Source Control and Artifact Repositories](#source-control-and-artifact-repositories)
	* [Collaboration](#collaboration)
	* [Continuous Integration Server](#continuous-integration-server)

You certainly don't everything on this list to get started, or even eventually.  This list is simply provided as a starting point when trying to decide where to start with a particular need you might run into.  

---
# Operating Systems

## MacOS
Apple MacOS is a great platform used by many developers, both new and seasoned.  It balances the line between a commercial OS built for usability, but also has the Linux underpinnings helpful for developers.  

## Linux
Linux is a great platform for development, with many open source and some commercial software packages available.  Though quickly changing, it isn't as polished and immediately user friendly like Mac OS X and Windows.  

## Windows
Windows can be a great platform for developers working in traditional Microsoft platforms like .NET.  However for developers developing for more Linux heavy platforms, Windows can be a challenge.  There has been a great deal of work by Microsoft to make it more universally developer friendly, but be cautious of potential problems if you choose to use Windows as your platform.  

---
# Must-Have Utilities

## Source Control

* [git][]

## Working Environment

* [Vagrant][]
* [Docker][]
* [VirtualBox][]

## Configuration Management

* [Ansible][]
* [Terraform][]

## IaaS Tools

* [AWS CLI][]
* OpenStack CLI - unlike many of these other tools, this is best installed via your
Linux distribution, a git clone of the repo, or [brew][] (on MacOS), not by downloading a package from
the OpenStack.org website.

## IDEs and Editors

* [Atom][]
* JetBrains Tools
	* [PyCharm][]
	* [WebStorm][]
* [Eclipse][]
* [BBEdit][]/[TextWrangler][]
* [MacDown][]
* [Visual Studio Code][]

## Other

* [Drone CLI][]
* [brew][] - Mac specific. Used to install tools traditionally used in Linux
onto MacOS without creating conflicts with Apple provided tools.


[git]:https://git-scm.com
[Vagrant]:https://www.vagrantup.com
[Docker]:https://www.docker.com
[VirtualBox]:https://www.virtualbox.org
[Ansible]:https://www.ansible.com
[Terraform]:https://www.terraform.io
[AWS CLI]:https://aws.amazon.com/cli/?nc2=h_m1
[brew]:http://brew.sh
[Atom]:http://atom.io
[PyCharm]:https://www.jetbrains.com/pycharm/
[WebStorm]:https://www.jetbrains.com/webstorm/
[Eclipse]:http://www.eclipse.org/downloads/
[BBEdit]:http://www.barebones.com/products/bbedit/index.html
[TextWrangler]:http://www.barebones.com/products/textwrangler/
[Drone CLI]:https://github.com/drone/drone
[MacDown]:http://macdown.uranusjr.com
[Visual Studio Code]:https://code.visualstudio.com

---
# Services and Accounts

## IaaS and PaaS Platforms

* OpenStack
* AWS
* Mantl
* Shipped

## Source Control and Artifact Repositories

* GitHub
* Docker Hub

## Collaboration

* Slack
* Gitter
* Cisco Spark

## Continuous Integration Server

* Drone
