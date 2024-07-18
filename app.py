# save this as app.py
from flask import Flask, render_template, request, send_from_directory
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "sqlite:///sqlite3.db"
)
db = SQLAlchemy(app)


app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = "jeemannu90@gmail.com"
app.config["MAIL_PASSWORD"] = "icbh jolb cnuv dnbq"
app.config["MAIL_USE_TLS"] = False
app.config["MAIL_USE_SSL"] = True

mail = Mail(app)
mail.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/robots.txt")
@app.route("/sitemap.xml")
@app.route("/BingSiteAuth.xml")
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])


class Details(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    subject = db.Column(db.String(200), nullable=False)
    msg = db.Column(db.String(200), nullable=False)

    def __repr__(self) -> str:
        return f"{self.s_no} - {self.title}"


class Crediantials(db.Model):
    ID = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self) -> str:
        return f"{self.username}"


@app.errorhandler(404)
def page_not_found(e):
    # Your custom logic here (logging, notifications, etc.)
    return render_template("404.html"), 404


@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        names = request.form["names"]
        emails = request.form["emails"]
        subjects = "IT" + " " + request.form["subjects"]
        msgs = request.form["msgs"]
        try:
            from Emails import Submission_Mail

            Submission_Mail(names, emails, subjects, msgs)
        except Exception as e:
            return f"{e}"

        details = Details(name=names, email=emails, subject=subjects, msg=msgs)
        db.session.add(details)
        db.session.commit()  # Commit the changes once
        return render_template("thankyou.html")
    return render_template("index.html")


@app.route("/project-showcase/<string:name>", methods=["POST", "GET"])
def projects(name):
    if name == "OG":
        return render_template("Projects/OG.html")
    elif name == "DB":
        return render_template("Projects/DB.html")
    elif name == "MAC":
        return render_template("Projects/MAC.html")
    elif name == "CM":
        return render_template("Projects/CM.html")

    return "404 Not Found"


@app.route("/administrator", methods=["POST", "GET"])
def Admin():
    if request.method == "POST":
        username = request.form["Username"]
        password = request.form["password"]
        admi = Crediantials.query.filter_by(
            username=username, password=password
        ).first()
        if admi:
            details = Details.query.all()
            return render_template("Database.html", details=details)
        else:
            return render_template("403.html")

    return render_template("login.html")


@app.route("/profile-mis", methods=["POST", "GET"])
def MIS():
    if request.method == "POST":
        names = request.form["names"]
        emails = request.form["emails"]
        subjects = "MIS" + " " + request.form["subjects"]
        msgs = request.form["msgs"]
        try:
            from Emails import Submission_Mail
            Submission_Mail(names, emails, subjects, msgs)
        except Exception as e:
            return f"{e}"
        details = Details(name=names, email=emails, subject=subjects, msg=msgs)
        db.session.add(details)
        db.session.commit()
        return render_template("thankyou.html")
    return render_template("MIS.html")


@app.route("/delete/<int:ID>", methods=["POST", "GET"])
def delete(ID):
    query = Details.query.get(ID)
    if query:
        db.session.delete(query)
        db.session.commit()
        return jsonify({"message": f"Item with ID {ID} deleted successfully"})


if __name__ == "__main__":
    app.run(debug=True, port=8000)
