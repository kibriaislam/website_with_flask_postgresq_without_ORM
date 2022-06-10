import psycopg2
import os
from dotenv import load_dotenv

load_dotenv('.env')


#establishing the connection
conn = psycopg2.connect(database=os.environ['db_name'], user='postgres', password=os.environ['db_password'], host='localhost', port= '5432')
#Creating a cursor object using the cursor() method
cursor = conn.cursor()
