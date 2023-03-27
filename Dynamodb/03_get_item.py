import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('bidaryProductCatalog')

resp = table.get_item(Key={"Id":"bidary201"})

print(resp['Item'])