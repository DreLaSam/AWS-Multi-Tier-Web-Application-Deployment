import create_vpc
import create_security_group
import launch_ec2_instance
import create_rds_instance
import monitoring_and_alerts
import cleanup_resources

# Step 1: Create VPC and Subnets
print("Step 1: Creating VPC and Subnets...")
vpc_id, subnet_public_id, subnet_private_id = create_vpc.create_vpc()

# Step 2: Create Security Group
print("Step 2: Creating Security Group...")
sg_id = create_security_group.create_security_group(vpc_id)

# Step 3: Launch EC2 Instance
print("Step 3: Launching EC2 Instance...")
ec2_instance_id = launch_ec2_instance.launch_ec2_instance(subnet_public_id, sg_id)

# Step 4: Create RDS Instance
print("Step 4: Creating RDS Instance...")
rds_instance_id = create_rds_instance.create_rds_instance(sg_id)

# Step 5: Set up CloudWatch Monitoring and SNS Alerts
print("Step 5: Setting up CloudWatch Monitoring and SNS Alerts...")
monitoring_and_alerts.create_cloudwatch_alarm(ec2_instance_id)

# Completion Message
print("All resources have been successfully created and configured!")

# Cleanup Prompt
cleanup = input("Do you want to clean up all resources? (yes/no): ").strip().lower()
if cleanup == 'yes':
    print("Cleaning up resources...")
    cleanup_resources.cleanup_resources(ec2_instance_id, rds_instance_id)
    print("All resources have been cleaned up.")
else:
    print("Resources have been left running. Don't forget to clean them up later to avoid charges.")
