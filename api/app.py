from flask import Flask, render_template, request
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

mail = Mail(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    if request.method == 'POST':
        recipient_email = 'parthhalwane@gmail.com' 
        subjects=request.form['subject'] 
        sender_name = request.form['name']
        sender_email = request.form['email']
        message_body = request.form['message']

        message = Message(subject=f'{sender_name}',
                          recipients=[recipient_email],
                          body=f"Sender: {sender_name}\nEmail: {sender_email}\nSubject: {subjects}\n\n{message_body}")

        mail.send(message)
        return render_template('index.html', message = 'Please enter the correct password',message_sent='success')

if __name__ == '__main__':
    app.run(debug=True)
