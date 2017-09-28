from flask import Flask, request, redirect

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!doctype html>
<html>
    <body>
        <form action="/hello" method="post">
            <label for="first-name">First Name:</label>
            <input id="first-name" type="text" name="first_name" />
            <input type="submit" />
        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/hello", methods=["POST"])
def hello():
    firstn = request.form['first_name']
    return "<h1>Hello, " + firstn + "</h1>"


app.run()
