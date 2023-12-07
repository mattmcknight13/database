import json
import os

class BaseDB(object):
    def __init__(self, location):
        self.location = os.path.expanduser(location)
        self.tables = {}
        self.load(self.location)

    # create location in memory
    def load(self, location):
        if os.path.exists(location):
            self._load()
        else:
            self.tables = {}
        return True
    
    # load tables into database
    def _load(self):
        data = json.load(open(self.location, "r"))
        for table_name, table_data in data.items():
            self.tables[table_name] = table_data

    # overwrite database
    def dumpdb(self):
        try:
            json.dump(self.tables, open(self.location, "w+"))
            return True
        except Exception as e:
            print("[X] Error Saving Tables to Database : " + str(e))
            return False

    # create a table in database
    def create_table(self, table_name):
        if table_name not in self.tables:
            self.tables[table_name] = {}
            self.dumpdb()
            return True
        else:
            print(f"Table '{table_name}' already exists.")
            return False

    # add table and dump into database
    def set(self, table_name, key, value):
        try:
            if table_name not in self.tables:
                self.create_table(table_name)
            self.tables[table_name][str(key)] = value
            self.dumpdb()
            return True
        except Exception as e:
            print("[X] Error Saving Values to Table : " + str(e))
            return False

    # get key value from table
    def get(self, table_name, key):
        try:
            return self.tables[table_name][key]
        except KeyError:
            print(f"No value can be found for key '{key}' in table '{table_name}'.")
            return None

    # delete key value from table
    def delete(self, table_name, key):
        if table_name in self.tables and key in self.tables[table_name]:
            del self.tables[table_name][key]
            self.dumpdb()
            return True
        else:
            return False

    # empty table in database
    def reset_table(self, table_name):
        if table_name in self.tables:
            self.tables[table_name] = {}
            self.dumpdb()
            return True
        else:
            print(f"Table '{table_name}' does not exist.")
            return False

    #  empty database
    def resetdb(self):
        self.tables = {}
        self.dumpdb()
        return True


# add a update table method
# add forigen key reference to join tables
# command line interface **
#  - query language as dumb as possible
#  - peristance
#  - actions