"""
AWS API Constants
Contains commonly used AWS service names, parameter names and other constants used when
interacting with AWS services via boto3.
"""
# AWS Credentials
AWS_ACCESS_ID = 'aws_access_key_id'
AWS_SECRET_KEY = 'aws_secret_access_key'
AWS_SESSION_TOKEN = 'aws_session_token'

# S3 Constants
S3_SERVICE = 's3'
S3_BUCKET = 'Bucket'
S3_KEY = 'Key'
S3_BODY = 'Body'
S3_ACL = 'ACL'
S3_REGION = 'LocationConstraint'

# DynamoDB Constants
DYNAMO_SERVICE = 'dynamodb'
DYNAMO_TABLE = 'TableName'
DYNAMO_KEY = 'Key'
DYNAMO_ITEM = 'Item'
DYNAMO_ATTRIBUTES = 'AttributeValues'

# AWS Regions
REGION_US_EAST_1 = 'us-east-1'
