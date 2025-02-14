#  creates CloudWatch alarms and SNS notifications for monitoring instance performance.

import boto3

def create_cloudwatch_alarm(instance_id):
    cloudwatch = boto3.client('cloudwatch')
    sns = boto3.client('sns')
    sns_topic = sns.create_topic(Name='ec2-alerts')
    sns_arn = sns_topic['TopicArn']
    print(f"SNS Topic created: {sns_arn}")

    cloudwatch.put_metric_alarm(
        AlarmName='HighCPUUtilization',
        MetricName='CPUUtilization',
        Namespace='AWS/EC2',
        Statistic='Average',
        Period=300,
        Threshold=70.0,
        ComparisonOperator='GreaterThanThreshold',
        EvaluationPeriods=2,
        AlarmActions=[sns_arn],
        Dimensions=[{'Name': 'InstanceId', 'Value': instance_id}]
    )
    print("CloudWatch Alarm created for CPU Utilization")

if __name__ == "__main__":
    instance_id = "YOUR_INSTANCE_ID_HERE"
    create_cloudwatch_alarm(instance_id)
