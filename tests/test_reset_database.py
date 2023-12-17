import pytest
from ..main import main_db_location, test_db_location
from ..cli import CLIInterface

@pytest.fixture
def setup_teardown():
    # Set up: Create an instance of CLIInterface with the test database
    cli_interface = CLIInterface(main_db_location, test_db_location)
    
    yield cli_interface  # The test runs here

    cli_interface.resetdb(test_db_location)

def test_reset_database(setup_teardown):
    cli_interface = setup_teardown
    
    # Set a value
    cli_interface.run(["set", "--table", "test_table", "--key", "name", "--value", "John", "--test"])
    
    # Reset the database
    result = cli_interface.run(["resetdb", "--test"])
    
    # Assert results
    assert result is True
    assert cli_interface.tables == {}
