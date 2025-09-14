# Import boto3 and create boto3 Firehose client
import boto3

from aws.constant import AWS_ACCESS_ID, AWS_SECRET_KEY, REGION_US_EAST_1
from aws.kinesis.constant import ENDPOINT, FIREHOSE

firehose_client = boto3.client(FIREHOSE,
                               aws_access_key_id=AWS_ACCESS_ID,
                               aws_secret_access_key=AWS_SECRET_KEY,
                               region_name=REGION_US_EAST_1,
                               endpoint_url=ENDPOINT)

# Get a list of delivery streams
response = firehose_client.list_delivery_streams()

# Iterate over the response contents and delete every stream
for stream_name in response['DeliveryStreamNames']:
    firehose_client.delete_delivery_stream(DeliveryStreamName=stream_name)
    print(f"Deleted stream: {stream_name}")

# Print list of delivery streams
print(firehose_client.list_delivery_streams())





import _setup, create_firehose
firehose, s3, records = _setup.ex_vars
for idx, row in records.iterrows():

    # Create a payload string that ends with a newline
    payload = ' '.join(str(value) for value in row)
    payload = payload + "\n"
    print("Sending payload: {}".format(payload))

    # Send the payload string to Firehose stream
    res = firehose.put_record(
        DeliveryStreamName='gps-delivery-stream',
        Record={'Data': payload})

    # Print the written RecordId
    print("Wrote to RecordId: {}".format(res['RecordId']))


import _setup, _run_deps, pandas as pd
firehose, s3, records = _setup.ex_vars

# List the objects that have been written to the S3 bucket
objects = s3.list_objects_v2(Bucket='sd-vehicle-data')['Contents']

# Create list for collecting dataframes from read files.
dfs = []

# For every object, load it from S3
for obj in objects:
    data_file = s3.get_object(Bucket='sd-vehicle-data', Key=obj['Key'])

    # Load it into a dataframe, specifying a delimiter and column names
    dfs.append(pd.read_csv(data_file['Body'],
                           delimiter=" ",
                           names=["record_id", "timestamp", "vin", "lon", "lat", "speed"]))

# Concatenate the resulting dataframes.
data = pd.concat(dfs)
print(data.groupby(['vin'])['speed'].max())




