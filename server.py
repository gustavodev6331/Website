import flask
from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()
my_email = os.environ.get("MY_EMAIL")
my_password = os.environ.get("MY_PASSWORD")

app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/contact', methods=["POST"])
def contact():
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        email_msg = f"""Subject: New portfolio message!
Reply-To: {email}
        
Name: {name}
Email: {email}

Message: 
{message}
"""
        server.starttls()
        server.login(my_email, my_password)
        server.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=email_msg
        )
        flask.flash("Thank you for your message, I'll reply as soon as possible!")
        return redirect(url_for('home') + '#contact')

if __name__ == '__main__':
    app.run(debug=True)
