import boto3
import ast
import json

client = boto3.client('secretsmanager')

def password_retrieval(client):
    id_input = input('Specify secret to retrieve:')
    try:
        response = client.get_secret_value(
        SecretId=id_input)
        sec_str = response['SecretString']
        comma_index = sec_str.rfind(',')
        user_str = sec_str[1:comma_index] + '\n'
        pass_str = sec_str[comma_index+1:len(sec_str)-1]
        file = open("secrets.txt", "w")
        file.writelines([user_str, pass_str])
        file.close()
        return (f'secrets stored in {file.name}')
    
    except client.exceptions.ResourceNotFoundException as e:
        return 'Secret not found'

# password_retrieval()


    