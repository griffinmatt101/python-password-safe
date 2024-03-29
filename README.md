# python-password-safe
Password manager written in Python, using DB connections through PostgreSQL

(CURRENTLY UNDER CONSTRUCTION)

## 3 Main Steps

### 1)
Grab user input from console

### 2)
Create functions for:
- Storing user's main (hashed) password in keyring
- Add entries for applications/sites and their corresponding passwords
- Retrieve passwords
- Make sure to authenticate users

### 3)
Store entries in postgresql db

### Stretch goals
- Create custom hash function
- Password generator
- Delete account

### TODO
- Write unit tests
- Write DB functions
- Write check auth function
- Create custom exceptions

### References
- https://www.geeksforgeeks.org/hashing-passwords-in-python-with-bcrypt/
- https://www.postgresqltutorial.com/postgresql-python/connect/
- https://martinheinz.dev/blog/59
- https://pynative.com/python-postgresql-tutorial/
- https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-create-table/
- https://timothybramlett.com/How_to_create_a_Python_Package_with___init__py.html
- https://coverage.readthedocs.io/en/6.0/
- Run unit test example: `python3 -m unittest AccountsTest.py`
- Run code coverage: `coverage run -m unittest AccountsTest.py`
- Display code coverage: `coverage report -m`

### Database Structure (WIP)

- Note: Need to store salt in a different table to minimize security risk

<pre>

user_accounts table
________________________________________________
|   usernames   |   hash_salt   |   hash_pwd   |
|   user_1      |   salt_1      |   hash1      |
|   user_2      |   salt_2      |   hash2      |
|______________________________________________|

user_n table
______________________________________
| service name | service pwd encrypt |
| example 1    | example 1 encrypt   |
| example 2    | example 2 encrypt   |
|____________________________________|
</pre>