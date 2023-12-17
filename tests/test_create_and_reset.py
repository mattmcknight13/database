import pytest
from ..main import main_db_location, test_db_location
from ..cli import CLIInterface

@pytest.fixture
def setup_teardown():
    # Set up: Create an instance of CLIInterface with the test database
    cli_interface = CLIInterface(main_db_location, test_db_location)
    
    yield cli_interface  # The test runs here

    cli_interface.resetdb(test_db_location)


def test_create_and_reset_table(setup_teardown):
    cli_interface = setup_teardown
    
    # Create a table
    result_create = cli_interface.run(["create_table", "--table", "test_table", "--test"])
    
    # Reset the table
    result_reset = cli_interface.run(["reset_table", "--table", "test_table", "--test"])
    
    # Assert results
    assert result_create is True
    assert result_reset is True
    assert cli_interface.tables.get("test_table") == {}
