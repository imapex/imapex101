# What is a Learning Lab?

Learning Labs are intended to be relatively short self-paced exercises to introduce someone to developer-oriented technology.  They can encompass basic developer tooling such as Postman and Git, but typically BUs intended to teach their Cisco developer technology (API, SDK, whatever).  A lab should take someone on the low end 15 minutes, and on the longer end 40 minutes.  We recommend that you include at least a beginner lab that will give a sense of the technology because we have a mixed audience, many of which are new to programming.  You can build up complex labs as well so long as they don't take longer than about 40 minutes.

These labs are intended to be available during events, such as Cisco Live, but also **generally available** on the Internet between events.

If you want to create code examples that the developer can run on a workstation, please make sure you read the section on code examples later in this guide.

## Getting Started Video

<a href="https://cisco.box.com/s/pjwep73hsxhjy668zq7en3m5veysxma9">Getting Started Video</a>

## Cloud vs. On-Prem

Leveraging a hosted / Cloud environment for your backend is recommended.  

## Events
At events like CiscoLive or GSX, we setup anywhere from 16 to 32 workstations, which run Windows via Citrix for centralized control and management.  If you need local tooling on the workstation and/or the server hosted for you, *please get this information to us immediately*.

Information that we need includes:
* Server
	* OS / Memory / HD requirements
	* Can your lab support a shared instance or do you need a unique instance per lab user?
	* What ports do you need opened?
	* Do you have a shared login or individual logins per lab user?
