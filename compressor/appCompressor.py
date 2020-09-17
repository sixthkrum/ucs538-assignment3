from flask import Flask

app = Flask(__name__, template_folder = "templates")
app.secret_key = "2394723023940"
app.config['UPLOAD_FOLDER'] = '/home/user/apps/ucs538-assignment3/compressor/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
