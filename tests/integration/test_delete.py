import pytest


def test_delete_value(setup_teardown):
    cli_interface = setup_teardown
    cli_interface.run(["create_table", "--table", "test_table", "--test"])
    
    # Set a value
    cli_interface.run(["set", "--table", "test_table", "--key", "name", "--value", "John", "--test"])
    
    # Delete the value
    result = cli_interface.run(["delete", "--table", "test_table", "--key", "name", "--test"])
    
    # Assert the value is deleted
    assert result is True
    # breakpoint()
    assert cli_interface.run(["get", "--table", "test_table", "--key", "name", "--test"]) is None
