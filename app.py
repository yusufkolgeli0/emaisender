from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emails.db'

db = SQLAlchemy(app)

class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipient = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(120))
    message = db.Column(db.Text, nullable=False)
    date_sent = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/', methods=['GET', 'POST'])
def compose_email():
    if request.method == 'POST':
        recipient = request.form.get('recipient')
        subject = request.form.get('subject')
        message = request.form.get('message')

        new_email = Email(recipient=recipient, subject=subject, message=message)
        db.session.add(new_email)
        db.session.commit()

        return redirect(url_for('view_emails'))

    return render_template('compose.html')

@app.route('/view')
def view_emails():
    emails = Email.query.order_by(Email.date_sent.desc()).all()
    return render_template('view.html', emails=emails)
