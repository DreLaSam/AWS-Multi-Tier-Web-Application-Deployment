#  deploys a CloudFormation template using boto3.

import boto3

def deploy_cloudformation():
    cloudformation = boto3.client('cloudformation')
    with open('my-template.yaml', 'r') as template_file:
        template_body = template_file.read()

    cloudformation.create_stack(
        StackName='MyAppStack',
        TemplateBody=template_body,
        Parameters=[
            {'ParameterKey': 'InstanceType', 'ParameterValue': 't2.micro'},
        ],
        Capabilities=['CAPABILITY_IAM']
    )
    print("CloudFormation Stack deployed")

if __name__ == "__main__":
    deploy_cloudformation()
