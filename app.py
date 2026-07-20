from flask import Flask, request, jsonify
from flask_mail import Mail, Message
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'yassinafify626@gmail.com'
app.config['MAIL_PASSWORD'] = 'yxyrzhxhduzcavlr'  
app.config['MAIL_DEFAULT_SENDER'] = 'yassinafify626@gmail.com'

mail = Mail(app)

@app.route('/api/schedule', methods=['POST'])
def schedule_consulation():
    data = request.get_json()

    procedure_type = data.get('procedureType')
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone', 'Not provided')
    date_range = data.get('dateRange')
    concerns = data.get('concerns', 'None stated')

    if not all([procedure_type, name, email, date_range]):
        return jsonify({"error": "Missing required fields"}), 400
    
    try:
        # ----------------------------------------------------------------------
        # EMAIL 1: Send Internal Alert to Your Team
        # ----------------------------------------------------------------------
        team_msg = Message(
            subject=f"New Consultation Request: {name}",
            recipients=['yassinafify626@gmail.com']
        )
        team_msg.body = f"""
        Hello Team,

        A new consultation request has been submitted:

        - Patient Name: {name}
        - Email Address: {email}
        - Phone Number: {phone}
        - Procedure Type: {procedure_type}
        - Preferred Date Range: {date_range}

        --- Patient Concerns ---
        {concerns}
        """
        mail.send(team_msg)

        # ----------------------------------------------------------------------
        # EMAIL 2: Send Confirmation Directly to the Client
        # ----------------------------------------------------------------------
        client_msg = Message(
            subject="We've received your consultation request - Sedate Health",
            recipients=[email]  # Sends to the email the client typed into the form
        )
        client_msg.body = f"""
        Hi {name},

        Thank you for reaching out to Sedate Health. We 
        have successfully received your request for a 
        pre-anesthesia consultation.

        Here is a summary of what you submitted:
        - Procedure Type: {procedure_type}
        - Preferred Dates: {date_range}

        What happens next?
        A board-certified anesthesiologist is personally 
        reviewing your details. We will call or email you 
        within one business day to officially confirm your 
        exact 30-minute appointment time.

        If you need to make changes or have an urgent 
        scheduling conflict, 
        please reply directly to this email.

        Best regards,
        The Sedate Health Team
        """
        mail.send(client_msg)

        return jsonify({"message": "Consultation request and client confirmation sent successfully!"}), 200

    except Exception as e:
        print(f"Error sending mail: {e}")
        return jsonify({"error": "Failed to process request due to an email system error."}), 500
    
if __name__ == '__main__':
    app.run(debug=True)