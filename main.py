from email.message import EmailMessage
import smtplib


remitente = "iotquindio@gmail.com"
destinatario = "camilogonzalezf8@gmail.com"

mensaje = "Felicitaciones, si puede leer esto quiere decir que funcionó"

email = EmailMessage()
email["From"] = remitente
email["To"] = destinatario
email["Subject"] = "Mensaje de prueba Raspberry Pi3" 
email.set_content(mensaje)
smtp = smtplib.SMTP_SSL("smtp.gmail.com")
smtp.login(remitente, "pjbrzaijismmntpf")
smtp.sendmail(remitente, destinatario, email.as_string())
smtp.quit()