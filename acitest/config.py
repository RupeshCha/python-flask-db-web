import os
'''
user = 'postgres' #os.environ['POSTGRES_USER']
password = '' #os.environ['POSTGRES_PASSWORD']
host = '172.22.146.148' #os.environ['POSTGRES_HOST']
database = 'postgres' #os.environ['POSTGRES_DB']
port = '32768' #os.environ['POSTGRES_PORT']

'''
user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
host = os.environ['POSTGRES_HOST']
database = os.environ['POSTGRES_DB']
port = os.environ['POSTGRES_PORT']

DATABASE_CONNECTION_URI = f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}'
