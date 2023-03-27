import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('bidaryProductCatalog')

with table.batch_writer() as batch:
    batch.put_item(Item={"Id": "bidary101", "Title": "Book 101 Title",
        "ISBN": "111-1111111111", "Authors": "Author1", "Price": 2, "ProductCategory": "Book"} )
    batch.put_item(Item={"Id": "bidary102", "Title": "Book 102 Title",
         "Authors": "Author2", "Price": 20, "ProductCategory": "Book"} )
    batch.put_item(Item={"Id": "bidary103", "Title": "Book 103 Title",
        "ISBN": "333-3333333333", "Authors": "Author1", "Price": 2000, "ProductCategory": "Book"} )
    batch.put_item(Item={"Id": "bidary201", "Title": "18-Bike-201",
        "Description": "201 Description", "BicycleType": "Road", "Price": 100, "ProductCategory": "Bicycle"} )
    batch.put_item(Item={"Id": "bidary202", "Title": "21-Bike-202",
         "BicycleType": "Road", "Price": 200, "Color":["Green","Black"],"ProductCategory": "Bicycle"} )
    batch.put_item(Item={"Id": "bidary203", "Title": "19-Bike-203",
        "Description": "203 Description", "BicycleType": "Road", "Price": 300, "ProductCategory": "Bicycle"} )