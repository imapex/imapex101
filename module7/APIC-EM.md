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

Once you have a token you can then make requests for data out of APIC. In the following example we will generate our token and hten request the software version running on all devices in inventory.

~~~
__author__ = 'Administrator'

import requests,json
import re

### Disable invalid certificate warnings.
requests.packages.urllib3.disable_warnings()

def createserviceticket():
    response = requests.post(
        url="https://198.18.129.100/api/v1/ticket",
        headers={
            "Content-Type": "application/json",
        },
        verify=False,
        data=json.dumps({
            "username": 'admin',
            "password": 'C1sco12345'
        })
    )
    output = ('Response HTTP Response Body: {content}'.format(content=response.content))
    match_service_ticket = re.search('serviceTicket":"(.*cas)', output, flags=0)
    service_ticket = match_service_ticket.group(1)
    return service_ticket

url = "https://198.18.129.100/api/v1/network-device"

response = requests.get(url,headers={"X-Auth-Token": createserviceticket(),"Content-Type": "application/json",},verify=False)

data = response.json()

device_list = data['response']
for device in device_list:
    print 'Hostname: %s' % device['hostname']
    print '     Software Version: %s '% device['softwareVersion']

~~~