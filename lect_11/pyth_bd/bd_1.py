import sqlite3


conn  = sqlite3.connect('test_base.db')
cur = conn.cursor()
conn.commit()
conn.close()


import psycopg2
conn = psycopg2.connect(database = 'my_base', user = 'egor', password = 'pass12',  port = "5432")

