import pytest


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
