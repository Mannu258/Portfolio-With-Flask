from app import app, db, Crediantials
with app.app_context():
    me = Crediantials(username="Admin", password="root")
    db.session.add(me)
    db.session.commit()
    print("The new credentials have been added to the database.")
