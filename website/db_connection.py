import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="blogsite_db", user='postgres', password='alterbridge', host='localhost', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()
