#!/usr/bin/python
# Filename: ami_backup_config.py

# example of config file
# time in minutes AMI images will be kept for
#backup_retention =  10080 # 7 days
backup_retention =  60 # 60 minutes
# File to save the script logs
logfile = "/tmp/ec2_to_ami.log"
# Servers to be backed up
servers = [
    dict(
        id = 'i-0002dab6e11437025', # Instance ID
        name = "Zhen Linux Test", # Server description
        #profile = "profile_one", # Account authentication profile name as set in the boto config file
        #region = "eu-west-1", #ec2 server region
        pattern = "Zhen Linux Test" # First part of Name tag of the server to backup
    ),
]
