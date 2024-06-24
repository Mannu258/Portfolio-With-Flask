from flask_mail import Message,Mail
from app import app


mail = Mail(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'jeemannu90@gmail.com'
app.config['MAIL_PASSWORD'] = 'cqep qxtj ijoy oaew '
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail.init_app(app)
def Submission_Mail(names, emails, subjects, msgs):
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
                  recipients=['mandeepkumarmannu123@gmail.com', 'mishramandeep@outlook.com'])
    msg.html = email_body
    mail.send(msg)

def Submission_Mail_MIS(names, emails, subjects, msgs):
    email_body = f"""
<html>
    <body style="background: url('https://picsum.photos/1920/1080'); background-size: cover; color: white;">
        <h1 style="color: #5e9ca0;">{subjects}</h1>
        <p><strong>Name:</strong> {names}</p>
        <p><strong>Email:</strong> {emails}</p>
        <p><strong>Subject:</strong> {subjects}</p>
        <p><strong>Message:</strong></p>
        <blockquote>{msgs}</blockquote>
    </body>
</html>
"""
    msg = Message(subjects,
                  sender='jeemannu90@gmail.com',
                  recipients=['mandeepkumarmannu123@gmail.com', 'mishramandeep@outlook.com'])
    msg.html = email_body
    mail.send(msg)
