# Flask example

Simple barebones Python Flask example

## Get started

(Assuming you have python 3 installed)

1. Download the code from this repo via the "Download" "button
2. Unzip ZIP file somewhere (e.g. `/Users/simon/flask-example`)
3. Open up a Terminal (on OSX aptly called "Terminal")

Execute these commands step by step: (without the $ part)

```bash
$ cd /Users/simon/flask-example
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install Flask
```

Now you're ready to start the application

```bash
$ FLASK_APP=hello.py flask run 
```

You should see some output:

```bash
 * Serving Flask app "hello.py"
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Don't close the terminal! Switch to your browser and surf to
http://127.0.0.1:500.

Enjoy!
