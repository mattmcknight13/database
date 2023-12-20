# tests/test_integration.py
import pytest

def test_create_table(setup_teardown):
    # attach setup/teardown
    cli_interface = setup_teardown

    # run command
    result = cli_interface.run(["create_table", "--table", "test_table", "--test"])
    # Assert results
    assert result is True
    assert "test_table" in cli_interface.tables