* Client
	* Does your client environment work under Citrix ESXi?
	* OS / Memory / HD requirements
	* Does your client have needs for specialized hardware (e.g., IoT devices, phones, etc.)?
	* Does your lab require special drivers?
	* Do you have source code that you'd like to share on GitHub?
	* Do you need a VPN connection?
	* Any runtimes beyond Python & Java (e.g. Go, C#, C++, etc.)?


Tooling on the workstation already:
* Python 2 & Python 3 (we recommend Python 3)
* Cisco AnyConnect
* Java 7
* Notepad++

# Lab Template

In this project, under the `docs/templates` directory, you will find a small example of a lab.  This should streamline lab creation for most lab creators.  Rename the `labid` folder and json file to the labid of your choosing.

# Lab Authoring

The following describes how to generate and structure your Learning Lab tutorial.  Lab content is created in Markdown format.  See [this site](http://daringfireball.net/projects/markdown/syntax) for detailed syntax documentation.  As an aside, Markdown is fairly flexible, and so you can also include arbitrary HTML.  The markdown files are dynamically converted to HTML when the lab is loaded.  Visit <http://learninglabs.cisco.com> to see examples.  A good exemplar is the [Coding 102 Lab](https://learninglabs.cisco.com/#/labs/coding-102-rest-python/step/1), you can find the source for this under `src/posts/files/coding-102-rest-python`.  

There are many Markdown editors & previewers for Mac or Windows.  Using one of them may help you with formatting.  I've been using Byword on the Mac, but Sublime Text, Text Mate support Markdown. MacDown and Mou are free editors.

Common Markdown syntax:

* To insert an image: `![Figure](/posts/files/cmx/postmanlaunch.png)`
* Separate code examples with a bactick (`)
* `<h1>` corresponds to `#`, `<h2>` to `##`, `<h3>` to `###`, and so on
* You may find it helpful to view the Markdown for this readme.  If so, you can go [here](http://gitlab.cisco.com/learning-labs/ng-learninglabs/raw/master/docs/LAB-CREATION.md)

*A note on image paths* -- If you are authoring outside of the learning labs application by just using a markdown editor, you will need to update your image paths to be `posts/files/<labid>/<image-name>` so that they will render properly when loaded in the context of the lab application.  Also, please try to follow best practices in image file size, by attempting to make them as small as possible.  A service like [tinypng](https://tinypng.com) can be useful.

## Lab content files

* Lab content is in the `client/posts/files` directory.
* `posts.json` includes an index of the labs that are available.
* The `labId` is used as the folder name for the lab, and the labs should be broken into individual markdown files numbered 1.md, 2.md, etc. corresponding to the lab step.  Include images within the labId folder name.  
* An example layout from the CMX is below:

```
posts
├── cmx.json
├── files
│   ├── cmx
│   │   ├── 1.md
│   │   ├── 2.md
│   │   ├── 3.md
│   │   ├── 4.md
│   │   ├── 5.md
│   │   ├── byod.html
│   │   ├── DevNet1.png
│   │   ├── DevNet2.png
│   │   ├── MSEInfrastructure.png
│   │   ├── POSTman1.png
│   │   └── postmanlaunch.png
└── posts.json
```

Note: See the example in the `docs/templates` directory.

### BYOD Information
To enable people to complete Learning Labs outside of an event, such as at their hotel room or at home, you can include "bring your own device" information in the lab by including a file called `byod.html` in your directory.  Author this content in HTML.  This will be displayed as an "accordion" element at the top of your lab.  Enable this by setting your lab JSON file property `"byod": true`.  

Example file `dmo.json`:

```
{
  "labId": "dmo",
  "files": [
    {"title": "1.md"},
    {"title": "2.md"},
    {"title": "3.md"},
    {"title": "4.md"},
    {"title": "5.md"},
    {"title": "6.md"}
  ],
  "byod": true
}
```

Note: See the example in the `templates` directory.

### Related Labs
To display related labs on the completed page, you can reference other labs by adding a JSON array named `related`.  You can determine the related lab ID to use by looking at the URL for a given lab.  The lab ID is contained in the path between `labs/` and `step`.  Example: `#/labs/cmx/step/1` where cmx is the lab ID.

Example file `apic-em-basic.json`:

```
{
  "labId": "apic-em-basic",
  "files": [
    {"title": "1.md"}
  ],
  "related": [
    {
      "labId": "apic-em",
      "title": "APIC-EM with Python"
    },
    {
      "labId": "apic-hunt",
      "title": "APIC-EM Treasure Hunt"
    }
  ]
}
```

Note: See the example in the `templates` directory.

## Code examples
If your lab contains code examples, you should create a git project with your sample code.  These examples will be hosted somewhere (GitHub or DevHub), so that we can have lab participants checkout appropriate tags and work in a read-only mode.  An example of this layout can be found [here](http://gitlab.cisco.com/asroach/apic-em-lab-example/tree/master).  You should include commentary in your lab on how to checkout the appropriate step.  The [Angular JS tutorial](https://docs.angularjs.org/tutorial/step_00) is a good example of how to do this.

Note: See the example in the `templates` directory.

## Video files
If you'd like to include video files, you can use the HTML5 syntax like this.  Since video files can be large, please work with Ashley Roach to figure out the best way to add these to the repository and site.

```
<video poster="posts/files/virl/images/ml.02.png" width="480" height="300" none controls> <source src="/virl-static/ml.02.mp4" type="video/mp4"> </video>
```

## Automated Credential Distribution and VM restarts

In event mode only, the Learning Labs platform contains a mechanism to automatically distribute a set of credentials, IP addresses, as well as start and stop VMs.  The distribution of addresses and credentials is managed so that all addresses are distributed before repeating an address.

We support two types of labs:

1. Single Credential with unique IP address or URL:

~~~
All users auth with demo/demo123
http://10.10.10.1/api/example
http://10.10.10.2/api/example
http://10.10.10.3/api/example
...
~~~

2. Multiple Credentials with a unique combination of IP address/URL and username

~~~
All users access a single instance; but use multiple credentials
http://10.10.10.1/api/example
demo1/demo123
demo2/demo123
demo3/demo123
...
~~~

For the reset/reload, we are expecting a single host that learning-labs (LLs) can make request to. Also, a way to get statuses for each server.

The flow is as follow:
User completed the lab — LLs take the server out of rotation and makes the request for reload
A cron service (on LLs) picks up the server out of rotation and makes the request for status — if response is “ready | online | etc”  then it’ll put it back into rotation.

Sample reload path:
`<host>:<port>/server/reload/<ip|URL>` or `<host>:<port>/server/reload?address=<ip|URL>`

Sample status path:
`<host>:<port>/server/status/<ip|URL>` or `<host>:<port>/server/status?address=<ip|URL>`

IMPORTANT: Response status(es) must be in JSON or simple text format.

JSON: Response header `Content-Type` should be `application/json` and body containing

`{"status": "open"}`

Simple text: Response header `Content-Type` should be `text/plain` and body containing

`open`

*Case insenitive


# Publishing

* Deliver a zipped up version of your lab folder containing the indivdual markdown files and images to your DevNet representative.
* If you're familiar and comfortable with the Git version control system, we can work with you to deliver via a pull request.
