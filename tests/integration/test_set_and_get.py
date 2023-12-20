import pytest


def test_set_and_get_values(setup_teardown):
    cli_interface = setup_teardown
    cli_interface.run(["create_table", "--table", "test_table", "--test"])
    
    # Set a value
    cli_interface.run(["set", "--table", "test_table", "--key", "name", "--value", "John", "--test"])
    
    # Get the value and assert
    result = cli_interface.run(["get", "--table", "test_table", "--key", "name", "--test"])
    assert result == "John"