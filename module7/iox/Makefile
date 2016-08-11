#
# @file
#	Makefile
#
# @description
#	Makefile for building an IOx native application which runs on
#	Python 2.7 and brings its own python modules
#
# @copyright
#	Copyright (c) 2015-2016 by Cisco Systems, Inc.
#	All rights reserved.
#

# Include common definitions and utilities makefile fragment
include ../shared/prologue.mk


# Select the target machine to build this application for
#YOCTO_MACHINE ?= ie4k-lxc
YOCTO_MACHINE ?= ir800-lxc
#YOCTO_MACHINE ?= isr800-lxc
#YOCTO_MACHINE ?= isr800-qemu
YOCTO_VERSION = 1.7

# Base image - this application needs python interpreter
YOCTO_IMAGE_TARGET = iox-core-image-python

# This application performs rootfs image post processing; we need .tar.gz from Yocto
ROOTFS_IMAGE_POSTPROCESSING = 1

# Include common definitions and utilities for native apps
# Note: Must have defined the following variables before including this one
# - YOCTO_MACHINE
# - YOCTO_VERSION
# - YOCTO_IMAGE_TARGET
# - ROOTFS_IMAGE_POSTPROCESSING
include ../shared/native.mk

# Yocto mirror location (optional)
YOCTO_MIRROR ?=

# External mirror (default, downloads from the internet)
PYPI = https://pypi.python.org

# Mirrors for downloading 3rd party python module sources
PYPY_MIRROR ?=

# The python application included in this project
PYTHON_APP = src/python-c-app.py

# Python modules' tar files will be extracted here
PKG_EXTRACTED_DIR = $(OUTPUT_YOCTO_MACHINE_DIR)/pkg-extracted

# Root directory to do an intermediate install of python modules
MODULES_DIR = $(abspath $(OUTPUT_YOCTO_MACHINE_DIR)/python-modules)

# The path where the python modules installed locally
SITE_PKGS_DIR = $(MODULES_DIR)/usr/lib/python2.7/site-packages

# Module for the target system.
# Add modules' names to be installed in $(MODULES_LIST)
# This application requires just one module, but user can add multiple modules in 'MODULES_LIST'
MODULES_LIST = \
	psutil-2.0.0

#
# Default Makefile Target
#
all: setup $(APP_PKG) teardown

#
# Application specific setup of project
# This setup ensures that the right local.conf is configured for the project
#
.PHONY = setup
setup: setup_common

#
# Create the application package
#
$(APP_PKG): $(APP_PKG_DESCRIPTOR) $(OUTPUT_ROOTFS_IMAGE) $(OUTPUT_KERNEL_IMAGE)
	$(call separator)
	@echo "Creating the application package..."
	@cd $(OUTPUT_DIR) && \
		$(IOX) package create --proj-file $(PROJECT_CONFIG) --img-id $(YOCTO_MACHINE)
	mv $(OUTPUT_DIR)/application.tar $@
	@echo "Done"

