# python-password-safe
Password manager written in Python, using DB connections through PostgreSQL

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

### References
- https://www.geeksforgeeks.org/hashing-passwords-in-python-with-bcrypt/
- https://www.postgresqltutorial.com/postgresql-python/connect/
- https://martinheinz.dev/blog/59
- https://pynative.com/python-postgresql-tutorial/

### Database Structure (WIP)
<pre>
______________
| table_name |
| user_1     |
| user_2     |
|    .       |
|    .       |
|    .       |
| user_n     |

user_n table 
___________________________________________
| id | service name | service pwd encrypt |
| 1  | example 1    | example 1 encrypt   |
| 2  | example 2    | example 2 encrypt   |
</pre>