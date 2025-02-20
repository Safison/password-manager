#entry script
#ask to input identifier, user name and password, and then saves the input as a secret in aws secrests manager
# 1- input identifier function
# 2 - creadetials function
# 3 - save entries function

import boto3
import maskpass


        
def get_identifier(id):
    #identifier = input('Please enter your identifier name: ')
    client = boto3.client('secretsmanager')
    try:
        response = client.describe_secret(SecretId=id)
        return 'This identifier already exists'
    except client.exceptions.ResourceNotFoundException as e:
        return id

    

def get_and_save_credentials(identifier):
    client = boto3.client('secretsmanager')
    get_username = input('Please enter your username: ')
    get_pwd = maskpass.askpass(prompt="Please enter your password: ", mask="#")
    username_str = '{"username":'
    password_str = ',"password":'
    end_str = '}'
    secretstring = username_str + get_username + password_str + get_pwd + end_str
    response = client.create_secret(
    Name=identifier,
    SecretString=secretstring
    )
    print(response)
    
    return response['Name']

# get_and_save_credentials('Angelo-Anas-test-ident1')



