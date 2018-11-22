from flask import Flask, render_template, request

app = Flask(__name__)
#app.debug = True



@app.route('/')
def hello_world():
    return 'Hello World!'
    pass

@app.route('/about')
def show_about():
    return render_template('about.html')
    pass


@app.route('/<int:user_id>', methods=['POST', 'GET'])
def show_user(user_id):
    if request.method == 'POST':
        print(request.form['message'])

    return render_template('profile.html')
    pass











if __name__ == '__main__':
    app.run(debug=True)

