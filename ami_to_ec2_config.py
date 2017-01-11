#!/usr/bin/python
# Filename: ami_to_ec2_config.py

# File to save the script logs
logfile = "/tmp/ami_to_ec2.log"

# Servers to be backed up
images = [
    dict(
        id = 'ami-0b637b1c', # AMI ID
        name = "Zhen Linux Test Restored", # AMI description
        mincount = 1, # MinCount
        maxcount = 1, # MaxCount
        #keyname='', # access key
        # securitygroup = ['string1', 'string2'], # Security Group 
        #profile = "profile_one", # Account authentication profile name as set in the boto config file
        #region = "eu-west-1", # Region
        instancetype = 't2.micro', # Instance Type
        # placement = {'key': 'value'}, # Placement
        #subnetid='string',        
        #privateipaddress='string', # Private IP address
        pattern = "Zhen Linux Test" # First part of Name tag of the image to restore
        
    ),
]
