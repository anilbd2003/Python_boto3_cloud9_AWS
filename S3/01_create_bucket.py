import boto3

client = boto3.client('s3', region_name='us-east-1')

bucket_name= 'myBucketName'
bucket_region= 'us-west-2'
response = client.create_bucket(
    ACL='private',
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': bucket_region
    },
)

if(response['ResponseMetadata']['HTTPStatusCode'])==200:
    print('bucket created with bucket name ' + bucket_name + ' in ' + bucket_region + 'region' )