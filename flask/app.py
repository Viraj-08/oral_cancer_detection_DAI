from flask import Flask, jsonify, render_template, request, redirect, flash, url_for
import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './static/upload'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__, template_folder="templates")

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def homepge():
    return index()
    # return scan()

@app.route("/index", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.fileUpload:
            flash('No file part')
            return redirect(request.url)
        file = request.fileUpload['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return render_template("index.html")

@app.route("/aboutUs")
def aboutUs():
    return render_template("aboutUs.html")

@app.route("/case_study")
def case_study():
    return render_template("case_study.html")

@app.route("/our_work")
def our_work():
    return render_template("our_work.html")

@app.route("/get_in_touch")
def get_in_touch():
    return render_template("get_in_touch.html")

@app.route("/acc/sudeep_linkedin")
def sudeep_linkedin():
    return redirect("https://www.linkedin.com/in/sudeep-roy-54a7b6247/")


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error404.html'), 404


if __name__ == '__main__':  
   app.run(debug=True, host='0.0.0.0', port=5000)

