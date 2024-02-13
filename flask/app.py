from flask import Flask, jsonify, render_template, request, redirect



app = Flask(__name__, template_folder="templates")
@app.route("/")
def homepge():
    return index()
    # return scan()

@app.route("/index")
def index():
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

