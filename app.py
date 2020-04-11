#!flask/bin/python
from flask import Flask, jsonify, request, render_template
from flask import redirect, url_for

from db_handler.MySqliteDB import MySqliteDatabase

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


# http://localhost:5000/todo/tasks
@app.route('/todo/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


# http://localhost:5000/
@app.route('/', methods=['GET'])
def index():
    return render_template("login.html")
    # return "<h1>Hello Flask</h1>"


# http://localhost:5000/admin
@app.route('/admin')
def hello_admin():
    return 'Hello Admin'


# http://localhost:5000/guest/Pritesh+Patel
@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' % guest


# http://localhost:5000/user/Pritesh
@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


# http://localhost:5000/success/Pritesh_Patel
@app.route('/success/<name>')
def success(name):
    return 'Welcome <B>%s</B>' % name


# http://localhost:5000/login
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


# http://localhost:5000/hello/Pritesh+Patel
@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html', name=user)


# http://localhost:5000/student
@app.route('/student')
def student():
    return render_template('student.html')


# http://localhost:5000/result
@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result=result)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


# http://localhost:5000/books/all
@app.route('/books/all', methods=['GET'])
def getAllBooks():
    db = MySqliteDatabase()
    return db.getAll()


# http://localhost:5000/books?published=1993
@app.route('/books', methods=['GET'])
def api_filter():
    query_parameters = request.args
    published = query_parameters.get('published')
    db = MySqliteDatabase()
    return db.getBooksByPublishedYear(published)


if __name__ == '__main__':
    app.run(debug=True)
