creating a database from scratch

example of commands

Create a table
```
python your_script.py create_table --table users
```

Set a value
```
python your_script.py set --table users --key john_doe --value '{"age": 25, "city": "New York"}'
```

Get a value
```python your_script.py get --table users --key john_doe
```

Target a test database
```
python your_script.py set --table users --key jane_doe --value '{"age": 30, "city": "San Francisco"}' --test
```