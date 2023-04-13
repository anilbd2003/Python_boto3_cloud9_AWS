import boto3

client = boto3.client('ec2')

response = client.attach_internet_gateway(
   
    InternetGatewayId='igwID',
    VpcId='vpcID'
)