
def send_email(sender, password, receiver, smtp_server, smtp_port, email_message, subject, attachment=None):
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.header import Header
    from email.mime.application import MIMEApplication

    message = MIMEMultipart()
    message['To'] = Header(receiver)
    message['From']  = Header(sender)
    message['Subject'] = Header(subject)
    message.attach(MIMEText(email_message,'plain', 'utf-8'))
    if attachment:
        att = MIMEApplication(attachment.read(), _subtype="txt")
        att.add_header('Content-Disposition', 'attachment', filename=attachment.name)
        message.attach(att)

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.ehlo()
    server.login(sender, password)
    text = message.as_string()
    server.sendmail(sender, receiver, text)
    server.quit()

def nav_to(url):
    import streamlit as st
    
    nav_script = """
        <meta http-equiv="refresh" content="0; url='%s'">
    """ % (url)
    
    st.write(nav_script, unsafe_allow_html=True)