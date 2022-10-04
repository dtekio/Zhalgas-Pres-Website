import os
from flask import Flask, redirect, render_template, url_for, request
from flask_bootstrap import Bootstrap
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")


@app.route("/contact", methods=['POST'])
def contact():
    if request.method == "POST":
        message = Mail(
            from_email=os.getenv('EMAIL', None),
            to_emails=os.getenv('EMAIL', None),
            subject='New Message',
            html_content=f'Name: { request.form.get("name") } | Message: «{request.form.get("message")}»'
        )
        try:
            sg = SendGridAPIClient(os.getenv('SENDGRID_API', None))
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e.message)
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
