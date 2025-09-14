import boto3


s3_client = boto3.client('s3')

# Create the new sd-vehicle-data bucket
s3_client.create_bucket(Bucket='sd-vehicle-data')

# List the buckets in S3
for bucket_info in s3_client.list_buckets()['Buckets']:
    # Get the bucket_name
    bucket_name = bucket_info['Name']

    # Generate bucket ARN.
    arn = "arn:aws:s3:::{}".format(bucket_name)

    # Print the ARN
    print(arn)

