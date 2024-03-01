#!/usr/bin/python3
"""
start Flask application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/airbnb_onepage/', strict_slashes=False)
def hello():
    """returns a gi0ven string000"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=None)
