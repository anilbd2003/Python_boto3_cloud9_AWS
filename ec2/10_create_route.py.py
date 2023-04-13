import boto3

client = boto3.client('ec2')

response = client.create_route(
    DestinationCidrBlock='0.0.0.0/0',
    GatewayId='igwID',
    RouteTableId='rtbID',
)

print(response)