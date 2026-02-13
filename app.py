from flask import Flask, render_template, request
import os
import zipfile
import smtplib
from email.message import EmailMessage
from subprocess import call

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <form method="POST" action="/mashup">
        Singer Name: <input name="singer"><br>
        Number of Videos: <input name="videos"><br>
        Duration (sec): <input name="duration"><br>
        Email: <input name="email"><br>
        <input type="submit">
    </form>
    '''

@app.route('/mashup', methods=['POST'])
def mashup():
    singer = request.form['singer']
    videos = request.form['videos']
    duration = request.form['duration']
    email = request.form['email']

    output_file = "result.mp3"

    # Call Program 1
    call(["python", "102303141.py", singer, videos, duration, output_file])

    # Zip file
    zip_name = "mashup.zip"
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        zipf.write(output_file)

    send_email(email, zip_name)

    return "Mashup sent to your email!"

def send_email(to_email, filename):
    msg = EmailMessage()
    msg['Subject'] = "Your Mashup File"
    msg['From'] = "dmalik_be23@thapar.com"
    msg['To'] = to_email

    msg.set_content("Attached is your mashup file.")

    with open(filename, 'rb') as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype='application',
                           subtype='zip', filename=filename)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login("dmalik_be23@thapar.edu", "fkjollarkrxhvabu")
        smtp.send_message(msg)

if __name__ == '__main__':
    app.run(debug=True)
