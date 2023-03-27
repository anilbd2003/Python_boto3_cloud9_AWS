import boto3
# The UpdateItem API allows you to update a particular item as identified by its key.
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('bidaryProductCatalog')

resp = table.update_item(
    Key={"Id": "bidary101"},
    # Expression attribute names specify placeholders for attribute names to use in your update expressions.
    ExpressionAttributeNames={
        "#authors": "Authors",
        
    },
    # Expression attribute values specify placeholders for attribute values to use in your update expressions.
    ExpressionAttributeValues={
        ":id": "Author4",
    },
    # UpdateExpression declares the updates you want to perform on your item.
    # For more details about update expressions, see https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.UpdateExpressions.html
    UpdateExpression="SET #authors = :id",
)
#now use the getitem api to show what the book looks like after the update.
res = table.get_item(Key={"Id":"bidary101"})

print("item after update")
print(res['Item'])