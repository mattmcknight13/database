from cli import CLIInterface

if __name__ == "__main__":
    cli_interface = CLIInterface("mydb.json")
    cli_interface.run()

# add ability to select database target
# make sure we can clean up (nuke) after tests
# add git ignore for database files
# setup .toml file