#!/usr/bin/python

# FILE: ec2_to_ami_config.py
# AUTHOR: Zhenyu Zhao
# DESC:
#   Configuration module for ec2_to_ami.py
# HISTORY:
#   2017-1-2 Created

# Time in minutes AMI images will be kept for
backup_retention =  60 # 60 minutes
# File to save the script logs
logfile = "/tmp/ec2_to_ami.log"
# Servers to be backed up
servers = [
    dict(
        id = 'ii-0002dab6e11437025', # Instance ID
        name = "Zhen Linux Test", # Server name
        #profile = "profile_one", # Account authentication profile name as set in the boto config file
        #region = "eu-east-1", #ec2 server region
        pattern = "Zhen Linux Test" # First part of Name tag of the server to backup
    ),
    dict(
        id = 'ii-0387a522860c0f5b0', # Instance ID
        name = "Zhen Windows Test", # Server name
        #profile = "profile_one", # Account authentication profile name as set in the boto config file
        #region = "eu-east-1", #ec2 server region
        pattern = "Zhen Windows Test" # First part of Name tag of the server to backup
    ),
]
