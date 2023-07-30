import psycopg2
from psycopg2 import Error

class PasswordDatabase():

  def __init__(self):

    try:
      #TODO: add to database.ini file
      self.connect = psycopg2.connect(user='test_user_1', password='test_password', host='localhost', port='5432', database='python_password')
      self.cursor = self.connect.cursor()

    except (Exception, Error) as error:
      print('Error connecting to PostgreSQL', error)

  def addUser(self,uname,hashObj):

    #TODO: ADD account_id AND INCREMENT
    sql = 'INSERT INTO accounts(username,password,salt) VALUES(%s,%s,%s);'

    try:
      self.cursor.execute(sql,(uname,hashObj.pwd,hashObj.salt))
      self.connect.commit()
      print('Successfully added account %s!', uname)
    except(Exception, psycopg2.DatabaseError) as error:
      print(error)

  def doesUserExistDB(self,uname):

    sql = 'SELECT ' + uname + ' FROM accounts;'

    try:

      self.cursor.execute(sql)
      print(self.cursor.fetchone())
      self.connect.commit()
      # if successfully executed, we know username exists
      return True

    except psycopg2.errors.UndefinedColumn:
      self.connect.commit()
      return False

  # def dbCon(self):

  #   try:
  #     connect = psycopg2.connect(user='test_user_1', password='test_password', host='localhost', port='5432', database='python_password')
  #     #create a cursor to perform db operations
  #     cursor = connect.cursor()

  #     #print("PostgreSQL server info: ")
  #     #print(connect.get_dsn_parameters(),'\n')

  #     #execute query
  #     #cursor.execute('SELECT version();')

  #     #record = cursor.fetchone()
  #     #print('Connected to: ', record, '\n')

  #   except (Exception, Error) as error:
  #     print('Error connecting to PostgreSQL', error)

  def closeDB(self):
    self.cursor.close()
    self.connect.close()