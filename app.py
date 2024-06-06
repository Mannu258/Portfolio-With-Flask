# save this as app.py
from flask import Flask,render_template,request ,send_from_directory
from flask_mail import Mail, Message

from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'jeemannu90@gmail.com'
app.config['MAIL_PASSWORD'] = 'cqep qxtj ijoy oaew '
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail.init_app(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db = SQLAlchemy(app)

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])

class Details(db.Model):
    ID = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(200),nullable=False)
    email = db.Column(db.String(200),nullable=False)
    subject = db.Column(db.String(200),nullable=False)
    msg = db.Column(db.String(200),nullable=False)

    def __repr__(self) -> str:
        return f"{self.s_no} - {self.title}"
    
class Crediantials(db.Model):
    ID = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(200),nullable=False)
    password = db.Column(db.String(200),nullable=False)
    def __repr__(self) -> str:
        return f"{self.username}"



@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        names = request.form['names']
        emails = request.form['emails']
        subjects = request.form['subjects']
        msgs = request.form['msgs']

        # Prepare the email message with the form details
        email_body = f"""
<html>
    <body style="background: url('https://picsum.photos/1920/1080'); background-size: cover; color: white;">
        <h1 style="color: #5e9ca0;">New Submission from Your Portfolio Site</h1>
        <p><strong>Name:</strong> {names}</p>
        <p><strong>Email:</strong> {emails}</p>
        <p><strong>Subject:</strong> {subjects}</p>
        <p><strong>Message:</strong></p>
        <blockquote>{msgs}</blockquote>
    </body>
</html>
"""
        msg = Message('New Portfolio Submission',
              sender='jeemannu90@gmail.com',
              recipients=['mandeepkumarmannu123@gmail.com','mishramandeep@outlook.com'])
        msg.html = email_body
        mail.send(msg)
        details = Details(name=names, email=emails, subject=subjects, msg=msgs)
        db.session.add(details)
        db.session.commit()  # Commit the changes once
        return render_template('thankyou.html')
    return render_template('index.html')


@app.route("/project-showcase/<string:name>",methods=['POST','GET'])
def projects(name):
    if name == "OG":
        return render_template('Projects/OG.html')
    elif name == "DB":
        return render_template('Projects/MG.html')
    elif name == "MAC":
        return render_template('Projects/MAC.html')
    
    return "404 Not Found"



@app.route("/administrator",methods=['POST','GET'])
def Admin():
    if request.method == "POST":
        username = request.form['Username']
        password = request.form['password']
        admi = Crediantials.query.filter_by(username=username,password=password).first()
        if admi:
            details = Details.query.all()
            return render_template('Database.html',details=details)
        else:
            return render_template('login.html')

    return render_template('login.html')
    
     

if __name__ == '__main__':
   app.run(debug=True ,port=8000)