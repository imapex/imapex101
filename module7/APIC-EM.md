#APIC-EM

The APIC-EM delivers SDN to the Enterprise to the WAN, Campus and Access networks. APIC-EM provides centralized automation of policy-based application profiles. Through programmability, automated network control helps IT rapidly respond to new business opportunities. APIC-EM can be downloaded at no additional charge using a free membership to the [Cisco DevNet community](http://devnet.cisco.com).

The APIC-EM is highly programmable through open APIs (representational state transfer [REST]). It can enable independent software developers to create innovative network services and applications to fuel business growth.

##Supported Platforms

The simpliest way to describe platform support for APIC-EM is essentially any router or switch that is currently not on an EoS/EoL cycle. The main page of the APCI-EM portal lists all supported platforms and minimum software releases. You can view the list of platforms [here](https://sandboxapic.cisco.com).

* Username - devnetuser
* Password - Cisco123!

The BU has stated they will be adding support for the ASA in APIC-EM in the GA 1.4 release. They are currently evaulating adding the Nexus 9K.

##API

The APIC-EM is highly programmable through open APIs (representational state transfer [REST]). It can enable independent software developers to create innovative network services and applications to fuel business growth.

APIC-EM's APIs are posted on both DevNet and through a swagger framework accessible on box at http://<hostname>/swagger. You can access the swagger interface through one of DevNet's [always on](https://sandboxapic.cisco.com/swagger) APIC-EM sandboxes.

Authentication is done through AuthToken. The following python script can be used to generate the token

~~~ 
# import request and json library
import requests
import json

#variable to define the url of the APIC-EM server
url = 'https://sandboxapic.cisco.com/api/v1/ticket'

#variable for login credentials for APIC-EM
payload = {"username":"devnetuser","password":"Cisco123!"}

#content type for header
header = {"content-type": "application/json"}

#POST for APIC-EM
response = requests.post(url,data=json.dumps(payload), headers=header, verify=False)

#print the response
print(response.text)
~~~

