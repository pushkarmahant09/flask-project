from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)
app.secret_key="secretkey"
dict = {
   "pushkar": "1234",
   "rahul": "0000"
}
@app.route('/')
def index():
   return render_template("login.html")

@app.route("/idiot")
def idiot():
   return"PLEASE ENETER VALID CREDENTIALS"

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        dict[username] = password

        return redirect(url_for("index"))

    return render_template("signup.html")


@app.route("/submit",methods=["POST"])
def submit():
   username=request.form.get("username")
   password=request.form.get("password")



   if username=="" and password=="":
      return  redirect(url_for("idiot"))
   elif username in dict:
      if password==dict[username]:
         return render_template("welcome.html",name=username)

      else:
         return "WRONG PASSWORD"
   else:
       return"WRONG USERNAME"




