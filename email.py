import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('181cs126@gmail.com','#181CS@126')
server.sendmail('181cs126@gmail.com','niroshkumar072@gmail.com','hey there')