import os
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    @app.route("/")
    def hello():
        return "Hello World!"

    @app.route("/ping")
    def ping():
        env = app.config['ENV']
        debug = app.config['DEBUG']
    
        return "It's alive. Environment: {}. Debug: {}".format(env, debug)

    return app