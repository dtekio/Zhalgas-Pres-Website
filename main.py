import os
from flask import Flask, redirect, render_template, url_for, request
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    team = [{'name':'Айдана','photo':'aidana','inst':'berkimbayyeva','grade':'10G'},
            {'name':'Рамадан','photo':'ramadan','inst':'ramadan_marat','grade':'10B'},
            {'name':'Томирис','photo':'tomiris','inst':'tomiriskassym','grade':'10G'}]
    return render_template("index.html", team=team)


@app.route("/contact", methods=['POST'])
def contact():
    if request.method == "POST":
        message = Mail(
            from_email=os.getenv('EMAIL', None),
            to_emails=os.getenv('EMAIL', None),
            subject='New Message',
            html_content=f'Name: { request.form.get("name") } | Message: «{request.form.get("message")}»'
        )
        sg = SendGridAPIClient(os.getenv('SENDGRID_API', None))
        sg.send(message)
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run()
