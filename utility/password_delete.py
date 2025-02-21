import boto3

# client = boto3.client('secretsmanager')

def delete(client):
    id_input = input('Specify secret to delete:')
    try:
        response = client.delete_secret(
        SecretId=id_input
        )
        print(response['Name'])
        return f'{id_input} has been deleted'
    except client.exceptions.ResourceNotFoundException as e:
        return 'Secret not found'
    
