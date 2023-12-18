from .cli import CLIInterface

main_db_location = "mydb.json"
test_db_location = "test.json"

if __name__ == "__main__":
    
    cli_interface = CLIInterface(main_db_location, test_db_location)
    cli_interface.run()

### TODO
# fix create_table (think we need to instanciate different instances based on db)
# add ability to create multiple tables at once to speed up start steps
# move current testing teardown setup stuff to own file to import to tests (dry code practices)
###
    
### Current Issues
# testing imports work but running database from cli isn't working in this format (file structure issue?)
# database information is hanging over been main run and --test flag duplicating data across databases 
###

### Goals
# add forigen key reference to join tables
# command line interface **
#  - query language as dumb as possible
#  - peristance
#  - actions
###
    