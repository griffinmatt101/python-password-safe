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

### TODO
- Write unit tests
- Write DB functions
- Write check auth function

### References
- https://www.geeksforgeeks.org/hashing-passwords-in-python-with-bcrypt/
- https://www.postgresqltutorial.com/postgresql-python/connect/
- https://martinheinz.dev/blog/59
- https://pynative.com/python-postgresql-tutorial/

### Database Structure (WIP)
<pre>

user_accounts table
_________________________________________________________
|   id   |   usernames   |   hash_salt   |   hash_pwd   |
|   1    |   user_1      |   salt_1      |   hash1'     |
|   2    |   user_2      |   salt_2      |   hash2'     |
|_______________________________________________________|

user_n table
___________________________________________
| id | service name | service pwd encrypt |
| 1  | example 1    | example 1 encrypt   |
| 2  | example 2    | example 2 encrypt   |
|_________________________________________|
</pre>