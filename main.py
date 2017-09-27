from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader - jinja2.FilesSystemLoader(template_dir))

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
"""

@app.route("/")
def index():
    return form

@app.route("/hello", methods=['POST'])
def hello():
    first_name = request.form['first_name']
    return "<h1>Hello, " + cgi.escape(first_name) + "</h1>"

time_form = """
    <style>
    .error {{ color: red; }}
    </style>
    <h1>Validate Time</h1>
    <form method='POST'>
        <label>Hours (24-hour format)
            <input name="hours" type="text" value=
"""

app.run()
