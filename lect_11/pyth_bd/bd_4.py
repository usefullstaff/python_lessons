import sqlite3


def select_songs(artist_name):
	conn  = sqlite3.connect('test_base.db')
	cur = conn.cursor()

	song = 'SELECT * FROM songs WHERE artist = {}'.format(artist_name)
	cur.execute(song)
	songs = cur.fetchall()

	conn.commit()
	conn.close()
	return songs
	pass