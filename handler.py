import os
import json
import boto3
import uuid
from botocore.exceptions import ClientError

# curl -d 'hallo welt' -H "Content-Type: text/plain" $(sls info --verbose | grep HttpApiUrl | cut -d' ' -f 2)/
def sample_post(event, context):
    client = boto3.client('s3')
    try:
        response = client.put_object(Body=event["body"], Bucket=os.environ['bucket'], Key=uuid.uuid4().hex + '.txt')
        return {
            "statusCode": 200,
            "body": json.dumps(response)
        }

    except ClientError as err:
        print(err)
        return {
            "statusCode": 500,
            "body": json.dumps(err.response)
        }

# curl $(sls info --verbose | grep HttpApiUrl | cut -d' ' -f 2)/
def sample_get(event, context):
    s3 = boto3.resource('s3')
    try:
        bucket = s3.Bucket(os.environ['bucket'])
        lines=[]
        for object_summary in bucket.objects.all(): 
            s3_object = s3.Object(object_summary.bucket_name, object_summary.key)
            response = s3_object.get()
            if len(lines) > 0:
                lines.append('\n')
            lines.append(response['Body'].read())

        return {
            "statusCode": 200,
            "body": ''.join(lines)
        }

    except ClientError as err:
        print(err)
        return {
            "statusCode": 500,
            "body": json.dumps(err.response)
        }    
