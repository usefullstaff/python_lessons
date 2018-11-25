import sqlite3


def test_connect(db_name):
	conn  = sqlite3.connect(db_name)
	cur = conn.cursor()
	cur.execute("INSERT * FROM tasks")
	rows = cur.fetchall()
	rows = cur.fetchone()
	conn.commit()
	conn.close()