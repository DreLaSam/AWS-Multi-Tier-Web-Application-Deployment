# creates a Security Group and add ingress rules for SSH (port 22) and HTTP (port 80)

# Create Security Group
def create_security_group(vpc_id):
    ec2 = boto3.client('ec2')
    security_group = ec2.create_security_group(GroupName='web-sg', Description='Web Server SG', VpcId=vpc_id)
    sg_id = security_group['GroupId']

    ec2.authorize_security_group_ingress(
        GroupId=sg_id,
        IpPermissions=[
            {'IpProtocol': 'tcp', 'FromPort': 22, 'ToPort': 22, 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
            {'IpProtocol': 'tcp', 'FromPort': 80, 'ToPort': 80, 'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},
        ]
    )
    print(f"Security Group created: {sg_id}")
    return sg_id

if __name__ == "__main__":
    vpc_id = "YOUR_VPC_ID_HERE"
    create_security_group(vpc_id)


