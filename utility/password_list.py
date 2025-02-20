import boto3


# list function
# - retrieve a list of all secrets identifiers

def list_secrets(client):
    
    sec_id_list=[]
    #client = boto3.client('secretsmanager')
    response = client.list_secrets()
    count = len(response['SecretList'])
    for sec in response['SecretList']:
        sec_id_list.append(sec['Name'])
    
    full_string = f'{count} secret(s) are available'
    sec_string = ''
    if sec_id_list:
        for i in range(len(sec_id_list)):
            sec_string += '\n' + sec_id_list[i]

        full_string = full_string + sec_string 
    return full_string
    # print(response)
    # print(count)
    # print(sec_id_list)

#print(list_secrets())