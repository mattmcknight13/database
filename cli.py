import argparse
from typing import List , Optional, Any
import basedb

class CLIInterface(basedb.BaseDB):
    def __init__(self, location: str, test_location: str) -> None:
        super().__init__(location)
        self.test_location = test_location

        # Create the command-line argument parser
        self.parser = argparse.ArgumentParser(description="Simple CLI for a basic database.")
        self.parser.add_argument("command", choices=["create_table", "set", "get", "delete", "reset_table", "resetdb"],
                                 help="Command to execute")
        self.parser.add_argument("--table", help="Table name")
        self.parser.add_argument("--key", help="Key")
        self.parser.add_argument("--value", help="Value")
        self.parser.add_argument("--test", action="store_true", help="Use test database")

    def run(self, args_list: Optional[List[str]] = None) -> Any:
        # Parse the command-line arguments
        args = self.parser.parse_args(args_list)

        # Determine the database location based on the --test flag
        db_location = self.test_location if args.test else self.location

        # Execute the corresponding command with the specified file path
        if args.command == "create_table":
           return self.create_table(db_location, args.table)
        elif args.command == "set":
           return self.set(db_location, args.table, args.key, args.value)
        elif args.command == "get":
            result = self.get(db_location, args.table, args.key)
            if result is not None:
                print(result)
            return result
        elif args.command == "delete":
           return self.delete(db_location, args.table, args.key)
        elif args.command == "reset_table":
           return self.reset_table(db_location, args.table)
        elif args.command == "resetdb":
           return self.resetdb(db_location)
        
        print(f"Unrecognized command: {args.command}")
        return False
