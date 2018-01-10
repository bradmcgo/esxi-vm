import os.path

import sys
import yaml
import datetime                   # For current Date/Time
from math import log


#
#
#   Functions
#
#


def setup_config():

    #
    #   System wide defaults
    #
    config_data = dict(

        #   Your logfile
        LOG=os.path.expanduser("~") + "/esxi-vm.log",

        #  Enable/Disable dryrun by default
        isDryRun=False,

        #  Enable/Disable Verbose output by default
        isVerbose=False,

        #  Enable/Disable exit summary by default
        isSummary=False,

        #  ESXi host/IP, port, root login & password
        HOST="esxi",
        PORT=22,
        USER="root",
        PASSWORD="",
        KEY="",

        #  Default number of vCPU's, GB Mem, & GB boot disk
        CPU=2,
        MEM=4,
        HDISK=20,

        #  Default Disk format thin, zeroedthick, eagerzeroedthick
        DISKFORMAT="thin",

        #  Virtual Disk device type
        VIRTDEV="pvscsi",

        #  Specify default Disk store to "LeastUsed"
        STORE="LeastUsed",

        #  Default Network Interface (vswitch)
        NET="None",

        #  Default ISO
        ISO="None",

        #  Default GuestOS type.  (See VMware documentation for all available options)
        GUESTOS="centos-64",

        # Extra VMX options
        VMXOPTS=""
    )

    config_data_file_location = os.path.expanduser("~") + "/.esxi-vm.yml"

    #
    # Get ConfigData from ConfigDataFile, then merge.
    #
    if os.path.exists(config_data_file_location):
        from_file_config_data = yaml.safe_load(open(config_data_file_location))
        config_data.update(from_file_config_data)

    try:
        with open(config_data_file_location, 'w') as FD:
            yaml.dump(config_data, FD, default_flow_style=False)
        FD.close()
    except:
        print("Unable to create/update config file {}".format(config_data_file_location))
        e = sys.exc_info()[0]
        print("The Error is {}".format(e))
        sys.exit(1)
    return config_data


def save_config(config_data):
    config_data_file_location = os.path.expanduser("~") + "/.esxi-vm.yml"
    try:
        with open(config_data_file_location, 'w') as FD:
            yaml.dump(config_data, FD, default_flow_style=False)
        FD.close()
    except:
        print("Unable to create/update config file {}".format(config_data_file_location))
        e = sys.exc_info()[0]
        print("The Error is {}".format(e))
        return 1
    return 0


def the_current_date_time():
    i = datetime.datetime.now()
    return str(i.isoformat())
