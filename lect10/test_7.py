from flask import Flask, render_template, request
from bot import lect_bot
app = Flask(__name__)
app.debug = True



@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/about')
def show_about():
    return render_template('about.html')


@app.route('/<int:user_id>', methods=['POST', 'GET'])
def show_user(user_id):
    if request.method == 'POST':
        lect_bot.bot.send_message(text_message = request.form['message'])

    return render_template('profile.html')
    pass











if __name__ == '__main__':
    app.run()

