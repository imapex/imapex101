#Routers and Switches

We are currently at an inflection point when it comes to the ability to device programability directly to a router or switch. NETCONF was extended into IOS in 2005 but the lack of a consistent data model limited adoption. Depending on the platform there are multiple options for accessing the deivce directly.

##WSMA - Web Services Management Agent

WSMA was Cisco's first real attempt at exposing the router to programitic interfaces. The WSMA relies on the integrated HTTP server to allow for sending data in an XML format. 

To enable the WSMA

~~~
ip http authentication localip http secure-serverwsma agent exec profile httpslistenerwsma agent config profile httpslistenerwsma profile listener httpslistener transport https~~~

Once enabled a user can send XML to either set configruaiton or request statistics through show commands. In the example below a user is requesting 'show interface gig2' from a router.

~~~
<?xml version="1.0" encoding="UTF-8"?> <SOAP:Envelope xmlns:SOAP="http://schemas.xmlsoap.org/soap/envelope/" xmlns:SOAP-ENC="http://schemas.xmlsoap.org/soap/encoding/" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><SOAP:Header>  <wsse:Security xmlns:wsse="http://schemas.xmlsoap.org/ws/2002/04/secext"  SOAP:mustUnderstand="false">      <wsse:UsernameToken>         <wsse:Username>cisco</wsse:Username>         <wsse:Password>cisco</wsse:Password>       </wsse:UsernameToken></wsse:Security></SOAP:Header> <SOAP:Body>  <request xmlns="urn:cisco:wsma-exec" correlator="show int gig1">   <execCLI maxWait="PT100S" xsd="false">    <cmd>show int gig2</cmd>   </execCLI>  </request> </SOAP:Body></SOAP:Envelope>~~~
The router sends the following response

~~~
 <response             xmlns="urn:cisco:wsma-exec" correlator="show int gig1" success="1">            <execLog>                <dialogueLog>                    <sent>show int gig1</sent>                    <received>                        <text>GigabitEthernet1 is up, line protocol is up   Hardware is CSR vNIC, address is fa16.3e4d.d212 (bia fa16.3e4d.d212)  Internet address is 10.203.30.98/24  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec,      reliability 255/255, txload 1/255, rxload 1/255  Encapsulation ARPA, loopback not set  Keepalive set (10 sec)  Full Duplex, 1000Mbps, link type is auto, media type is RJ45  output flow-control is unsupported, input flow-control is unsupported  ARP type: ARPA, ARP Timeout 04:00:00  Last input 00:00:00, output 00:00:38, output hang never  Last clearing of &quot;show interface&quot; counters never  Input queue: 0/375/628/0 (size/max/drops/flushes); Total output drops: 0Queueing strategy: fifo  Output queue: 0/40 (size/max)  5 minute input rate 12000 bits/sec, 26 packets/sec  5 minute output rate 0 bits/sec, 0 packets/sec     9749975 packets input, 586616472 bytes, 0 no buffer     Received 0 broadcasts (0 IP multicasts)     0 runts, 0 giants, 0 throttles      0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored     0 watchdog, 0 multicast, 0 pause input     37239 packets output, 3670630 bytes, 0 underruns     0 output errors, 0 collisions, 1 interface resets     3999 unknown protocol drops     0 babbles, 0 late collision, 0 deferred     0 lost carrier, 0 no carrier, 0 pause output     0 output buffer failures, 0 output buffers swapped out</text>                    </received>                </dialogueLog>            </execLog>        </response>~~~

The challenge with using WSMA is the command strucute is fairly picky. Command strings sent are essentially CLI which means any variation in platform CLI will require script modification.

Adam Radford wrote a series of python scripts that leverage WSMA to provide basic router management. You can access his git repository at

~~~
https://github.com/aradford123/wsma_python
~~~

##Netconf/YANG
In 2012 Cisco started standardizing on Netconf/YANG as the methodoly for direct programming of IOS devices. For routing platforms we started introducing Netconf/YANG in IOS-XE 3.17 while the rest of the platforms saw support added with Polaris (IOS 16.x). 

To validate what a device can support use

~~~
ssh -p2022 -l sdn <host address> -s netconf  ~~~

The device will respond back with all the various model types supported. 


