from flask_mail import Message, Mail
from app import app
from threading import Thread

mail = Mail(app)

# Your mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'jeemannu90@gmail.com'
app.config['MAIL_PASSWORD'] = 'cqep qxtj ijoy oaew'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def Submission_Mail(names, emails, subjects, msgs):
    # Email body for the confirmation to yourself
    confirmation_body = f"""
<html>
    <head>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                margin: 0;
                padding: 0;
                background: url('https://picsum.photos/1920/1080') no-repeat center center fixed;
                background-size: cover;
                color: white;
            }}
            .container {{
                padding: 20px;
            }}
            h1 {{
                color: #5e9ca0;
            }}
            p {{
                margin: 10px 0;
            }}
            .footer {{
                margin-top: 20px;
                font-size: 0.8em;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>New Submission from Your Portfolio Site</h1>
            <p><strong>Name:</strong> {names}</p>
            <p><strong>Email:</strong> {emails}</p>
            <p><strong>Subject:</strong> {subjects}</p>
            <p><strong>Message:</strong></p>
            <blockquote>{msgs}</blockquote>
            <div class="footer">
                <p>This is an automated message. Please do not reply directly to this email.</p>
            </div>
        </div>
    </body>
</html>
"""
    # Confirmation email to yourself
    confirmation_msg = Message('New Portfolio Submission',
                               sender='jeemannu90@gmail.com',
                               recipients=['mandeepkumarmannu123@gmail.com', 'mishramandeep@outlook.com'])
    confirmation_msg.html = confirmation_body
    Thread(target=send_async_email, args=(app, confirmation_msg)).start()

    # Thank you email to the person who filled the form
    thank_you_body = f"""
<html>
    <head>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f2f2f2;
                color: #333;
            }}
            .container {{
                width: 80%;
                margin: auto;
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            h1 {{
                color: #5e9ca0;
            }}
            p {{
                line-height: 1.6;
            }}
            .footer {{
                margin-top: 20px;
                text-align: center;
                font-size: 0.8em;
                color: #888;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Thank You for Your Submission!</h1>
            <p>Dear {names},</p>
            <p>We have received your message and appreciate you reaching out to us. One of our team members will review your submission and get back to you shortly.</p>
            <p>If you have any additional information to add, please reply to this email with the details.</p>
            <div class="footer">
                <p>This is an automated message. Please do not reply directly to this email.</p>
            </div>
        </div>
    </body>
</html>
"""
    thank_you_msg = Message('Thank You for Your Submission!',
                            sender='jeemannu90@gmail.com',
                            recipients=[emails])  # Corrected to use a list
    thank_you_msg.html = thank_you_body
    Thread(target=send_async_email, args=(app, thank_you_msg)).start()




def Submission_Mail_MIS(names, emails, subjects, msgs):
    # Email body for the confirmation to yourself
    confirmation_body = f"""
<html>
    <head>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                margin: 0;
                padding: 0;
                background: url('https://picsum.photos/1920/1080') no-repeat center center fixed;
                background-size: cover;
                color: white;
            }}
            .container {{
                padding: 20px;
            }}
            h1 {{
                color: #5e9ca0;
            }}
            p {{
                margin: 10px 0;
            }}
            .footer {{
                margin-top: 20px;
                font-size: 0.8em;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>{subjects}</h1>
            <p><strong>Name:</strong> {names}</p>
            <p><strong>Email:</strong> {emails}</p>
            <p><strong>Subject:</strong> {subjects}</p>
            <p><strong>Message:</strong></p>
            <blockquote>{msgs}</blockquote>
            <div class="footer">
                <p>This is an automated message. Please do not reply directly to this email.</p>
            </div>
        </div>
    </body>
</html>
"""
    # Confirmation email to yourself
    confirmation_msg = Message(subjects,
                               sender='jeemannu90@gmail.com',
                               recipients=['mandeepkumarmannu123@gmail.com', 'mishramandeep@outlook.com'])
    confirmation_msg.html = confirmation_body
    Thread(target=send_async_email, args=(app, confirmation_msg)).start()

    # Thank you email to the person who filled the form
    thank_you_body = f"""
<html>
    <head>
        <style>
            body {{
                font-family: 'Arial', sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f2f2f2;
                color: #333;
            }}
            .container {{
                width: 80%;
                margin: auto;
                background-color: #fff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            h1 {{
                color: #5e9ca0;
            }}
            p {{
                line-height: 1.6;
            }}
            .footer {{
                margin-top: 20px;
                text-align: center;
                font-size: 0.8em;
                color: #888;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Thank You for Your Submission!</h1>
            <p>Dear {names},</p>
            <p>We have received your message and appreciate you reaching out to us. One of our team members will review your submission and get back to you shortly.</p>
            <p>If you have any additional information to add, please reply to this email with the details.</p>
            <div class="footer">
                <p>This is an automated message. Please do not reply directly to this email.</p>
            </div>
        </div>
    </body>
</html>
"""
    thank_you_msg = Message('Thank You for Your Submission!',
                            sender='jeemannu90@gmail.com',
                            recipients=[emails])  # Corrected to use a list
    thank_you_msg.html = thank_you_body
    Thread(target=send_async_email, args=(app, thank_you_msg)).start()


