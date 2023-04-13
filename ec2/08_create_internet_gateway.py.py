import boto3

client = boto3.client('ec2')

#Creates an internet gateway for use with a VPC. After creating the internet gateway, you attach it to a VPC using AttachInternetGateway .

internet_gateway = client.create_internet_gateway(
)