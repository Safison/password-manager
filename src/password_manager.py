from utility.password_entry import get_identifier, get_and_save_credentials


def main():
    identifier = input('Please enter your identifier name: ')
    get_id = get_identifier(identifier)
    if get_id == identifier:
        get_credentials = get_and_save_credentials(identifier)
        if get_credentials == identifier:
            return 'Secret created successfully'
            
        else:
            print('Unsuccessful creation, try again')
    else:
        return "Identifier already exist"

