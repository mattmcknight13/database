# tests/conftest.py
import pytest
from ...main import main_db_location, test_db_location
from ...cli import CLIInterface  # Replace with the actual module containing CLIInterface

@pytest.fixture
def setup_teardown():
    main_db = main_db_location
    test_db = test_db_location
    
    # Set up: Create an instance of CLIInterface with the test database
    cli_interface = CLIInterface(main_db, test_db)
    
    yield cli_interface  # The test runs here
    
    # Teardown: Reset the test database
    cli_interface.resetdb(test_db)
