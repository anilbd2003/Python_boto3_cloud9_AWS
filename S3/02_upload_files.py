import boto3
s3 = boto3.client('s3')

with open('architect.jpg', 'rb') as data:
    s3.upload_fileobj(data, 'myBucketName', 'architect.jpg')

print('file architect.jpg uploaded successfully ')