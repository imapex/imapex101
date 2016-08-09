[Class Contents](../README.md)

# Module 6: Leveraging Cisco DevNet

## [Finding and Accessing Cisco Development Docs](https://developer.cisco.com)

Though DevNet provides a number of services, arguably the most important is to provide context around why an application developer would write software that integrates with certain Cisco product and how to actually achieve that task.  The best and most adopted APIs can track their success to documentation that is easy to find, understand and use.  DevNet is working diligently across the company to tout the benefits of an API first mentality as new products are being developed.  That mentality dictates a conformity to excellent documentation with the application developer in mind.  DevNet has been successful thus far in influencing this change but as you'll see, there is much work to be done.

DevNet is currently broken up into DevCenters that contain several microsites pertaining to individual technologies.  In addition, there are several "spoke" sites off of the DevNet "hub" where product/BU teams provided alpha/beta content to limited audience before bringing it into DevNet, or as in the case of Spark, it made strategic sense to have the development site live outside of DevNet.

### ToDo
#### APIC-EM task
1. Find APIC-EM docs through DevNet
2. Find the API call to identify the hosts managed by the controller
3. Run the API call in documentation to create a ticket (username: devnetuser, password: Cisco123)

#### CMX task
1. Find CMX docs through DevNet
2. Find API call to identify the number of clients being tracked by the mobility services engine
3. Run the API call in the documentation (username: learning, password: learning)

#### Spark task
1. Find Spark docs through DevNet
2. Find API call to identify list of rooms you are a member of
3. Run the API call in the documentation to list the rooms

## [Learning Labs](https://learninglabs.cisco.com)

DevNet also prides itself on being an educational organization.  Starting at Cisco Live! US 2014, DevNet introduced [Learning Labs](https://learninglabs.cisco.com).  Learning Labs are self paced tutorials lasting 15-40 minutes in length designed to introduce users to new technologies in a step by step manner.  They are now organized into modules and tracks to allow users to focus on the labs that pertain specifically to their goals

### ToDo
#### Pick 2 learning labs of interest and complete them
#### [Building new Learning Labs](https://github.com/denapom11/imapex101/blob/master/module6/LearningLabs.md) 

DevNet provides the ability for any internal engineer or doc writer to build out a learning lab on a topic that they feel the larger developer community may find useful.  Documentation on how to do this is covered [here](https://github.com/denapom11/imapex101/blob/master/module6/LearningLabs.md)


## Sandboxes

Docmentation, tutorials and sample code are useless if developers don't have a sufficient environment to run their code against.  That's where the [DevNet Sandbox](https://devnetsandbox.cisco.com) comes in.  The DevNet Sandbox provides a few dozen combinations of technologies and infrastructure topologies for reservation or anytime use (these are know as "Always-On").  This allows application developers to have an environment to test out their applications or solutions without having to spend a lot of time and/or money to get their lab up and running.  

### Todo

#### Browse the offering available in the Sandbox and make a sandbox reservation

#### APIC-EM task
1. Find the instructions for the APIC-EM always on lab
2. Find APIC-EM docs
2. In Postman figure out how to create an API ticket on the APIC-EM always on Sandbox using credentials 
{
    "username":"devnetuser",
    "password":"Cisco123!"
    
}
3. Use that ticket to get a list of hosts managed on that controller

#### CMX Task
1. Find the instructions for the CMX always on lab
2. Find the CMX docs
3. In Postman, figure out how to get a list of the notification subscriptions already on the server
4. Reverse engineer the result to create a NEW notification subscription on the server

## API and Developer Support through DevNet

Downstream, as developers are working with the technologies in the sandboxes or in their own labs, they may come across some issues that they can't figure out, either because the documentation is bad *gasp*, or their problem is new, or there is a bug in the platform *double gasp*.  This is where support comes into play.

The first line of defense are the [DevNet Communities](https://communities.cisco.com/commmunity/developer).  This area is split up in relation to all of the technologies DevNet supports so for each microsite there is a community for discussion forums and blog content.  Though there is no SLA and response is best effort, DevNet staff monitor these forums daily and respond when the community does not or cannot.  

The second line of defence is a support ticket.  This is a benefit of the solution partner program or can be purchased on an ad-hoc basis.  Tickets are assigned to engineers directly who provide 1 on 1 developer support and potentially work hand in hand with TAC should it be a product issue.  These engineers are the third party developers' main advocate

## Hackathon and Meetup Support

From all the Cisco Live events, to global hackathons and conferences, if there are developers, DevNet is there.  Through our ever expanding team of Dev Evangelists, DevNet is represented all over the world touting the benefits of working with our myriad of technologies.  In a month or so we'll be launching the DevNet Events portal, allowing internal users to submit a request for DevNet to support events inside and outside of the company.  If we have the resources and it makes sense for us to be there (oh and if there is enough money for food and travel) then we'll be there to support it and reach out to the developers.

