import boto3

client = boto3.client('ec2')

#Associates a subnet with a route table. The subnet and route table must be in the same VPC. 

response = client.associate_route_table(
    RouteTableId='rtbID',
    SubnetId='subnetID',
)

print(response)