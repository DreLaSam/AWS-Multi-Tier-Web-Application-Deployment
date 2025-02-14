# launches EC2 instances with a UserData script to install and start a web server.

import boto3

def launch_ec2_instance(subnet_id, sg_id):
    ec2 = boto3.client('ec2')
    instance = ec2.run_instances(
        ImageId='ami-0abcdef1234567890',  # Replace with your AMI ID
        MinCount=1,
        MaxCount=1,
        InstanceType='t2.micro',
        KeyName='your-key-pair',
        SecurityGroupIds=[sg_id],
        SubnetId=subnet_id,
        UserData='''#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "Welcome to My Web Application" > /var/www/html/index.html'''
    )
    print(f"EC2 Instance launched: {instance['Instances'][0]['InstanceId']}")
    return instance['Instances'][0]['InstanceId']

if __name__ == "__main__":
    subnet_id = "YOUR_PUBLIC_SUBNET_ID_HERE"
    sg_id = "YOUR_SECURITY_GROUP_ID_HERE"
    launch_ec2_instance(subnet_id, sg_id)