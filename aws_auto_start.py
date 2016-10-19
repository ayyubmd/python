# !/usr/bin/python
# Written Ayyub Mohammad (Ayyub_Mohammad) on 08/25/2016

import boto.ec2
import sys
import time
import logging
from datetime import datetime

#AWS Keys
auth = {"aws_access_key_id": "<access-key>", "aws_secret_access_key": "<secrete-key>"}

# Setup logging
date_year = time.strftime("%d.%Y")

logfilename = "techopsInstance" + "_" + date_year + ".log"
logging.basicConfig(filename=logfilename, level=logging.INFO)
logging.info('This is a log message.')

def main():

 if len(sys.argv) < 2:
  print "Usage: python aws.py {start|stop}\n"
  sys.exit(0)
 else:
  action = sys.argv[1]

 if action == "start":
   startInstance()
 elif action == "stop":
   stopInstance()
 else:
   print "Usage: python aws.py {start|stop}\n"

# Start ec2 Instances in TechOps
def startInstance():
 logging.info("Starting the Instance..... ")

 try:
   ec2 = boto.ec2.connect_to_region("us-east-1", **auth)

 except Exception, e1:
   error1 = "Error in conneting Env: %s" % str(e1)
   loggin.error(error1)
   sys.exit(0)

 try:
  reservations = ec2.get_all_instances()
  for reservation in reservations:
    for instances in reservation.instances:
      if instances.state == "stopped":
       description = 'Starting %(Instance_Name)s with instanceId %(Instance_Id)s which is in %(Instance_State)s state at %(date)s' % {
         'Instance_Name': instances.tags["Name"],
         'Instance_Id': instances.id,
         'Instance_State': instances.state,
         'date': datetime.today().strftime('%d-%m-%Y %H:%M:%S')
        }
       logging.info(description)
	   ec2.start_instances(instances.id)

 except Exception, e1:
   error1 = "Error in instance Start Up: %s" % str(e1)
   logging.error(error1)
   sys.exit(0)


# Stop ec2 Instances in TechOps
def stopInstance():
 logging.info("Stoping the Instances..... ")

 try:
   ec2 = boto.ec2.connect_to_region("us-east-1", **auth)

 except Exception, e1:
   error1 = "Error in conneting Env: %s" % str(e1)
   loggin.error(error1)
   sys.exit(0)

 try:
  reservations = ec2.get_all_instances()
  for reservation in reservations:
    for instances in reservation.instances:
      if instances.state == "running":
       description = 'Stoping %(Instance_Name)s with instanceId %(Instance_Id)s which is in %(Instance_State)s state at %(date)s' % {
         'Instance_Name': instances.tags["Name"],
         'Instance_Id': instances.id,
         'Instance_State': instances.state,
         'date': datetime.today().strftime('%d-%m-%Y %H:%M:%S')
        }
       logging.info(description)
	   ec2.stop_instances(instances.id)

 except Exception, e1:
   error1 = "Error in instance Start Up: %s" % str(e1)
   logging.error(error1)
   sys.exit(0)

#-------------------------------------
if __name__ == '__main__':
 main()
