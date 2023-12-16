# tests/test_integration.py
import os
import pytest
from main import main_db_location, test_db_location
from cli import CLIInterface

@pytest.fixture
def setup_teardown():
    # Set up: Create an instance of CLIInterface with the test database
    cli_interface = CLIInterface(main_db_location, test_db_location)
    
    yield cli_interface  # The test runs here
    
    # Teardown: Reset the test database after the test
    cli_interface.resetdb(test_db_location)

def test_create_table(setup_teardown):
    # Arrange
    cli_interface = setup_teardown

    # Act
    result = cli_interface.run(["create_table", "--table", "test_table"])

    # Assert
    assert result is True
    assert "test_table" in cli_interface.tables

# Add more test functions for other commands (set, get, delete, reset_table, resetdb)
