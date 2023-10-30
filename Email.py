import main as main
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content

def enviar_email():
    tabela = main.preencher_ativos()

    SENDGRID_API_KEY = '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'
    sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
    from_email = Email("cleonidesn@gmail.com")  # Change to your verified sender
    to_email = To("cleonidesn@gmail.com")  # Change to your recipient
    subject = "Email enviado agora."

    content = Content("text/plain", f"{tabela}")
    mail = Mail(from_email, to_email, subject, content)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()

    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
    print(response.status_code)
    print(response.headers)

enviar_email()