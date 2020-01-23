import boto3
import csv

# get a handle on s3
session = boto3.Session(
                    aws_access_key_id='XXXXXXXXXXXXXXXXXXXXXXX',
                    aws_secret_access_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
                    region_name='XXXXXXXXXX')
                    
s3 = session.resource('s3')

# get a handle on the bucket that holds your file
bucket = s3.Bucket('dev-innowatts-sparkenergy-processing')

# get a handle on the object you want (i.e. your file)
obj = bucket.Object(key='gas/midwest/r_midwest_customer_info/process_date=2019-09-16/CUSTOMER_20190916_MIDWEST.csv')

# get the object
response = obj.get()

# read the contents of the file
lines = response['Body'].read()

# saving the file data in a new file test.csv
with open('test.csv', 'wb') as file:
    file.write(lines)
