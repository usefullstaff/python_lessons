from flask import Flask, render_template, request
from bot import lect_bot
import funcs
app = Flask(__name__)
app.debug = True



@app.route('/')
def hello_world():
	bands_list = funcs.get_music_info(funcs.sel_all_artists)
	return render_template('base.html', bands = bands_list)


@app.route('/<band_name>')
def show_band(band_name):
	about_band = funcs.get_music_info(funcs.sel_band_info.format("'"+band_name+"'"))
	songs_list = funcs.get_music_info(funcs.sel_band_songs.format("'"+band_name+"'"))
	return render_template('profile.html', about_band = about_band, songs_list = songs_list)
	pass



if __name__ == '__main__':
	app.run()

