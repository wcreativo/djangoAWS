import boto3


def create_folder(bucket, directory_name):
    """Permite crear un folder en el bucket"""

    try:
        s3 = boto3.client('s3')
        key_path = directory_name + '/' "Indicamos crear un folder"
        s3.put_object(Bucket=bucket, Key=key_path)
    except Exception as err:
        print(err)
