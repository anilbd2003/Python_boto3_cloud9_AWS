import boto3

client = boto3.client('ec2')

response = client.terminate_instances(
    InstanceIds=[
        'instanceID',
    ],
)