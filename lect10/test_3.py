from flask import Flask
app = Flask(__name__)
#app.debug = True



@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/about')
def show_about():
    return 'info about company'


@app.route('/<int:user_id>')
def show_user(user_id):
    return 'User {}'.format(user_id)


if __name__ == '__main__':
    app.run(debug=True)

