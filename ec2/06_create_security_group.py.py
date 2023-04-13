import boto3

client = boto3.client('ec2')

#You can add or remove rules from your security groups using 
#AuthorizeSecurityGroupIngress , AuthorizeSecurityGroupEgress , 
#RevokeSecurityGroupIngress , and RevokeSecurityGroupEgress 

security_group = client.create_security_group(
    Description='web (http) access',
    GroupName='mywebSG',
    VpcId='vpcID',
)