#  terminates EC2 instances, delete RDS instances, and clean up other resources.

import boto3

def cleanup_resources(instance_id, db_instance_id):
    ec2 = boto3.client('ec2')
    rds = boto3.client('rds')

    ec2.terminate_instances(InstanceIds=[instance_id])
    print(f"Terminated EC2 Instance: {instance_id}")

    rds.delete_db_instance(DBInstanceIdentifier=db_instance_id, SkipFinalSnapshot=True)
    print(f"Deleted RDS Instance: {db_instance_id}")

if __name__ == "__main__":
    instance_id = "YOUR_INSTANCE_ID_HERE"
    db_instance_id = "YOUR_DB_INSTANCE_ID_HERE"
    cleanup_resources(instance_id, db_instance_id)
