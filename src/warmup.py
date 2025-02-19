import boto3
from botocore.exceptions import ClientError
from pprint import pprint

# def create_bucket():
#     try:
#         s3_client = boto3.client('s3')
#         s3_client.create_bucket(Bucket='dec-angelo-anas-sprint-bucket',
#                                 CreateBucketConfiguration={'LocationConstraint':'eu-west-2'})
        
#     except ClientError as e:
#         print(e)

# create_bucket()
# def upload_files():
#     try:
#         s3_client = boto3.client('s3')
#         s3_client.upload_file('sprint.txt','dec-angelo-anas-sprint-bucket','sprint-2.txt')
#         s3_client.upload_file('password-manager.txt','dec-angelo-anas-sprint-bucket','password-2.txt')
#     except ClientError as e:
#         print(e)

# upload_files()

# def list_files():
#     s3 = boto3.resource('s3')
#     my_bucket = s3.Bucket('dec-angelo-anas-sprint-bucket')
#     files_list=[]
#     for my_bucket_object in my_bucket.objects.all():
#         files_list.append(my_bucket_object.key)
#     for i in range(len(files_list)):
#         print(files_list[i])
    
#     s3_client = boto3.client('s3')
#     file = s3_client.get_object(Bucket='dec-angelo-anas-sprint-bucket', Key='sprint-2.txt')
#     data = file['Body'].read()
#     pprint(data)

# list_files()

# def delete_objects():
#     s3_client = boto3.client('s3')
#     response = s3_client.delete_objects(Bucket='dec-angelo-anas-sprint-bucket',
#                                         Delete={"Objects": [{"Key": "sprint-2.txt"}, {"Key": "password-2.txt"}]})
#     print(response)

# delete_objects()

# def delete_bucket():
#     s3_client = boto3.client('s3')
#     response = s3_client.delete_bucket(Bucket='dec-angelo-anas-sprint-bucket')
#     print(response)

# delete_bucket()

def list_buckets():
    s3_client = boto3.client('s3')
    response = s3_client.list_buckets()
    print(response['Buckets'])

list_buckets()