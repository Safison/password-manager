from utility.retrieve_password import password_retrieval
import pytest
import boto3

def test_password_retrieval_retrieves_id_and_save_credentials_to_file():
    client = boto3.client('secretsmanager')
    result = password_retrieval(client)
    file_name = 'secrets.txt'
    assert result == f'secrets stored in {file_name}' 

def test_password_retrieval_shows_error_message_if_id_not_exist():
    client = boto3.client('secretsmanager')
    result = password_retrieval(client)
    
    assert result == 'Secret not found' 

