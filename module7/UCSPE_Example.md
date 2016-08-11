# UCS Platform Emulator Examples

The UCS Platform Emulator provides developers their own UCS system, so they don't have to work on systems in production. The UCS Platform Emulator is built on the same code as the actual product. Code that is written against the emulator works with UCS Manager.

### Running UCS Platform Emulator in VirtualBox

Running the UCS Platform Emulator 3.1 in VirtualBox is possible with some simple tweaks. This makes it possible to avoid installing a VMware Fusion, Player, or Workstation application to get the full functionality of the emulator.

The trick is to download the [UCS Platform Emulator 3.1](https://communities.cisco.com/docs/DOC-66688 "Title") VM as a .zip file from the [downloads](https://communities.cisco.com/docs/DOC-67121 "Title") page, and then convert the VM into an OVA with the VMware OVF tool available [here](https://my.vmware.com/web/vmware/details?downloadGroup=OVFTOOL400&productId=353 "Title"). The command to create the OVA is something like **ovftool ucspe.vmx ucspe.ova**. Then import the OVA into VirtualBox and it should run without problems.

To access the UCS Platform Emulator after it starts, I created a Host-only Network with a DHCP server in the VirtualBox preferences and used Host-only Adapters for all three of the virtual NICS configured on the UCS Platform Emulator VM.

### Install UCS Manager Python SDK

You can ignore this step if you already have pip installed.

	wget https://bootstrap.pypa.io/get-pip.py
	python get-pip.py
	
This command will install the latest released version of the UCS Manager Python SDK.

	pip install ucsmsdk
	
If you want the latest development version, use git (this assumes you already have git installed on your workstation).

	git clone https://github.com/CiscoUcs/ucsmsdk.git
	cd ucsmsdk
	make install

### Logging into the UCS Platform Emulator via Python

Once the emulator is running and has a working network configuration in VirtualBox and you have installed the UCS Manager Python SDK, you can login to the UCS Platform Emulator with Python.

From the Python shell execute:

	from ucsmsdk.ucshandle import UcsHandle
	handle = UcsHandle("192.168.0.1","username","password")
	handle.login()
	
Then launch the UCS GUI from the current Python session:

	from ucsmsdk.utils import ucsguilaunch
	ucsguilaunch.ucs_gui_launch(handle)
	
## Use the Converttopython tool
	
Now we can begin to generate Python code as we make changes to the UCS system configuration within the GUI.

	from ucsmsdk.utils import converttopython
	converttopython.convert_to_ucs_python()
	
Python script will be generated in the Python shell terminal, and it can be used to automate the UCS operations through the scripting language.

For example, adding a common VLAN through the UCS GUI generated the following script.

	from ucsmsdk.mometa.fabric.FabricVlan import FabricVlan

	mo = FabricVlan(parent_mo_or_dn="fabric/lan", sharing="none", name="101", id="101", 	mcast_policy_name="", policy_owner="local", default_net="no", pub_nw_name="", 	compression_type="included")
	handle.add_mo(mo)

	handle.commit()
	
From this bit of code, it's simple to change values or add variables to generate complex scripts that can be used to automate common tasks that would take much longer to accomplish in the GUI.



	
