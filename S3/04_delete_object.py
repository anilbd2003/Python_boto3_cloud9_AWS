import boto3
s3 = boto3.client('s3')


response = s3.delete_object(
    Bucket='myBucketName',
    Key='architect.jpg',
    
)

print('object deleted successfully')