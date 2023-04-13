import boto3

client = boto3.client('ec2')

#Creates a subnet in an existing VPC.

response = client.create_subnet(
    AvailabilityZone='us-west-2a',
    CidrBlock='10.0.1.0/24',
    VpcId='vpcID',
)

print(response)