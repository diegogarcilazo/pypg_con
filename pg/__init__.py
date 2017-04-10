from sqlalchemy import create_engine
import getpass
def pg_con(db, host = 'localhost', encoding = 'cp1252'):
    password = getpass.getpass("Enter your password: ")
    return create_engine('postgresql://postgres:'+password+'@'+host+'/'+db, encoding = encoding)
