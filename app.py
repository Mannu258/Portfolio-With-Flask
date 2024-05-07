# save this as app.py
from flask import Flask,render_template,request

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(app)

class Details(db.Model):
    ID = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200),nullable=False)
    email = db.Column(db.String(200),nullable=False)
    subject = db.Column(db.String(200),nullable=False)
    msg = db.Column(db.String(200),nullable=False)

    def __repr__(self) -> str:
        return f"{self.s_no} - {self.title}"




@app.route("/", methods=['POST','GET'])
def index():
    if request.method == "POST":
        names = request.form['names']
        emails = request.form['emails']
        subjects = request.form['subjects']
        msgs = request.form['msgs']
        deatils = Details(name=names, email=emails,subject=subjects,msg=msgs)
        db.session.add(deatils)
        db.session.commit()  # Commit the changes once
        return render_template('thankyou.html')
    return render_template('index.html')
     
if __name__ == '__main__':
   app.run()