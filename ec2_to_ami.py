# FILE: ec2-to-ami.py
# AUTHOR: Zhenyu Zhao
# DESC:
#   This program reads configuration from a seperate module and back up EC2 instances.
#   It also deletes images that is old
# HISTORY:
#   201-12-30 Created

import boto3
import datetime
import time
import sys
from time import mktime
#from time import sleep
# Configuration file in same directory
import ec2_to_ami_config 
import logging

def main():
  # Housekeeping
  logger = logging.getLogger('AMIBackup')
  handler = logging.FileHandler(ec2_to_ami_config.logfile)
  formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
  handler.setFormatter(formatter)
  logger.addHandler(handler)
  logger.setLevel(logging.INFO)
  signature = "_bkp_"

  print "Backup started\n"
  
  # Read server info from config file
  servers = ec2_to_ami_config.servers
  backup_retention = ec2_to_ami_config.backup_retention 

  # Iterate the list
  for server in servers:
    server_id = server['id']
    server_name = server['name']
    #account_profile = server['profile']
    server_name_pattern = server['pattern']
    #server_region = server['region']

    # Get EC2 resouce 
    ec2 = boto3.resource('ec2')
    #print "ec2=", ec2
    # The above commnad returns ec2 = ec2.ServiceResource()
  
    # Get the instance
    instance = ec2.Instance(server_id)

    # tags is a list
    tags = instance.tags
    # Iterate the list 
    for tag in tags:
      # tag is a dictionary 
      if tag['Key'] == 'Name':
         instance_name = tag['Value']
    # for

    # server_name is from config file and instance_name is from instance itself
    print "\n" + server_name + ": " + instance_name + " (" + server_id + ")"  

    # What time is it now?
    current_datetime = datetime.datetime.now()        
    date_stamp = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

    # New image name
    ami_name = instance_name + signature + date_stamp
    print "ami_name=", ami_name

    #
    # Create new AMI
    #
    try:
      # Ruturn type: ec2.Image
      # Return value: image resource
      image = instance.create_image(Name=ami_name)
    except Exception, e:
      # Failed
      logger.error("Backup " + server_name + ": " + e.message)
      # Skip to the next iteration
      continue

    # Succeeded
    logger.info("Backup " + server_name + ": " + ami_name)
    
    print "===AMI creation started=="
    print "AMI name: " + ami_name
 
    # Display image attributes
    #print image.id
    #print image.tags

    # Add a tag containing timestamp
    image.create_tags(Tags=[{'Key': 'Name',
                             'Value': ami_name}])
  
    #  
    # Deregister old images
    #
    print "===Deletion of old AMIs==="
  
    # Get a list of matching images
    filters = [{"Name":"tag:Name", "Values":[server_name_pattern + signature + "*"]}]
    images = ec2.images.filter(Filters = filters)

    for image in images:
      # Get image name 
      for tag in image.tags:
        # tag is a dictionary 
        if tag['Key'] == 'Name':
          image_name = tag['Value']
          print image_name
      # for

      # Get image ID
      #image_id = image.id
      #print image_id

      image_stamp = image_name.replace(server_name_pattern + signature, "")
      image_timestamp = mktime(time.strptime(image_stamp, "%Y-%m-%d_%H-%M-%S"))
      current_timestamp = mktime(current_datetime.timetuple())
      diff_minutes = (current_timestamp - image_timestamp) / 60

      if (diff_minutes > backup_retention):
        image.deregister()
        print image_name + " deleted"
        logger.info("Deleted AMI " + image_name )
      else:
        print image_name + " kept"
        logger.info("Kept AMI " + image_name )
    # for
  # for
 
# End of main()

# If this script is executed as a standalone program, Python's __main__ built-in
# moudle loads the script as a module
if __name__ == '__main__':
  main()
