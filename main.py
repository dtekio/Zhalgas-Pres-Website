import os
from flask import Flask, abort, flash, redirect, render_template, url_for, request
from flask_bootstrap import Bootstrap
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    email = StringField("E-Mail", validators=[DataRequired(), Email()])
    phone_number = StringField("Phone Number", validators=[DataRequired()])
    message = StringField("Message", validators=[DataRequired()])
    submit = SubmitField("Send")


app = Flask(__name__)
app.secret_key = '3'
# app.secret_key = os.getenv('FLASK_SECRET', None)
Bootstrap(app)


@app.route('/', methods=['GET','POST'])
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=['POST'])
def contact():
    if request.method == "POST":
        message = Mail(
            from_email='tairko2007@gmail.com',
            to_emails='tairko2007@gmail.com',
            subject='New Message',
            html_content=f'Name: { request.form.get("name") } | Message: «{request.form.get("message")}»'
        )
        try:
            sg = SendGridAPIClient(
                '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')
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run(debug=True)
