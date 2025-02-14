# Creates VPC and subnets.

import boto3

def create_vpc():
    ec2 = boto3.client('ec2')
    vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
    vpc_id = vpc['Vpc']['VpcId']
    print(f"VPC created: {vpc_id}")

    # Enable DNS support and hostname
    ec2.modify_vpc_attribute(VpcId=vpc_id, EnableDnsSupport={'Value': True})
    ec2.modify_vpc_attribute(VpcId=vpc_id, EnableDnsHostnames={'Value': True})

    # Create Subnets
    subnet_public = ec2.create_subnet(VpcId=vpc_id, CidrBlock='10.0.1.0/24', AvailabilityZone='us-east-1a')
    subnet_private = ec2.create_subnet(VpcId=vpc_id, CidrBlock='10.0.2.0/24', AvailabilityZone='us-east-1b')
    print(f"Public Subnet: {subnet_public['Subnet']['SubnetId']}")
    print(f"Private Subnet: {subnet_private['Subnet']['SubnetId']}")

    return vpc_id, subnet_public['Subnet']['SubnetId'], subnet_private['Subnet']['SubnetId']

if __name__ == "__main__":
    create_vpc()