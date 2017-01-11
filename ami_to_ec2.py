# FILE: ami_to_ec2.py
# AUTHOR: Zhenyu Zhao
# DESC:
#   This program reads configuration from a seperate file/module and then 
#   restore EC2 instances from AMIs
# HISTORY:
#   2017-1-9 Created

import boto3
import datetime
import time
import sys
from time import mktime
# Configuration file in same directory
import ami_to_ec2_config 
import logging

def main():
  # Housekeeping
  logger = logging.getLogger('ami_to_ec2')
  handler = logging.FileHandler(ami_to_ec2_config.logfile)
  formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
  handler.setFormatter(formatter)
  logger.addHandler(handler)
  logger.setLevel(logging.INFO)
  signature = "_bkp_"

  print "Restore started\n"
  
  # Read image info from config file
  images = ami_to_ec2_config.images

  # Get EC2 resouce 
  ec2 = boto3.resource('ec2')
  #print "ec2=", ec2
  # The above commnad returns ec2 = ec2.ServiceResource()

  # Iterate the list
  for image in images:
    argv = {}

    image_id = image['id']
    if image_id:
      argv['ImageId'] = image_id

    min_count = image['mincount']
    if min_count:
      argv['MinCount'] = int(min_count)

    max_count = image['maxcount']
    if max_count:
      argv['MaxCount'] = int(max_count)

    instance_type = image['instancetype']
    if instance_type:
      argv['InstanceType'] = instance_type

    server_name_pattern = image['pattern']

    # Create instances
    instances = ec2.create_instances(**argv)
    for instance in instances:
      print instance.id
     
      # What time is it now?
      current_datetime = datetime.datetime.now()
      date_stamp = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

      # Add a Name tage to the instance
      instance.create_tags(Tags=[{'Key': 'Name',
                                  'Value': server_name_pattern + 'Restored' + ' ' + date_stamp}])
    # for

  # for

  #print "We are dne here"
 
# End of main()

# If this script is executed as a standalone program, Python's __main__ built-in
# moudle loads the script as a module
if __name__ == '__main__':
  main()
