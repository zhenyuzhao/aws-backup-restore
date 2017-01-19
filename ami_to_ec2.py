# FILE: ami_to_ec2.py
# AUTHOR: Zhenyu Zhao
# DESC:
#   This program reads configuration from config module and then 
#   launch EC2 instances from AMIs
# HISTORY:
#   2017-1-1 Created

import boto3
import datetime
import time
import sys
from time import mktime
import logging
# Custom config module in same directory
import ami_to_ec2_config 

def main():
  # Get a logger object
  logger = logging.getLogger('ami_to_ec2')
  # Get logfile pathname from config module
  logfile = ami_to_ec2_config.logfile
  # Associate logfile with logger
  handler = logging.FileHandler(logfile)
  formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
  handler.setFormatter(formatter)
  # Associate logfile with logger again
  logger.addHandler(handler)
  logger.setLevel(logging.INFO)
  signature = "_bkp_"

  print "Restore started"
  
  # Get list of images info from config file
  images = ami_to_ec2_config.images

  # Create a default session
  # Create a EC2 resource 
  # The below statement returns ec2.ServiceResource()
  try:
    ec2 = boto3.resource('ec2')
  except Exception, e:
    # Failed
    logger.error("Resource ec2 creation: " + e.message)
    print "Error: " + e.message
    return

  # Iterate the list of images
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

    security_group = image['securitygroup']
    if security_group:
      argv['SecurityGroupIds'] =  security_group

    instance_type = image['instancetype']
    if instance_type:
      argv['InstanceType'] = instance_type

    server_name_pattern = image['pattern']

    # Create instances
    try:
      instances = ec2.create_instances(**argv)
    except Exception, e:
      # Failed
      logger.error("Resource ec2 creation: " + e.message)
      print "Error: " + e.message
      # Skip the current iteration pass
      continue

    for instance in instances:
      print "AMI ID=" + image_id + "==>" + "Instance ID=" + instance.id
     
      # What time is it now?
      current_datetime = datetime.datetime.now()
      date_stamp = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

      # Add a Name tage to the instance
      instance.create_tags(Tags=[{'Key': 'Name',
                                  'Value': server_name_pattern + ' Restored ' + ' ' + date_stamp}])
    # for
  # for

  print "Restore ended"
# End of main()

# If this script is executed as a standalone program, Python's __main__ built-in
# moudle loads the script as a module
if __name__ == '__main__':
  main()
