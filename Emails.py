from app import mail, Message, app

with app.app_context():

    def Submission_Mail(names, emails, subjects, msgs):
        try:
            # Notify yourself (portfolio owner)
            msg = Message(
                subject="New Portfolio Submission",
                sender="jeemannu90@gmail.com",
                recipients=[
                    "mandeepkumarmannu123@gmail.com",
                    "mishramandeep@outlook.com",
                ],
            )
            msg.body = f"""
                Hello Mandeep,

                You have a new submission from your portfolio site:
                Name: {names}
                Email: {emails}
                Subject: {subjects}
                Message:
                {msgs}

                Best regards,
                Your Portfolio Team
            """
            mail.send(msg)

            # Auto-reply to the form filler
            autoreply = Message(
                subject="Thank You for Your Submission",
                sender="jeemannu90@gmail.com",
                recipients=[emails],
            )
            autoreply.body = f"""
                Hello {names},

                We have received your message and appreciate you reaching out to us. One of our team members will review your submission and get back to you shortly.

                This is an automated message. Please do not reply directly to this email.

                Best regards,
                Mandeep Mishra
                9386090900
            """
            mail.send(autoreply)

            return "Emails sent successfully"
        except Exception as e:
            return str(e)
