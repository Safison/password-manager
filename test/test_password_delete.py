from utility.password_delete import delete
from utility.password_list import list_secrets
import os
from moto import mock_aws
import boto3

@pytest.fixture
def aws_credentials():
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"

def test_delete_works_for_valid_input():
    with mock_aws():
        client = boto3.client('secretsmanager')
        response_create1 = client.create_secret(
            Name='Mock_secret1',
            SecretString='{"username":"david","password":"EXAMPLE-PASSWORD"}'
            )
        response_create2 = client.create_secret(
            Name='Mock_secret2',
            SecretString='{"username":"david","password":"EXAMPLE-PASSWORD"}'
            )
        response_create3 = client.create_secret(
            Name='Mock_secret3',
            SecretString='{"username":"david","password":"EXAMPLE-PASSWORD"}'
            )
        result = delete(client)
        assert result == 'Mock_secret2 has been deleted'
    
    
    
def test_delete_works_for_invalid_input():
    with mock_aws():
        client = boto3.client('secretsmanager')
        response_create1 = client.create_secret(
            Name='Mock_secret1',
            SecretString='{"username":"david","password":"EXAMPLE-PASSWORD"}'
            )
        response_create2 = client.create_secret(
            Name='Mock_secret2',
            SecretString='{"username":"david","password":"EXAMPLE-PASSWORD"}'
            )
        response_create3 = client.create_secret(
            Name='Mock_secret3',
            SecretString='{"username":"david","password":"EXAMPLE-PASSWORD"}'
            )
        result = delete(client)
        assert result == 'Secret not found'