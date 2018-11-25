import sqlite3


import json
music_data = json.load(open('music.json', encoding="utf8"))


def insert_music():
	conn  = sqlite3.connect('test_base.db')
	cur = conn.cursor()
	for band in music_data['music']['bands']:
		insert_band = 'INSERT INTO bands VALUES({},{},{})'.format('"'+band['name']+'"',band['start_year'],'"'+band['type']+'"')
		cur.execute(insert_band)


	for song in music_data['music']['songs']:
		insert_song = 'INSERT INTO songs VALUES({},{})'.format('"'+song['name']+'"','"'+song['artist']+'"')
		cur.execute(insert_song)

	conn.commit()
	conn.close()


insert_music()



"""

CREATE TABLE songs (
    name,
    artist  REFERENCES bands (name) ON DELETE CASCADE
);

"""