def delete():
    client = boto3.client('secretsmanager')
    id_input = input('Specify secret to delete:')
    try:
        response = client.delete_secret(
        SecretId=id_input,
        RecoveryWindowInDays=7,
        ForceDeleteWithoutRecovery=True|False
        )
        print(response['Name'])
        return f'{id_input} has been deleted'
    except client.exceptions.ResourceNotFoundException as e:
        return 'Secret not found'
    
