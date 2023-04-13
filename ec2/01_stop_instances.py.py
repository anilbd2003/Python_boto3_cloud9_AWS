import boto3

client = boto3.client('ec2')

response = client.stop_instances(
    InstanceIds=[
        'instanceID',
    ],
)