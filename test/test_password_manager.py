from src.password_manager import main
import pytest

def test_main_password_manager_if_id_not_exists():
    result = main()
    assert result == 'Secret created successfully'
    pass

def test_main_password_manager_if_id_exists():
    result = main()
    assert result == "Identifier already exist"
    pass


