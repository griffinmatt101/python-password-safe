import psycopg2
import sys

def db_con():
  #connection string
  #add to database.ini file?
  connect_str = "host='localhost' dbname='python_password' user='test_user_1' password='test_password'"

  connect = psycopg2.connect(connect_str)

  #resturns a cursor object
  cursor = connect.cursor()
  print('Connected!\n')