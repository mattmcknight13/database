import unittest
import tempfile
import os
from ...basedb import BaseDB

class TestBaseDB(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.temp_dir = tempfile.mkdtemp()
        self.test_db_location = os.path.join(self.temp_dir, "test_db.json")

        # Create an instance of your database with the temporary location
        self.db = BaseDB(self.test_db_location)

    def tearDown(self):
        # Remove the temporary directory and its contents
        if os.path.exists(self.temp_dir):
            for root, dirs, files in os.walk(self.temp_dir, topdown=False):
                for file in files:
                    os.remove(os.path.join(root, file))
                for dir in dirs:
                    os.rmdir(os.path.join(root, dir))
            os.rmdir(self.temp_dir)

    def test_create_table(self):
        table_name = "test_table"
        self.assertTrue(self.db.create_table(self.test_db_location, table_name))

    def test_set_and_get(self):
        table_name = "test_table"
        key = "test_key"
        value = "test_value"

        self.db.create_table(self.test_db_location, table_name)
        self.assertTrue(self.db.set(self.test_db_location, table_name, key, value))

        retrieved_value = self.db.get(self.test_db_location, table_name, key)
        self.assertEqual(retrieved_value, value)

    # Add more test cases as needed

if __name__ == '__main__':
    unittest.main()
