import psycopg2
from psycopg2 import Error
from ..exceptions.Exceptions import UserExistsException
from ..exceptions.Exceptions import UserDoesNotExistException
from ..Hash import HashClass 

class PasswordDatabase:

  def __init__(self):

    try:
      #TODO: add to database.ini file
      self.connect = psycopg2.connect(user='test_user_1', password='test_password', host='localhost', port='5432', database='python_password')
      self.cursor = self.connect.cursor()

    except (Exception, Error) as error:
      print('Error connecting to PostgreSQL', error)

  '''
  Adds a user into the database with their hashed password
  and a unique salt IF they don't exist in the database

  If the username is already in the database, raise an exception to be passed back

  TODO: Update sql string format like selectUser function
  '''
  def addUser(self,uname,hashObj):

    sql = 'INSERT INTO accounts(username,password,salt) VALUES(%s,%s,%s);'

    try:

      self.cursor.execute(sql,(uname,hashObj.pwd,hashObj.salt))
      self.connect.commit()
      print('Successfully added account %s!' % uname)

    except(psycopg2.errors.UniqueViolation):
      raise UserExistsException

    except(Exception, psycopg2.DatabaseError) as error:
      print(error)

  '''
  Grabs the username, hashed password, and unique salt from the database
  to use for authentication
  '''
  def selectUser(self,uname):
    sql = 'SELECT password,salt FROM accounts WHERE username=%(uname)s;'
    try:

      self.cursor.execute(sql, {'username' : uname})
      self.connect.commit()
      output = self.cursor.fetchone()

      #empty list, user is not in DB
      if(not output):
        raise UserDoesNotExistException

      hashObj = HashClass()
      hashObj.pwd = output[0][0]
      hashObj.salt = output[0][1]

      return hashObj

    except(Exception, psycopg2.DataError) as error:
      print(error)

  '''
  Creates a new table for an existing user to store their passwords
  TODO: need to figure out when to check if user has a table
  '''
  def createUserTable(self,uname):
    return
  '''
  Adds requested service and password to user's table in database
  '''
  def addEntry(self):
    return

  def closeDB(self):
    self.cursor.close()
    self.connect.close()
