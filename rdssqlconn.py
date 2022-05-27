import pymysql

# url parts for fetching data using api

def mysqlconnect():
# To connect MySQL database
    conn = pymysql.connect(
        host='********.amazonaws.com',
        port=3306,
        user='admin', 
        password = "****",
        db='******db',
        )
    return conn

conn = mysqlconnect()
cur = conn.cursor()
    
    
# Select query
cur.execute("select * from stocktracker")
records = cur.fetchall()

for i in records:
    print(i)

cur.close()
conn.close()
