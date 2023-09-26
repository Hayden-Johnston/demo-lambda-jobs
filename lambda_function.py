import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    s3 = boto3.resource('s3')
    bucket_name = 'demo-job-data'
    file_name = 'test.txt'
    file_content = 'Hello, World!'
    
    object = s3.Object(bucket_name, file_name)
    object.put(Body=file_content)