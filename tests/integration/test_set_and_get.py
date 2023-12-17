import pytest
from ...main import main_db_location, test_db_location
from ...cli import CLIInterface

@pytest.fixture
def setup_teardown():
    # Set up: Create an instance of CLIInterface with the test database
    cli_interface = CLIInterface(main_db_location, test_db_location)
    
    yield cli_interface  # The test runs here
    
    # Teardown: Reset the test database after the test
    cli_interface.resetdb(test_db_location)

def test_set_and_get_values(setup_teardown):
    cli_interface = setup_teardown
    cli_interface.run(["create_table", "--table", "test_table", "--test"])
    
    # Set a value
    cli_interface.run(["set", "--table", "test_table", "--key", "name", "--value", "John", "--test"])
    
    # Get the value and assert
    result = cli_interface.run(["get", "--table", "test_table", "--key", "name", "--test"])
    assert result == "John"