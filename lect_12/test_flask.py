from flask import Flask, render_template, request
import component
app = Flask(__name__)
app.debug = True


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/echo')
def echo():
    component.bot.echo_mess()
    return render_template('about.html')

@app.route('/movies')
def movies_list():
    component.bot.send_message(text_message = str(component.movies_today))
    return render_template('movies.html', movies = component.movies_today)
    pass







if __name__ == '__main__':
	app.run()

