import psycopg2
import json



def simple_select():
    psql_conn = psycopg2.connect(database = 'bands', user = 'postgres', password = '1234567q',  port = "5432")
    cur = psql_conn.cursor()


    sel_all = "SELECT * FROM bands"
    bands  = cur.execute(sel_all)        
    print(bands) 

    psql_conn.commit()
    psql_conn.close()


simple_select()

