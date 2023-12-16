from cli import CLIInterface

if __name__ == "__main__":
    main_db_location = "mydb.json"
    test_db_location = "test.json"

    cli_interface = CLIInterface(main_db_location, test_db_location)
    cli_interface.run()


# make sure we can clean up (nuke) after tests
# setup .toml file
    