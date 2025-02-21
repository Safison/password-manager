from utility.password_entry import get_identifier, get_and_save_credentials


def main():
    flag = True
    while flag:
        initial_input = input('Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it:')
        if initial_input == 'e':
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
        elif initial_input == 'r':
        elif initial_input == 'd':
        elif initial_input == 'l':
        elif initial_input == 'x':
            print('Thank you. Goodbye.')
            flag = False
        else:
            return 'Invalid input. Please specify [e]ntry, [r]etrieval, [d]eletion, [l]isting or e[x]it:'
            
        

