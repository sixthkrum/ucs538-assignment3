import os
from appConverter import app
from flask import Flask, flash, request, redirect, render_template, url_for, send_file
from werkzeug.utils import secure_filename
import filetype
from convertBW import convertVideoToBW

def isVideo(stream):
    if str(filetype.guess(stream)).find('video') == -1:
        return 0
    return 1

@app.route('/ucs538-assignment3-q1/')
def uploadForm():
    return render_template('uploadConvert.html')

@app.route('/ucs538-assignment3-q1', methods = ['POST'])
def uploadConvertFile():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file sent in post request')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('No file selected')
            return redirect(request.url)

        if file and isVideo(file):
            filePath = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename))
            file.save(filePath)
            outputPath = convertVideoToBW(filePath)
            return send_file(outputPath, as_attachment = True)

        else:
            flash('Only videos are allowed')
            return redirect(request.url)

if __name__ == '__main__':
    app.run()
