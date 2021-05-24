import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


class SubmitEmail:

    def submit(self, order_data:dict):
        user = 'livroparatodxs@outlook.com'
        password = 'zFD9L2Y@bRt5'

        try:
            server = smtplib.SMTP('smtp.outlook.com', 587)
            server.starttls()
            server.login(user, password)

            email_msg = MIMEMultipart()
            email_msg['From'] = user
            email_msg['To'] = order_data["email_client"]
            email_msg['Subject'] = order_data["email_title"]

            filename = order_data["type"]
            filepath = order_data["file_path"]
            attachment = open(filepath, 'rb')

            att = MIMEBase('application', 'octet-stream')
            att.set_payload(attachment.read())
            encoders.encode_base64(att)
            att.add_header('Content-Disposition', f'attachment; filename= {filename}')

            attachment.close()
            email_msg.attach(att)

            server.sendmail(email_msg['From'], email_msg['To'], email_msg.as_string())
            server.quit()

            return True

        except Exception as Erro:
            return dict(status=False, message=Erro.args)