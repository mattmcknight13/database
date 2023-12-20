import pytest


def test_reset_database(setup_teardown):
    cli_interface = setup_teardown
    
    # Set a value
    cli_interface.run(["set", "--table", "test_table", "--key", "name", "--value", "John", "--test"])
    
    # Reset the database
    result = cli_interface.run(["resetdb", "--test"])
    
    # Assert results
    assert result is True
    assert cli_interface.tables == {}
