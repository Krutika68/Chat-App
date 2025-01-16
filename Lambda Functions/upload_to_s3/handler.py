import boto3

def lambda_handler(event, context):
    # Extract file content and name from the event (payload)
    file_content = event.get('file_content')
    file_name = event.get('file_name')
    
    s3 = boto3.client('s3')
    bucket_name = 'your-s3-bucket-name'
    
    # Upload the file to S3
    s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)
    
    return {
        'statusCode': 200,
        'body': f"File {file_name} uploaded to S3."
    }
