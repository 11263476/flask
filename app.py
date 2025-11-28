from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/home/<user>")
def profile(user):
    return render_template("home.html", user=user)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        if username == "":
            return "Username cannot be empty"
        return f"Hello {username}! You are logged in."
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
