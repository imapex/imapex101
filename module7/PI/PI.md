# Programming in Prime Infrastructure

PI 3.1 can be programmed using its REST APIs.  It supports **XML** and **JSON** data formats.  It follows the typical REST model, where:  
  GET = retrieve  
  POST = submit  
  PUT = change  
  DELETE = delete  

Authentication is required.  A user account that provides support for **NBI Read**, **NBI Write**, and **NBI Credential** is required. Furthermore, if PI does not have a valid certificate installed, the user account must also have **admin** privileges.  

Key uses of the PI API includes:   
   1. Monitoring alarms and events   
   2. Collecting device inventory   
   3. Monitoring network clients and usage   
   4. Configuring devices   

## Sample REST Calls in PI

A full list of available API's for PI can be found at [DevNet's Page for PI](https://developer.cisco.com/site/prime-infrastructure/documents/api-reference/rest-api-v3-1/)

An example of what can be done in PI would be to pull a list of devices in PI's database:

```curl -k "https://user:passwd@PI-server/webacs/api/v1/data/Devices"```
  
This call results in a list of devices, but the only unique identifier is their "entity id"  
![alt txt](images/PI-REST-PullingDeviceList-CURL.PNG)

It is possible to pull more detailed information about these devices by expanding on the request:  

```curl -k "https://user:passwd@PI-Server/webacs/api/v1/data/Devices?.full=true"```
  
But this would provide a very long list of data about each device in PI's database.  

So this introduces some of the additional power in PI's APIs: *Sorting, Filtering, and Paging*  
**Sorting** allows the response to be sorted by virtually any value returned in the response (ipAddress for example).  
**Filtering** allows the response to be filtered based on rules found [here](https://developer.cisco.com/media/prime-infrastructure-api-reference-v3-1/192.168.115.187/webacs/api/v1/index0404.html?id=filtering-doc), and includes options like "contains" or "endsWith".  
**Paging** allows the response to be limited to a certain number of results.  

If we wanted to request a list from the PI server for the total number of ISR4331s in its database, then we could use: 

```curl -k "https://user:passwd@PI-Server/webacs/api/v1/data/Devices?.full=true&.sort=ipAddress&deviceType=contains(\"4331\")"```  

Part of the results:  
![alt-txt](images/PI-REST-Sorting&Filtering.PNG)  

## Sample Python Scripts in PI

A great source of examples on using python to program through PI using REST and the API's in PI is from Adam Radford's examples on Github:

*http://github.com/aradford123/cisco-prime-infrastructure-examples*


An example python script here shows how to get a list of devices in PI's database

```python
#!/usr/bin/env python
from __future__ import print_function
import requests
import json
from argparse import ArgumentParser

requests.packages.urllib3.disable_warnings()
from pi_config import PI, USER, PASSWORD

BASE="https://%s:%s@%s/webacs/api/v1/" %(USER,PASSWORD,PI)

class NoDeviceFound(Exception):
    pass
def all_devices():
    print ("Getting all devices")
    print ("{0:6s} {1:10s}".format("ID", "IP address"))
    result = requests.get(BASE + "data/Devices.json?.full=true", verify=False)
    result.raise_for_status()
    for device in result.json()['queryResponse']['entity']:
        print (device['devicesDTO']['@id'], device['devicesDTO']['ipAddress'])

def device_by_id(id):
    print ("Getting a specific device")
    result = requests.get(BASE + "data/Devices/%s.json?.full=true" % id, verify=False)
    result.raise_for_status()
    print (json.dumps(result.json(), indent=2))

def device_by_ip(ip):

    result = requests.get(BASE + "data/Devices.json?.full=true&ipAddress=%s" % ip, verify=False)
    result.raise_for_status()
    if result.json()['queryResponse']['@count'] == "1":
        return result.json()
    else:
        raise NoDeviceFound("No device with ip: %s" %ip)

def device_to_id(devicesearchDTO):
    return devicesearchDTO['queryResponse']['entity'][0]['devicesDTO']['@id']


if __name__ == "__main__":
    parser = ArgumentParser(description='Select options.')
    parser.add_argument('--id', type=str,
                        help="device details by id")
    parser.add_argument('--ip', type=str,
                        help="device details by ip address")
    args = parser.parse_args()

    if args.id:
        device_by_id(args.id)
    elif args.ip:
        print (json.dumps(device_by_ip(args.ip), indent=2))
    else:
        all_devices()
```

