import boto3
import ast

def password_retrieval():
    client = boto3.client('secretsmanager')
    id_input = input('Specify secret to retrieve:')
    try:
        response = client.get_secret_value(
        SecretId=id_input)

        #response['SecretString']['Name'] == id_input
        sec_string_dict = ast.literal_eval(response['SecretString'])
        user_id = sec_string_dict['username']
        password = sec_string_dict['password']
        file = open("secrets.txt", "w")
        
        file.writelines([f'user_id: {user_id}',f'password: {password}'])
        file.close()
        return (f'secrets stored in {file.name}')
    
    except client.exceptions.ResourceNotFoundException as e:
        return 'Secret not found'

password_retrieval()


    