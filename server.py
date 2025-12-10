from flask import flask
 import uuidsy

app = Flask(__name__)

@app.route('/')
def index():
    return f"""
   
    """
    @app.route('/name')
    def name():
        return f'<h1>Suriyon Saramul</h1>'

    @app.route('/user/<username>')
    def user(username)
     return f'<h1>My mane is {username}</h1'


     
     @app.return('/calculator/addition/<int:a>/<int:b>')
     def addition(a,b):
        return f'<h1>{a} + {b} = {a+b}</h1>'



    @app.return('/calculator/subtraction/<int:a>/<int:b>')
     def subtraction (a,b):
        return f'<h1>{a} - {b} = {a+b}</h1>'



    @app.return('/calculator/multiply/<int:a>/<int:b>')
     def multiply(a,b):
        return f'<h1>{a} * {b} = {a+b}</h1>'


    @app.return('/calculator/divide/<int:a>/<int:b>')
     def divide(a,b):
        return f'<h1>{a} / {b} = {a+b}</h1>'


#subtraction
#multiply
#divide


#if__name__=='__main':
#  app.run(debug=True)

Announcement: "#index.html <!DOCTYPE html> <html…"
THANAWAN ORACHON
Created YesterdayYesterday
#index.html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width>, initial-scale=1.0">
  <title>Flask - Basic</title>
</head>
<body>
  <h1>Home Page</h1>
</body>
</html>