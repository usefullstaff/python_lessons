from flask import Flask,render_template

app = Flask(__name__)
#app.debug = True



@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/about')
def show_about():
    return render_template('about.html')


@app.route('/<int:user_id>')
def show_user(user_id):
    some_date = 'Some text'
    return render_template('profile.html', user_id=user_id, text = some_date,)
    pass




if __name__ == '__main__':
    app.run(debug=True)

