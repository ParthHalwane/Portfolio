from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = 'ab45xy45@gmail.com'  
app.config['MAIL_PASSWORD'] = 'vher bdzv city fcuj'  
app.config['MAIL_DEFAULT_SENDER'] = 'ab45xy45@gmail.com'  

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
