from utility.password_list import list_secrets
import pytest
from moto import mock_aws
import os
import boto3


@pytest.fixture
def aws_credentials():
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"

def test_password_list_returns_0_list_if_no_secrets():

    with mock_aws():
        client = boto3.client('secretsmanager')
        result = list_secrets(client)
        assert result == '0 secret(s) are available'

def test_password_list_returns_list_of_secrets():
    client = boto3.client('secretsmanager')
    result = list_secrets(client)
    assert result == """4 secret(s) are available\nAngelo-Anas-test-ident5\nangelo-anas-first-id\nangelo-anas-second-id\nangelo-anas-third-id"""