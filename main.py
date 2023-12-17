from .cli import CLIInterface

main_db_location = "mydb.json"
test_db_location = "test.json"

if __name__ == "__main__":
    
    cli_interface = CLIInterface(main_db_location, test_db_location)
    cli_interface.run()

### TODO
# make sure we can clean up (nuke) after tests
# setup .toml file
# create unit tests
# fix create_table (think we need to instanciate different instances based on db)
# add ability to create multiple tables at once to speed up start steps
    
# add forigen key reference to join tables
# command line interface **
#  - query language as dumb as possible
#  - peristance
#  - actions
###
    
### Issues to fix
# testing isn't working getting import issues, need to move into integration directory in tests
# database information is hanging over been main run and --test flag duplicating data across databases 
###
    