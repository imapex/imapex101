[Class Contents](../README.md)

# Module 4: Continuous Integration/Deployment Tools

## Intro to CICD Tools

### Hudson / Jenkins

Hudson was sort of the grandfather of CI/CD tools, but was eventually forked into what became known as Jenkins.
Jenkins is today the most extensible CI/CD tool that is available, and offers over a thousand plugins for various
integrations such as SCM's, IaaS, PaaS providers, etc. The basic architecture of Jenkins consists of Master and slave
nodes, slave nodes can be added for additionally scalability for processing more jobs concurrently, as well as supporting
multiple platforms / architectures. Jenkins is configured primarily through a UI where plugins, jobs, and schedules are
managed centrally.  Based on the success of Jenkins other offerings were introduced which followed similar workflow and
architecture, these include Bamboo, Team City and others.

While Jenkins is still widely used in many development shops, new competitors have emerged which change the paradigm
for how we think about CI/CD.  These include Travis, CircleCI, and Drone to name a few.  The primary difference between
these products and their predecessors is where the configuration for the build pipeline resides.  As mentioned previously
Jenkins, Bamboo, and others relied on a seperate configuration which resided on the build server itself, whereas Drone,
Travis, and CircleCI leverages a build configuration file which resides with the source code itself, and is therefore
version controlled.

* Using Drone as a Build Server
  * Phases
    * Build
    * Publish
    * Deploy
    * Notify
  * The .drone.yml file
  * Activating a Repo
  * Drone CLI tools
    * Secrets and .drone.sec
  * Drone Plugins
  * Service Containers
  * Executing Tests
  * Conditionals
    * Branch/Tags
    * Success/Failure
    * Pull Requests
  * Badges
  * Practical Examples
    * Sending Messages to Spark
    * Webhooks to Mantl/Marathon