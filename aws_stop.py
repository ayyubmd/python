# !/usr/bin/python
# Written Ayyub Mohammad (Ayyub_Mohammad) on 12/12/2016
# Python Script to stop running instance in AWS Environment. This is can modifed in many ways based on tags and instance state.
# This script can be used in AWS LAMBDA To schedule stop the instance during weekend.

import boto3

region = 'us-east-1'

ec2 = boto3.resource('ec2', region_name=region)


def main():

 ids = []

 # Use the filter() method of the instances collection to retrieve all running EC2 instances.
 instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

 # Get All the running instance id's in a list
 for instance in instances:

   #Print Instance and Instance state
   print instance.id + " " +instance.state['Name']

   #Store instance ID in list
   ids = ids + [instance.id]

   #Get the Name of the instance ID if requried
   for tag in instance.tags:
    if tag['Key'] == 'Name':
      print tag['Value'] + ' stopping'

 # Stopping multiple instances given a list of instance IDs
 ec2.instances.filter(InstanceIds=ids).stop()


#-------------------------------------
if __name__ == '__main__':
 main()