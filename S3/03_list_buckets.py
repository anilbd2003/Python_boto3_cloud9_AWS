import boto3
s3 = boto3.client('s3')


response= s3.list_buckets()  # this only list under the hood. to display list, you need to run response 

print('Name of buckets in your account are listed below. ')

for bucket in response['Buckets']:
    print(bucket['Name'])