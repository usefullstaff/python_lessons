from flask import Flask, render_template, request
from bot import lect_bot
import funcs_2
app = Flask(__name__)
app.debug = True



@app.route('/')
def hello_world():
	bands_list = funcs_2.get_music_info(funcs_2.sel_all_artists)
	return render_template('base.html', bands = bands_list)
	pass


@app.route('/editor', methods=['POST', 'GET'])
def show_all_songs():
	songs_list = funcs_2.get_music_info(funcs_2.sel_all_songs)

	if request.method == 'POST':
		funcs_2.get_music_info(funcs_2.del_song.format("'"+request.form['song_name']+"'"))
		return render_template('editor.html', songs_list = songs_list)

	if request.method == 'GET':	
		return render_template('editor.html', songs_list = songs_list)
		pass




@app.route('/<int:user_id>', methods=['POST', 'GET'])
def show_user(user_id):
    if request.method == 'POST':
        print(request.form['message'])

    return render_template('profile.html')
    pass









@app.route('/<band_name>')
def show_band(band_name):
	about_band = funcs_2.get_music_info(funcs_2.sel_band_info.format("'"+band_name+"'"))
	songs_list = funcs_2.get_music_info(funcs_2.sel_band_songs.format("'"+band_name+"'"))
	return render_template('profile.html', about_band = about_band, songs_list = songs_list)
	pass



if __name__ == '__main__':
	app.run()

