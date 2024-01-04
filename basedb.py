import json
import os
from typing import Any, Optional

class BaseDB(object):
    def __init__(self, location: str) -> None:
        self.location = os.path.expanduser(location)
        self.tables = {}
        self.load(self.location)

    # create location in memory
    def load(self, location: str)-> bool:
        if os.path.exists(location):
            self._load(location)
        else:
            self.tables = {}
        return True
    
    # load tables into database
    def _load(self, location:str) -> None:
      try:
          with open(location, "r") as file:
              data = json.load(file)
          for table_name, table_data in data.items():
              self.tables[table_name] = table_data
      except (json.JSONDecodeError, FileNotFoundError):
          # Handle the case when the file is empty or does not exist
          self.tables = {}

    # overwrite database
    def dumpdb(self, location: str) -> bool:
        try:
            json.dump(self.tables, open(location, "w+"))
            return True
        except Exception as e:
            print("[X] Error Saving Tables to Database : " + str(e))
            return False

    # create a table in database
    def create_table(self,location: str, table_name: str) -> bool:
        if table_name not in self.tables:
            self.tables[table_name] = {}
            self.dumpdb(location)
            return True
        else:
            print(f"Table '{table_name}' already exists in database {location}.")
            return False

    # add table and dump into database
    def set(self,location: str, table_name: str, key: str, value: Any) -> bool:
        try:
            if table_name not in self.tables:
                self.create_table(location, table_name)
            self.tables[table_name][str(key)] = value
            self.dumpdb(location)
            return True
        except Exception as e:
            print("[X] Error Saving Values to Table : " + str(e))
            return False

    # get key value from table with optional filters
    def get(self, location: str, table_name: str, key: str, filters: Optional[dict] = None) -> Any:
        try:
            value = self.tables[table_name][key]

            if filters:
                for filter_key, filter_value in filters.items():
                    if value.get(filter_key) != filter_value:
                        return None
            
            return value
        except KeyError:
            print(f"No value can be found for key '{key}' in table '{table_name}'.")
            return None

    # delete key value from table
    def delete(self,location: str, table_name: str, key: str) -> bool:
        if table_name in self.tables and key in self.tables[table_name]:
            del self.tables[table_name][key]
            self.dumpdb(location)
            return True
        else:
            return False

    # empty table in database
    def reset_table(self,location: str, table_name: str) -> bool:
        if table_name in self.tables:
            self.tables[table_name] = {}
            self.dumpdb(location)
            return True
        else:
            print(f"Table '{table_name}' does not exist.")
            return False

    #  empty database
    def resetdb(self, location: str) -> bool:
        self.tables = {}
        self.dumpdb(location)
        return True
