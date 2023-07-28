import psycopg2
from psycopg2 import Error

def db_con():
  #connection string
  #add to database.ini file?
  #connect_str = "host='localhost' dbname='python_password' user='test_user_1' password='test_password'"

  try:
    connect = psycopg2.connect(user='test_user_1', password='test_password', host='localhost', port='5432', database='python_password')
    #create a cursor to perform db operations
    cursor = connect.cursor()

    print("PostgreSQL server info: ")
    print(connect.get_dsn_parameters(),'\n')

    #execute query
    cursor.execute('SELECT version();')

    record = cursor.fetchone()
    print('Connected to: ', record, '\n')

  except (Exception, Error) as error:
    print('Error connecting to PostgreSQL', error)
  finally:
    if(connect):
      cursor.close()
      connect.close()
      print('PostgreSQL connection is closed')