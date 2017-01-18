# FILE: ami_to_ec2_config.py
# AUTHOR: Zhenyu Zhao
# DESC:
#   This module is config module to be imported by ami_to_ec2
# HISTORY:
#   2017-1-1 Created

# Logfile pathname
logfile = "/tmp/ami_to_ec2.log"

# AMIs to be launched
images = [
    dict(
        id = 'ami-1ae1090c', # AMI ID
        name = "Zhen Linux Test Restored", # AMI description
        mincount = 1, # MinCount
        maxcount = 1, # MaxCount
        #keyname='', # access key
        securitygroup = ['launch-wizard-17'], # Security Group 
        #profile = "profile_one", # Account authentication profile name as set in the boto config file
        #region = "eu-west-1", # Region
        instancetype = 't2.micro', # Instance Type
        #placement = {'key': 'value'}, # Placement
        #subnetid='string',        
        #privateipaddress='string', # Private IP address
        pattern = "Zhen Linux Test" # First part of Name tag of the image to restore
    ),
    dict(
        id = 'ami-a3e40cb5', # AMI ID
        name = "Zhen Linux Test Restored", # AMI description
        mincount = 1, # MinCount
        maxcount = 1, # MaxCount
        #keyname='', # access key
        securitygroup = ['launch-wizard-20'], # Security Group 
        #profile = "profile_one", # Account authentication profile name as set in the boto config file
        #region = "eu-east-1", # Region
        instancetype = 't2.medium', # Instance Type
        #placement = {'key': 'value'}, # Placement
        #subnetid='string',        
        #privateipaddress='string', # Private IP address
        pattern = "Zhen Linux Test" # First part of Name tag of the image to restore
    ),
]
