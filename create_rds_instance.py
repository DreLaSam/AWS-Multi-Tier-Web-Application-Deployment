# creates a MySQL RDS instance.

import boto3

def create_rds_instance(sg_id):
    rds = boto3.client('rds')
    response = rds.create_db_instance(
        DBName='MyAppDB',
        DBInstanceIdentifier='myapp-db',
        AllocatedStorage=20,
        DBInstanceClass='db.t2.micro',
        Engine='mysql',
        MasterUsername='admin',
        MasterUserPassword='password123',
        VpcSecurityGroupIds=[sg_id],
        MultiAZ=False,
        StorageType='gp2'
    )
    print(f"RDS Instance created: {response['DBInstance']['DBInstanceIdentifier']}")
    return response['DBInstance']['DBInstanceIdentifier']

if __name__ == "__main__":
    sg_id = "YOUR_SECURITY_GROUP_ID_HERE"
    create_rds_instance(sg_id)
