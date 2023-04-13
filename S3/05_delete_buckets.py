import boto3

client = boto3.client('s3')

response = client.delete_bucket(
    Bucket='myBucketName'
)

print('bucket deleted successfully')