import os
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from termcolor import colored
from quiz import Quiz
UPLOAD_FOLDER = 'static/videos/'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def quizes():
    return render_template('test_1.html')
if __name__=='__main__':
    app.secret_key='dsa123'
    app.run(debug=True)
