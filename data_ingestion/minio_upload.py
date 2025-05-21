import minio
from minio import Minio

client = Minio(
    'localhost:9000',
    access_key='minioadmin',
    secret_key='minioadmin',
    secure=False
)

bucket = 'openedge-data'
if not client.bucket_exists(bucket):
    client.make_bucket(bucket)

# Example: upload a file
def upload_file(local_path, object_name):
    client.fput_object(bucket, object_name, local_path)

if __name__ == "__main__":
    upload_file('example.json', 'data/example.json')
