from utility.password_entry import get_identifier, get_and_save_credentials

def test_get_identifier_if_identifier_does_not_exist_ask_for_username_and_password_works_returns_id():
    input = 'Angelo-Anas-test-ident123'
    #expected = input
    result = get_identifier(input)
    assert result == input
    
def test_get_identifier_if_identifier_exists_output_valid_message():
    input = 'Angelo-Anas-test-ident5'
    #expected = "This identifier already exists"
    result = get_identifier(input)
    assert result == 'This identifier already exists'


def test_get_credentials_asks_for_username_and_password():
    input_user = 'angelo'
    input_password = 123
    expected = 'Angelo-Anas-test-ident5'

    result = get_and_save_credentials(input_user)
    assert result == expected
    
    
    