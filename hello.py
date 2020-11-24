from flask import render_template
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    name = "Simon"
    return render_template('hello.html', name=name)

@app.route('/foo/bar')
def foo_bar():
    return render_template("foobar.html")
