# AWS-Multi-Tier-Web-Application-Deployment
This project demonstrates how to automate the deployment of a multi-tier web application on AWS using Python and boto3. The architecture includes a VPC, EC2 instances, an RDS database, and CloudWatch for monitoring.

Architecture Overview:

  - VPC: Creates a virtual network with public and private subnets for secure communication.
  
  - EC2 Auto Scaling Group: Provides scalable web application instances.
  
  - RDS (MySQL): Manages the database layer in a private subnet.
  
  - CloudWatch & SNS: Monitors resource performance and sends notifications for alerts.
  
  - CloudFormation: Automates infrastructure as code for consistency and repeatability.
  

Setup Instructions: 

  Prerequisites

    - Ensure you have the following installed and configured:
    
    - Python 3.x
    
    - boto3 (pip install boto3)
    
    - AWS CLI configured with your credentials (aws configure)

  Running the Project:

  Clone the repository and run each script sequentially:

    # Clone the repository
    $ git clone https://github.com/yourusername/aws-multi-tier-project.git
    $ cd aws-multi-tier-project
    
    # Run the scripts in order
    $ python create_vpc.py
    $ python create_security_group.py
    $ python launch_ec2_instance.py
    $ python create_rds_instance.py
    $ python monitoring_and_alerts.py

  You can also run main.py to automate the full deployment end-to-end.

    $ python main.py


File Structure:

  - create_vpc.py: Creates the VPC and subnets.
  
  - create_security_group.py: Creates a security group with rules for HTTP and SSH access.
  
  - launch_ec2_instance.py: Launches an EC2 instance with a simple web server.
  
  - create_rds_instance.py: Deploys a MySQL RDS instance in a private subnet.
  
  - monitoring_and_alerts.py: Sets up CloudWatch alarms and SNS notifications.
  
  - deploy_cloudformation.py: (Optional) Deploys a CloudFormation template for full automation.
  
  - cleanup_resources.py: Cleans up all AWS resources to avoid charges.
  

How It Works:

  - VPC Creation: Sets up a secure network environment.
  
  - Security Group Setup: Defines access rules for your EC2 instances.
  
  - EC2 Deployment: Launches a web server that runs a simple HTML page.
  
  - RDS Deployment: Creates a MySQL database for the application.
  
  - Monitoring and Alerts: Tracks CPU utilization and sends notifications when thresholds are exceeded.
  

Sample Output:

  - VPC created successfully.
  
  - EC2 instance launched: i-1234567890abcdef0
  
  - RDS instance created: myapp-db
  
  - CloudWatch Alarm set for high CPU utilization.
  

Future Improvements:

  - Add an Application Load Balancer (ALB) for better traffic distribution.
  
  - Integrate S3 for static file storage.
  
  - Use AWS Lambda for serverless automation.
  
  - Enable Multi-AZ for the RDS instance for higher availability.
