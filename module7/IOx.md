# IOx

IOx is an edge computing/fog computing framework for Cisco devices. This
framework enables users to run applications on selected Cisco hardware.  

The devices that IOx runs on are generally small, hardened devices, that are intended to be deployed at the network edge. The serial ports built into the hardware can be accessed by the application, allowing sensors or other devices to be connected to the router and used by the application.

IOx applications can be of three types: PaaS (either Python or Java), VM
(OVA via KVM), or container (LXC).

## IOx hardware

Industrial Routers:  
[IR 809][]  
[IR 829][]

Integrated Services Routers:  
[ISR 819][] - only supported on models with 4G interfaces, 1GB RAM & Flash, and no integrated WiFi.

Industrial Switches:  
[IE4000][] - coming soon!

The [ISR 819][] contains a dual-core, 32-bit Freescale PowerPC based
CPU and 256MB of RAM.

The [IR 809][] and [IR 829][] are 64-bit Intel processor based with 360MB of RAM available.

There is limited support for VM style IOx applications on ISR4k routers as well; however, these applications cannot access router hardware
and do not leverage the Python or Java runtimes available in the other
supported platforms.


[IR 809]: http://www.cisco.com/c/en/us/products/collateral/routers/809-industrial-router/datasheet-c78-734980.html
[IR 829]: http://www.cisco.com/c/en/us/products/collateral/routers/829-industrial-router/datasheet-c78-734981.html
[ISR 819]: http://www.cisco.com/c/en/us/products/collateral/routers/819-integrated-services-router-isr/data_sheet_c78-678459.html
[IE4000]: http://www.cisco.com/c/en/us/products/collateral/switches/industrial-ethernet-4000-series-switches/datasheet-c78-733058.html


## IOx software
There are three software components in the IOx solution.  

Local Director - Built into the IOx image, LD provides for localized management of applications running on a given device.   

[Fog Director][] - Deployed as an OVA, FD is a centralized management solution for IOx applications. It can centrally deploy and upgrade applications as well as monitor the status of applications.

[IOx SDK][] - The IOx SDK includes the tools needed to compile 32 bit PPC applications on a 64-bit Intel based host PC as well as a build system for Yocto Linux and a packaging system to compile applications into deployable application packages.

[Fog Director]: http://www.cisco.com/c/en/us/products/cloud-systems-management/fog-director/index.html
[IOx SDK]: https://software.cisco.com/download/release.html?mdfid=286306005&flowid=79282&softwareid=286306230&release=1.0.0&relind=AVAILABLE&rellifecycle=&reltype=latest

## IOx Capabilities

IOx provides a fully functional Linux environment that applications are hosted by. IOx applications can access the serial ports in the host router; they also have full network access (controlled by standard IOS ACLs).

The simplest type of IOx application is the PaaS type. These applications are developed in [Python][] or [Java][] (currently) and abstract the application away from the host operating system, device drivers, etc. PaaS application packages are quite small as they include only the application code and any needed libraries.

VM type applications include a full operating system ([Yocto Linux][]) in the application bundle. VM applications can be written in any language since they do not run on an IOx provided runtime. VM apps are larger due to the inclusion of the full Yocto environment. VMs utilize [KVM][] for virtualization.

Container applications include the application code, any needed libraries, and a root file system (less the kernel). They are very similar to [Docker][] containers, though the underlying technology used is [LXC][] rather than Docker.

Each platform supports one or more application types. The [compatibility matrix][] on DevNet is the best place to find the most up to date list.

[Python]: http://www.python.org
[Java]: http://www.java.com
[Yocto Linux]: https://www.yoctoproject.org/
[KVM]: http://www.linux-kvm.org/page/Main_Page
[Docker]: https://www.docker.com
[LXC]: https://linuxcontainers.org/
[compatibility matrix]: https://developer.cisco.com/media/iox-dev-guide-7-12-16/platforms/supported-platforms/#platform-support-matrix

## IOx Documentation

Cisco's official repository for IOx documentation is the [DevNet IOx Space][]. There are extensive guides on SDK setup, compiling and installing the example applications, and skeletons for creating new applications.

Example applications in the current SDK release include PaaS, VM, and container applications, written in Python, Java, and C.

The [IOx community][] is also a valuable resource for peer to peer communication with others working with the IOx framework.

[DevNet IOx Space]: https://developer.cisco.com/site/iox/
[IOx community]: https://communities.cisco.com/community/developer/networking/internet-of-things/iox

## IOx Example

An IOx application, in source form, consists of a number of files.

    application.py - main application file
    app-{lxc|vm}.yaml - application description, used with LXC apps
    iox-project-{lxc|vm}.conf - project configuration file used by SDK tools
    makefile - used by make to build and package the application

Note that the application description file and project files are duplicated for the LXC and VM app types because the options needed for each type are different.

### Application Source Code
This example is taken from the SDK example nt03-python_mods. This application can be compiled either as an LXC or VM style application.


    import datetime
    import psutil


    # This program displays the current running processes in tabular form
    def main():
    """ Prints current active processes """
    # Create a format and print table headings
    row_format = "{:<40} {:<10} {:<30} {:<20}"
    print row_format.format("Proc Name", "Proc ID", "Start Time", "Status",
                            "Priority")
    print "-" * 100
    # Iterate over all running processes
    for proc in psutil.process_iter():
        # Get process create time in the standard time format
        time = datetime.datetime.fromtimestamp(proc.create_time()).strftime(
        "%Y-%m-%d %H:%M:%S")
        # Print process's name, pid, create time and status in a table format
        print row_format.format(proc.name(),
                                proc.pid,
                                time,
                                proc.status())

As you can see there is nothing special about the Python code - it is no different than an application written for any other platform. This feature of the IOx platform makes it simple to write and test applications on a developer's workstation for much of the development cycle before access to physical hardware is required.

Full copies of the example project files:

[python-c-app.py](python-c-app.py)  
[Makefile](Makefile)  
[app-lxc.yaml](app-lxc.yaml)  
[app-vm.yaml](app-vm.yaml)  
[iox-project-lxc.conf](iox-project-lxc.conf)  
[iox-project-vm.conf](iox-project-vm.conf)  

## Tips

IOx is a very new and rapidly evolving technology. It has a number of quirks to be aware of.

### The build

The most complex and time consuming part of the build process is creating the Yocto Linux image needed for the application. It is highly advisable to utilize a single Yocto build directory for all applications as the image rarely changes. This should be located outside the SDK directory since the contents of the SDK directory may be removed by future installations of the SDK.

This can be done in the example applications by passing YOCTO_PROJECT_DIR on the make command line:  

    make YOCTO_PROJECT_DIR=~/yp YOCTO_MACHINE=isr800-lxc  

That same Yocto directory can be leveraged in your own applications by referencing it in your build process.

### IOS

Only very new IOS images include IOx support. 15.6(1)T1 is the first version supported by the 1.1.0.0 SDK.

### Testing

Real hardware is always the best for testing. If you have access to a suitable router, AT&T offers a Jasper SIM for IOT developers for $11. The SIM includes 300MB of data as well as SMS messaging access and works for 6 months. Visit http://starterkit.att.com for details and ordering.

It is rumored that a data SIM can be added to corporate paid cell phone plans for $10/month but I have been unable to verify that.