# Command set to use to generate a new LXC rootfs
ROOTFS_REPACK_SCRIPT = \
	$(IMG_BLDR) -c extract -d $(ROOTFS_STAGING_DIR) -i $(abspath $<) && \
	cp $(PYTHON_APP) $(ROOTFS_STAGING_DIR)/usr/bin/ && \
	cp -ua $(MODULES_DIR)/* $(ROOTFS_STAGING_DIR) && \
	$(IMG_BLDR) -c pack -p $(YOCTO_PROJECT_DIR) -d $(ROOTFS_STAGING_DIR) -r 0.5 -a 1 -i $@

#
# Ready the final rootfs image using the one built by Yocto build system
# For this application, the python app and module are inserted
#
$(OUTPUT_ROOTFS_IMAGE): $(YOCTO_ROOTFS_IMAGE) $(addprefix $(MODULES_DIR)/, $(addsuffix .setup_done, $(MODULES_LIST)))
	$(call separator)
	$(call mk_dir,$(@D))
	$(RM) -rf $(ROOTFS_STAGING_DIR)
	$(RM) -rf $@
	$(call mk_dir,$(ROOTFS_STAGING_DIR))
	@echo -e "$(ROOTFS_REPACK_SCRIPT)" | $(FAKEROOT);
	@echo "Done"

#
# Copy the kernel to the staging directory.
# This application doesn't modify the kernel, copy as is
#
$(OUTPUT_KERNEL_IMAGE): $(YOCTO_KERNEL_IMAGE)
	$(call separator)
	$(call mk_dir,$(@D))
	cp $< $@
	touch $@
	@echo "Done"

#
# Build the Yocto rootfs image
# If the Yocto project configuration file is modified, we want to rebuild the image
#
$(YOCTO_ROOTFS_IMAGE): $(YOCTO_PROJECT_LOCAL_CONF)
	$(call separator)
	@echo "Building image: $(YOCTO_IMAGE_TARGET)..."
	@cd $(YOCTO_PROJECT_DIR) && \
		source ./SOURCEME && \
		bitbake $(YOCTO_IMAGE_TARGET) -c clean && \
		bitbake $(YOCTO_IMAGE_TARGET)
	@echo "Done"

#
# Target to cross compile the python modules
# Generally yocto sets variables (Example: BUILD_SYS, HOST_SYS etc) while building the image.
# Since we are not using Yocto to build the modules, default values are set for BUILD_SYS and HOST_SYS.
# STAGING_LIBDIR & STAGING_INCDIR: target sysroot library and include dir.
#
$(MODULES_DIR)/%.setup_done: $(addprefix $(PKG_EXTRACTED_DIR)/, %) $(MODULES_DIR) $(BUILD_ENV_FILE)
	$(call separator)
	$(call mk_dir,$(@D))
	@source $(BUILD_ENV_FILE); \
	export LDSHARED="$${CC} -pthread -shared"; \
	export CFLAGS="-I$${SDKTARGETSYSROOT}/usr/include/python2.7/"; \
	export PYTHONPATH=$${PYTHONHOME}/usr/lib/python2.7:$${PYTHONHOME}/usr/lib/python2.7/lib-dynload; \
	export BUILD_SYS=""; \
	export HOST_SYS=""; \
	export STAGING_LIBDIR=$${SDKTARGETSYSROOT}/usr/lib; \
	export STAGING_INCDIR=$${SDKTARGETSYSROOT}/usr/include; \
	echo "Setting up: $<..."; \
	cd $<; \
	$${PYTHONHOME}/bin/python-native/python2.7 \
	setup.py install -v --compile --root=$(@D) --prefix=usr; \
	if [ $${?} -ne 0 ]; then \
		echo "Error while installing python module: $<! Exiting..."; \
		exit 1; \
	fi; \
	cd -;
	@echo "Removing \"egg-info\" metadata..."
	@$(RM) -rf $(DIST_PKGS_DIR)/*.egg-info
	@touch $@
	@echo "Done"

#
# Create directory to install python modules
#
$(MODULES_DIR):
	$(call separator)
	@echo "Creating directory to setup python modules: $(@D)..."
	$(call mk_dir,$(@D))

#
# Extract python modules' tar packages
#
.PRECIOUS: $(PKG_EXTRACTED_DIR)/%
$(PKG_EXTRACTED_DIR)/%: $(DOWNLOAD_DIR)/%.tar.gz
	$(call separator)
	$(call mk_dir,$(@D))
	@echo "Extracting $< to get $@"
	tar -zxvf $< -C $(@D)
	touch $@
	@echo "Done"

#
# Target to fetch sources and validate them
#
.PRECIOUS: $(DOWNLOAD_DIR)/%.tar.gz
$(DOWNLOAD_DIR)/%.tar.gz:
	$(call separator)
	$(call mk_dir,$(@D))
	@cd $(@D); \
	rc=0; \
	archive_name=$(@F); \
	echo "Downloading source archive: $${archive_name}..."; \
	if [ -z "$(PYPY_MIRROR)" ]; then \
		echo "Downloading from internet: ${PYPI}"; \
		DOWNLOAD_URL="${PYPI}/packages/source/$${archive_name:0:1}/$${archive_name%-*}/$${archive_name}"; \
		wget --no-clobber $${DOWNLOAD_URL}; \
	else \
		echo "Downloading from mirror: $(PYPY_MIRROR)"; \
		cp -u $(PYPY_MIRROR)/$${archive_name} .; \
	fi; \
	if [ $${?} -ne 0 ]; then \
		echo "Error while downloading sources! Exiting..."; \
		exit 1; \
	fi;
	@echo "Validating archive: $@..."
	@tar -tzf $@ > /dev/null 2>&1; \
	if [ $${?} -ne 0 ]; then \
		echo "Not a valid archive: $@"; \
		exit 1; \
	fi;
	@touch $@
	@echo "Done"

#
# Creates build environment setup file
#
$(BUILD_ENV_FILE): $(YOCTO_ROOTFS_IMAGE)
	$(call separator)
	@echo "Creating build environment setup file..."
	$(IOX) ldsp execute yocto-1.7 buildenv create -p $(YOCTO_PROJECT_DIR)
	@echo "Done"

#
# Application specific cleanup tasks after each run
#
.PHONY = teardown
teardown:

#
# Remove some of the output files created by the build process
#
clean:
	$(call separator)
	@echo "Cleaning up application generated files..."
	$(RM) -rf $(APP_PKG) $(OUTPUT_YOCTO_MACHINE_DIR) $(PKG_EXTRACTED_DIR)
	@echo "Done"

#
# Remove all output files created by the build process
#
cleanall: clean
	$(call separator)
	@echo "Cleaning up all build generated files..."
	$(RM) -rf $(OUTPUT_DIR)
	@echo "Removing downloaded files..."
	$(RM) -rf $(DOWNLOAD_DIR)
	@echo "Done"

#
# Simple debug target to debug this Makefile
#
debug:
	$(call separator)
	$(call debug_common)
	$(call debug_native)

.PHONY: cleanall clean debug
