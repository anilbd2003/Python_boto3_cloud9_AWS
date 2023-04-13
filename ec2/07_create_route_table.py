import boto3

client = boto3.client('ec2')

response = client.create_route_table(
    VpcId='vpcID',
    
)
# After you create a route table, you can add routes and associate the table with a subnet.