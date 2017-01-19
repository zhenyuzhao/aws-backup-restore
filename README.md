This repo contains two Python scripts intended for backup and restore of EC2 instances.

The Cloud code snippet assignemnt requirements are: 
Design a Windows/Linux EC2 backup strategies using AMI
- Research on various backup/restore strategies using AMI
- Script the process to schedule the AMI creation
- Script the process to use the AMI creation
- Incorporate all the configuration changes required for the new instance to be functional

Two programs are: 
1. Backup: ec2_to_ami.py and ec2_to_ami_config.py
2. Restore: ami_to_ec2.py and ami_to_ec2_config.py

ec2_to_ami.py uses ec2_to_ami_config.py while ami_to_ec2.py uses ami_to_ec2_config.py
