import psycopg2
from psycopg2 import Error

class PasswordDatabase:

  def __init__(self):

    try:
      #TODO: add to database.ini file
      self.connect = psycopg2.connect(user='test_user_1', password='test_password', host='localhost', port='5432', database='python_password')
      self.cursor = self.connect.cursor()

    except (Exception, Error) as error:
      print('Error connecting to PostgreSQL', error)

  '''
  This method adds a user into the database with their hashed password
  and a unique salt IF they don't exist in the database

  If the username is already in the database, raise an exception
  '''
  def addUser(self,uname,hashObj):

    sql = 'INSERT INTO accounts(username,password,salt) VALUES(%s,%s,%s);'

    try:
      self.cursor.execute(sql,(uname,hashObj.pwd,hashObj.salt))
      self.connect.commit()
      print('Successfully added account %s!' % uname)

    except(psycopg2.IntegrityError):
      raise UserExistsException

    except(Exception, psycopg2.DatabaseError) as error:
      print(error)

  '''
  This method grabs the username, hashed password, and unique salt from the database
  to use for authentication
  '''
  def selectUser(self,uname):

  def addEntry(self)

  def closeDB(self):
    self.cursor.close()
    self.connect.close()