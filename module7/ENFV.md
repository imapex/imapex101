# Programming in NFVIS

NFVIS can be programmed using its REST APIs.  It supports **XML** and **JSON** data formats.  It follows the typical REST model, where:  
  GET = retrieve  
  POST = submit  
  PUT = change  
  DELETE = delete  

Authentication is required.  The authentication will be basic.

Key uses of the NFVIS API includes:   
   1. VM image import, status checking, and deletion   
   2. Bridge and Network creation, modification, status, and deletion  
   3. VM profile creation, modification, status, and deletion     
   4. VM deployments  
   5. VM operations     

## Sample REST Calls in NFVIS

A full list of available API's for NFVIS can be found at [this HTTP Server](http://10.91.13.171/Files/nfvis-user-guide_May-6-early-draft.pdf)

An example of what can be done in NFVIS would be to pull a list of VM's deployed on NFVIS:

*curl -k "https://user:passwd@NFVIS-server/api/config/esc_datamodel/tenants/tenant/admin/deployments?deep"*  
This call results in a list of VM's deployed on the platform including the profile of the device and its configuration.
![alt txt](http://10.91.13.171/Files/NFVIS-REST-VM-Status-1.PNG)  
![alt txt](http://10.91.13.171/Files/NFVIS-REST-VM-Status-2.PNG)  

This API also would make it possible to deploy a VM from an image that is already installed on NFVIS, although this is a very lengthy CURL command, and is outside the scope of this brief overview.
  
Other possibilities include changing vNICs on a VM, changing the profile of the VM to make the instance larger or smaller, or starting or stopping the VM.  

Another example would be creating a bridge or a network inside NFVIS:  
If we wanted to create a new network called "IMAPEX-net":  
*curl -k -v -u user:passwd -H Content-Type:application/vnd.yang.data+xml https://NFVIS-Server/api/config/networks -d "<network><name>imapex-net</name><bridge>lan-br</bridge></network>"*  
  
![alt-txt](http://10.91.13.171/Files/NFVIS-REST-CreateNetwork-1.PNG)  
![alt-txt](http://10.91.13.171/Files/NFVIS-REST-CreateNetwork-2.PNG)  

  
