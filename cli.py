import argparse
from basedb import BaseDB

class CLIInterface(BaseDB):
  def __init__(self, location):
    super().__init__(location)

    self.parser = argparse.ArgumentParser(description="cli interface for BaseDB.")
    self.parser.add_argument("command", choices=["create_table", "set", "get", "delete", "reset_table", "resetdb"],
                             help="Command to execute.")
    self.parser.add_argument("--table", help="Table name")
    self.parser.add_argument("--key", help="Key name")
    self.parser.add_argument("--value", help="Value name")

  def run(self):
        # Parse the command-line arguments
        args = self.parser.parse_args()

        # Execute the corresponding command
        if args.command == "create_table":
            self.create_table(args.table)
        elif args.command == "set":
            self.set(args.table, args.key, args.value)
        elif args.command == "get":
            result = self.get(args.table, args.key)
            if result is not None:
                print(result)
        elif args.command == "delete":
            self.delete(args.table, args.key)
        elif args.command == "reset_table":
            self.reset_table(args.table)
        elif args.command == "resetdb":
            self.resetdb()

# Example usage:
if __name__ == "__main__":
    cli_interface = CLIInterface("mydb.db")
    cli_interface.run()