from flask import Flask, request, render_template, redirect

app = Flask(__name__,template_folder="templates",static_folder="static",static_url_path='/')

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html")

@app.route("/about",methods=["GET","POST"])
def about():
    return render_template("about_us.html")

@app.route("/contact",methods=["GET","POST"])
def contact():
    return render_template("contact.html")

@app.route("/blog",methods=["GET","POST"])
def blog():
    return render_template("blog.html")

@app.route("/login",methods=["GET","POST"])
def login():
    return render_template("login.html")


if __name__ == '__main__':
    app.run("0.0.0.0")