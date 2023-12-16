from cli import CLIInterface

if __name__ == "__main__":
    main_db_location = "mydb.json"
    test_db_location = "test.json"

    cli_interface = CLIInterface(main_db_location, test_db_location)
    cli_interface.run()

### TODO
# make sure we can clean up (nuke) after tests
# setup .toml file
# fix create_table (think we need to instanciate different instances based on db)
# add ability to create multiple tables at once to speed up start steps
###
    