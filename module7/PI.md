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

*curl -k "https://user:passwd@PI-server/webacs/api/v1/data/Devices"*  
This call results in a list of devices, but the only unique identifier is their "entity id"  
![alt txt](images/PI-Device-List.PNG)

It is possible to pull more detailed information about these devices by expanding on the request:  
*curl -k "https://user:passwd@PI-Server/webacs/api/v1/data/Devices?.full=true"*  
But this would provide a very long list of data about each device in PI's database.  

So this introduces some of the additional power in PI's APIs: *Sorting, Filtering, and Paging*  
**Sorting** allows the response to be sorted by virtually any value returned in the response (ipAddress for example).  
**Filtering** allows the response to be filtered based on rules found [here](https://developer.cisco.com/media/prime-infrastructure-api-reference-v3-1/192.168.115.187/webacs/api/v1/index0404.html?id=filtering-doc), and includes options like "contains" or "endsWith".  
**Paging** allows the response to be limited to a certain number of results.  

If we wanted to request a list from the PI server for the total number of ISR4331s in its database, then we could use: *curl -k "https://user:passwd@PI-Server/webacs/api/v1/data/Devices?.full=true&.sort=ipAddress&deviceType=contains(\"4331\")"*  

Part of the results:  
![alt-txt](images/PI-REST-Sorting&Filtering.PNG)  
