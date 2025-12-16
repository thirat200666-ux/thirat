from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Flask - Basic</title>
</head>
<body>
    <h1>Home Page</h1>
    <hr>
</body>
</html>

'''


@app.route('/<name>')
def show_name(name):
    return f'<h1>My name is {name}</h1>'


@app.route('/hello/<name>')
def hello(name):
    return f'<h1>Hello, {name}</h1>'

@app.route('/greeting/<name>/<int:age>')
def greeting(name, age):
    return f'<h1>My name is, {name}. I am {age} years old.</h1>'

@app.route('/caculate/addition/<int:a>/<int:b>')
def addition(a, b):
    return f'<h1>{a} + {b} = {a + b}</h1>'

@app.route('/caculate/subtraction/<int:a>/<int:b>')
def subtraction(a, b):
    return f'<h1>{a} - {b} = {a - b}</h1>'


@app.route('/secretkey/<uuid:key>')
def secretkey(key):
    return f'<h1>Your secret key is {key}</h1>'