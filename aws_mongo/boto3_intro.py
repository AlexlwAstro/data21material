import io

import boto3
from pprint import pprint
import json
import pandas as pd

s3_client = boto3.client('s3')
bucket_list = s3_client.list_buckets()
# pprint(bucket_list, sort_dicts=False)
# print()
# for index, item in enumerate(bucket_list['Buckets'], start=1):
#     x = item['Name']
#     pprint(f'{index},{x}')
bucket_name = 'data-eng-resources'
#bucket_contents = s3_client.list_objects_v2(
#    Bucket=bucket_name
#)
# pprint(bucket_contents)
# for index, list_dict in enumerate(bucket_contents['Contents'], start=1):
#     print(index, list_dict['Key'])

# 'resource' api built into Boto3
s3_resource = boto3.resource('s3')
bucket = s3_resource.Bucket(bucket_name)
contents = bucket.objects.all()
# for object_x in contents:
#     pprint(object_x.key)
s3_object = s3_client.get_object(
    Bucket=bucket_name,
    Key='python/fish-market.csv'
)
# pprint(s3_object)
# data we want lives in s3_object['Body'], which is a StreamingBody object

# JSON case:
# json python module can import streaming objects!
#contents = s3_object['Body'].read()
# above line produces a binary (Byte) string
#contents_dict = json.loads(contents)
# produces a standard Python dictionary!
#pprint(contents_dict)

# CSV case: use Pandas
#print(contents)
#df = pd.read_csv(s3_object['Body'])
# data streams are one-time streams - only use 1 'read' method at a time
# can't run line 36 and 44 without commenting one out
#print(df)


# WRITING TO S3:
#my_name = 'Alex Lisboa-Wright'
my_dict = {
    'name': 'Alex Lisboa-Wright',
    'groceries': ['chocolate', 'apple', 'milk', 'beef']
}
# make local file then upload (inefficient)
# with open('alex-name.json', 'w') as outfile:
#     json.dump(my_dict, outfile)
# # write to s3:
# s3_client.upload_file(
#     Filename='alex-name.json',
#     Bucket='data-eng-resources',
#     Key='Data21/alexlisboa-wright.json'
# )

# put directly into s3 by converting to a byte stream
# s3_client.put_object(
#     Body=json.dumps(my_dict),
#     Bucket='data-eng-resources',
#     Key='Data21/Put/alex.json'
# )

# Pandas dataframe
df = pd.DataFrame([2, 4, 6, 8, 10], [10, 20, 30, 40, 50])
# write to a string buffer using io package - buffer just holds onto the data
str_buffer = io.StringIO()
df.to_csv(str_buffer)

# s3_client.put_object(
#     Body=str_buffer.getvalue(),
#     Bucket='data-eng-resources',
#     Key='Data21/CSV/alex.csv'
# )

# can do the same thing with resource instead of client:
# s3_resource = boto3.resource('s3')
s3_resource.Object(
    'data-eng-resources',
    'Data21/CSV/alex.csv'
).put(
    Body=str_buffer.getvalue()
)
