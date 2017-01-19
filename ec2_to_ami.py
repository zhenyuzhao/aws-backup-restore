# FILE: ec2_to_ami.py
# AUTHOR: Zhenyu Zhao
# DESC:
#   This program reads configuration from a seperate module and then back up EC2 instances.
#   It also deletes images that is older than what the retention ploicy specifies.
# HISTORY:
#   201-12-30 Created

import boto3
import datetime
import time
import sys
from time import mktime
import logging
# Configuration file in same directory
import ec2_to_ami_config 

def main():
  # Instantiate a logger object
  logger = logging.getLogger('ec2_to_ami')
  # Get logfile pathname from config module
  logfile = ec2_to_ami_config.logfile
  # Associate logfile with logger
  handler = logging.FileHandler(logfile)
  formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
  handler.setFormatter(formatter)
  # Associate logfile with logger again
  logger.addHandler(handler)
  logger.setLevel(logging.INFO)
  signature = "_bkp_"

  print "Backup started"
  
  # Get a list of servers from config module
  servers = ec2_to_ami_config.servers

  # Get AMI retention policy from config module
  backup_retention = ec2_to_ami_config.backup_retention 

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

  #
  # Iterate the list of servers
  # Each server is a dictionary object 
  #
  for server in servers:
    server_id = server['id']
    server_name = server['name']
    #account_profile = server['profile']
    server_name_pattern = server['pattern']
    #server_region = server['region']

    # Get the instance
    # returned is an object
    instance = ec2.Instance(server_id)

    # Returned is a list of dictionary elements
    tags = instance.tags
    # Iterate the list 
    for tag in tags:
      # tag is a dictionary 
      if tag['Key'] == 'Name':
         instance_name = tag['Value']
    # for

    # server_name is from config file and instance_name is from instance itself
    print server_name, ": ", instance_name, " (", server_id, ")"  

    # What time is it now?
    current_datetime = datetime.datetime.now()        
    date_stamp = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")

    # New image name
    ami_name = instance_name + signature + date_stamp

    #
    # Create AMI
    #
    try:
      # Ruturned type: ec2.Image
      # Returned value: image resource
      image = instance.create_image(Name=ami_name)
    except Exception, e:
      # Failed
      logger.error("Backup " + server_name + ": " + e.message)
      print "Error: " + e.message
      # Skip the current iteration pass
      continue

    # Succeeded
    logger.info("Backup " + server_name + ": " + ami_name)
    
    print "\t", "Instance ID=" + server_id + "===>" + "AMI name=" + ami_name
 
    # Display image attributes
    #print image.id
    #print image.tags

    # Add a tag containing name 
    image.create_tags(Tags=[{'Key': 'Name',
                             'Value': ami_name}])
  
    # Add a tag containing name timestamp
    image.create_tags(Tags=[{'Key': 'CreateTime',
                             'Value': date_stamp}])

    #  
    # Deregister old images
    #
    print "\t", "===Deleting old AMIs (Retention policy is " + str(backup_retention) +" mins)==="
  
    # Get a list of matching images
    # Create a filter
    filters = [{"Name":"tag:Name", "Values":[server_name_pattern + signature + "*"]}]
    # Returned a list of images
    try:
      images = ec2.images.filter(Filters=filters)
    except Exception, e:
      # Failed
      logger.error("Backup " + server_name + ": " + e.message)
      print "Error: " + e.message
      # Skip the current iteration pass
      continue

    for image in images:
      # Get image name 
      for tag in image.tags:
        # Each tag is a dictionary 
        if tag['Key'] == 'Name':
          image_name = tag['Value']
      # for

      # Get image ID
      #image_id = image.id
      #print image_id

      # Calculate the time difference in minutes
      image_stamp = image_name.replace(server_name_pattern + signature, "")
      image_timestamp = mktime(time.strptime(image_stamp, "%Y-%m-%d_%H-%M-%S"))
      current_timestamp = mktime(current_datetime.timetuple())
      diff_minutes = (current_timestamp - image_timestamp) / 60

      if (diff_minutes > backup_retention):
        try:
          image.deregister()
        except Exception, e:
          logger.error("Backup " + server_name + ": " + e.message)
          print "Error: " + e.message 
          # Skip the current iteration pass
          continue

        print "\t", image_name, " deleted"
        logger.info("Deleted AMI " + image_name )
      else:
        print "\t", image_name, " kept"
        logger.info("Kept AMI " + image_name )
    # for
  # for
 
  print "Backup ended\n"
# End of main()

# If this script is executed as a standalone program, Python's __main__ built-in
# moudle loads the script as a module
if __name__ == '__main__':
  main()
