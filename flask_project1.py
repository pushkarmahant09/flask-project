from flask import Flask, request, redirect, Response, url_for, session

app = Flask(__name__)

app.secret_key = "supersecret"


@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "pushkar" and password == "9009":
            session["user"] = username
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid credentials.Please try again laater", mimetype="text/plain")

    return ''' 
           <h2>Login Page</h2>
           <form method="POST">
            Username: <input type="text" name="username"><br> Password: <input type-"text" name="password"><br>
            <input type="submit" value="Login">
            </ form>

'''


@app.route("/welcome")
def welcome():
    if "user" in session:
        return f'''
      <h2>welcome{session["user"]}!</h2>
      <a href ={url_for('logout')}>logout</a>

   '''
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))