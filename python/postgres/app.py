import psycopg

conn = psycopg.Connection.connect(dbname="mydb")
cur = conn.execute("select now()")
print(cur.fetchone()[0])

cur.close()
conn.close()

