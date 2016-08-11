# Programmability and UCS

Cisco UCS was architected as **programmable infrastructure** from its inception seven years ago. Cisco offers application program interfaces (APIs), tools, orchestration and integration to meet coding requirements.

### Unified UCS Management

The latest release of *UCS Manager, version 3.1*, brings together support for the 2nd generation UCS hardware and the latest 3rd UCS hardware. This includes UCS Mini, UCS B-Series and C-Series servers, Cisco Hyperflex, and Cisco composable infrastructure. It also features a new HTML5 interface.

![UCS Programmability](http://blogs.cisco.com/wp-content/uploads/bog-ucs-management-02.jpg)

### UCS PowerTool Suite

*UCS Manager 3.1* is supplemented by some great programmability tools. *UCS PowerTool 2.0* suite supports *Microsoft's Desired State Configuration* (DSC), PowerTools has a unified Installer, support for UCS Manager, UCS Central, and UCS Integrated Management Controller (IMC) on C-Series and E-Series, as well as consolidation of duplicated Cmdlets across the suite. For example, **Set-UcsCentralConfiguration**, and **Set-UcsPowerToolConfiguration** are combined into **Set-UcsPowerToolConfiguration**. These changes as well as a listing of all the newly added Cmdlets are fully described in the [UCS PowerTool Release Notes](http://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/sw/msft_tools/powertools/powertools_releasenotes/Pwrtool_RN_2x.html "Title").

And the software is available [here](https://software.cisco.com/download/release.html?mdfid=286305108&flowid=&softwareid=284574017&release=2.0.1&relind=AVAILABLE&rellifecycle=&reltype=latest "Title").

*UCS PowerTool* includes a **ConvertTo-UcsDSCConfig** Cmdlet, which generates DSC configuration code based on actions carried out in the UCS Manager GUI. Utilize the **ConvertTo-UcsDSCConfig** Cmdlet along with the DSC support for UCS Objects, syncing a UCS Object from a reference UCS Domain, syncing a UCS Object from a backup or running a script to bring UCS Objects to their desired state.

### UCS Python SDK

There is also *UCS Manager Python SDK* in the final stages of development. The UCS Manager Python SDK is currently hosted on *github* under the [CiscoUcs](https://github.com/CiscoUcs "Title") account. While the SDK is currently in beta, you can folow the progress of the UCS Python SDK in the UCS section of [Cisco Communities](https://communities.cisco.com/docs/DOC-64378 "Title") and check out the ever growing library of [UCS Manager Python SDK samples](https://github.com/CiscoUcs/ucsmsdk_samples "Title") as well as the [documentation](https://github.com/CiscoUcs/ucsmsdk_docs "Title").

### Open XML APIs

UCS PowerTool and the Python SDK are built on top of the UCS Management open XML APIs. These tools compose the XML needed for the XML request and parse the response. Optionally, you could always manipulate the XML API directly. There are user guides for each of the UCS XML API choices. As long as the programming language you want to use supports writing an HTTP client or use utilies like curl or Postman to quickly prototype.

* [Cisco UCS Manager XML API Programmer's Guide](http://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/sw/api/b_ucs_api_book.html "Title")
* [Cisco UCS Rack-Mount Servers CIMC XML API Programmer's Guide](http://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/c/sw/api/b_cimc_api_book.html "Title")
* [Cisco UCS Central XML API Programmer's Guide](http://www.cisco.com/c/en/us/products/servers-unified-computing/ucs-central-software/index.html "Title")

### UCS Emulator

The [UCS Platform Emulator 3.1](https://communities.cisco.com/docs/DOC-66688 "Title") provides developers their own UCS system, so they don't have to work on systems in production. The UCS Platform Emulator is built on the same as the actual product. Code that is written against the emulator works with UCS Manager.

The emulator also has the complete *UCS Manager Object Model Documentation*. The Object Model Documentation has all of the classes, methods, faults, syslog messages, and more. Another benefit is that one or more UCS Platform Emulators can be registered to *UCS Central*, to truly represent a real UCS deployment. The UCS Platform emulator is an integral part of the offerings at Cisco dCloud, for example the [Application Policy Infrastructure Controller 1.2 with Cisco CloudCenter 4.5 v1](https://dcloud-cms.cisco.com/?p=23113 "Title"), dCloud offering utilizes the 3.1 UCS Platform Emulator.

An example of working with the UCS Platform Emulator and the Python SDK is [here](UCSPE_Example.md)

### Free Tools and Community Support

The *UCSX PowerTool Suite 2.X*, the *Python UCS Manager SDK*, the *Python UCS IMC SDK*, and the *UCS Platform Emulator* are all **free** to customers and partners. And the UCS Programmability tools have [community support](https://communities.cisco.com/community/technology/datacenter/compute-and-storage/ucs_management "Title") and are represented in [Cisco DevNet](https://developer.cisco.com/site/ucs-dev-center/index.gsp "Title").

### UCS Central

[UCS Central](http://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/release/notes/RN-CiscoUCSCentral_1-4.html "Title") was recently updated with a significant number of new capabilities, an HTML5 interface and a new task based orientation. Even customers with only one UCS system should be using UCS Central. UCS management over multiple UCS systems through UCS Central is programmable and automated as the other UCS management options via [UCS Central PowerTool](http://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/sw/msft_tools/UCS_Central/powertools/user_guide/ucsc_pwrtool_ug_2x.html "Title") or the [UCS Central XML API](http://www.cisco.com/c/en/us/products/servers-unified-computing/ucs-central-software/index.html "Title").

PowerShell, Python, the emulator, and all Cisco UCS products provide the advantage of programmatic capabilities the UCS management options have to offer.
