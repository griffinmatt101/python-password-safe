# python-password-safe
Password manager written in Python, using DB connections through PostgreSQL

## 3 Main Steps

### 1)
Grab user input from console

### 2)
Create function to hash input

### 3)
Store hash in postgresql db

### Stretch goals
- Create custom hash function
- Password generator

### References
- https://www.geeksforgeeks.org/hashing-passwords-in-python-with-bcrypt/
- https://www.postgresqltutorial.com/postgresql-python/connect/
- https://itecnote.com/tecnote/python-connect-to-a-db-using-psycopg2-without-password/
- https://www.peterbe.com/plog/connecting-with-psycopg2-without-a-username-and-password

### Database Structure (WIP)
++++++++++++++++++++++++++++++++
| table_name | 
| user_1     | 
| user_2     |
|    .       |
|    .       |
|    .       |
| user_n     |

user_n table
| id | service_name | service_pwd_encrypt |
| 1  | example_1    | example_1_encrypt   |
| 2  | example_2    | example_2_encrypt   |