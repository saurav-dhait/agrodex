from flask import Flask, request, render_template, redirect,session,url_for, render_template_string,flash

app = Flask(__name__,template_folder="templates",static_folder="static",static_url_path='/')
EMAILS = ['tessco913@gmail.com']
PASS = ["1234"]
app.secret_key = 'yay'
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
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('pass')
        if email in EMAILS and password in PASS:
            session['email'] = email
            return redirect(url_for('streamlit'))
        else:
            flash("Invalid Credentials")
            return render_template("login.html")
    return render_template("login.html")
@app.route("/streamlit",methods=["GET","POST"])
def streamlit():
    return render_template('streamlit.html')

if __name__ == '__main__':
    app.run("0.0.0.0")