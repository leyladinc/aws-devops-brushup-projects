import json
import urllib.parse

def lambda_handler(event, context):
    print("Full event received:")
    print(json.dumps(event))

    for record in event["Records"]:
        bucket_name = record["s3"]["bucket"]["name"]
        object_key = urllib.parse.unquote_plus(record["s3"]["object"]["key"])

        print("New file uploaded")
        print(f"Bucket: {bucket_name}")
        print(f"File: {object_key}")

    return {
        "statusCode": 200,
        "body": "S3 event processed successfully"
    }
