import os
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

relative_path = '/static/upload/img'
upload_dir = os.path.abspath('.' + relative_path)

images = ['/asdfasd']

def create_app():
    app = Flask(
        __name__,
        static_folder='../../static',
        template_folder='../templates'
    )

    app.config['UPLOAD_FOLDER'] = upload_dir

    @app.route("/")
    def hello():
        return render_template("index.html", images=images)

    @app.route("/upload", methods = ["POST"])
    def upload():
        if  'file' not in request.files:
            return redirect('/')

        file = request.files['file']

        if file.filename == '':
            return redirect('/')

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        images.append(relative_path + '/' + filename)

        return redirect('/')


    @app.route("/ping")
    def ping():
        env = app.config['ENV']
        debug = app.config['DEBUG']

        return render_template("ping.html")

    return app
