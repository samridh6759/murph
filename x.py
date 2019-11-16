print('LOADING LIBRARIES')
import wolframalpha
import wikipedia
from gtts import gTTS
import speech_recognition as sr
import playsound
import os
from requests import get
from requests.exceptions import RequestException
from contextlib import closing 
from splinter import Browser
import time
import random
from datetime import datetime
import sys
import numpy as np
import numpy as np 
from warnings import simplefilter
import smtplib,ssl
import pickle
import requests
os.system('cls')
print('                                  MURPH                                                  ')
print('                                                                                                              ')
print('                               A.I ASSISTANT                                                        ')
state=1
app_id='6WPAP6-L4WVRG22XG'
client = wolframalpha.Client(app_id)
q=2
def speak(x):
	tex=gTTS(x,lang='en-in')
	tex.save('run'+str(q)+'.mp3')
	playsound.playsound('run'+str(q)+'.mp3', True)
	os.remove('run'+str(q)+'.mp3')
def spell(x):
	global q
	for i in x :
		if i=='.':
			speak('dot')

			q=q+1
			print(i)
		else:
			speak(i)
			q=q+1
			print(i)
def email(x):
	global q
	port = 587  
	smtp_server = "smtp.gmail.com"
	sender_email = "murph.intelligence01@gmail.com"
	speak('Whom shall i send this email to \n')
	q=q+1
	receiver_email = str(input('Whom shall i send this email to ?\n'))
	speak('Shall i spell the email')
	q=q+1
	id_check=str(input('Shall i spell the email (y/n) \n'))
	if id_check=='y':
		spell(receiver_email)
	password = 'binary0101'
	message = x
	context = ssl.create_default_context()
	with smtplib.SMTP(smtp_server, port) as server:
		server.ehlo()  # Can be omitted
		server.starttls(context=context)
		server.ehlo()  # Can be omitted
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message)
	speak('Email has been sent')
	q=q+1
	print('Email has been sent')
speak('Hello sir what can i do for you')
q=q+1
print('Hello sir what can i do for you')
def listen():
	r = sr.Recognizer()
	with sr.Microphone() as source:    
		try:            
			audio = r.record(source,duration=5)
			output=r.recognize_google(audio)
			if type(output)=='None':
				listen()
			else:
				return(output)
		except:
			listen()
work_list={}
while state==1:
	arg=str(input())
	if arg=='sleep':
		state=0
	elif arg=='clean':
		os.system('cls')
		god_save_humanity()
	elif arg=='help':
		a=open('help.txt','r')
		b=a.readlines()
		for i in b:
			print(i)
	elif arg=='hi' or arg=='hello':
		speak('Hello')
		q=q+1
		print('Hi')
	elif 'sleep' in arg  and 'for' in arg and 'minutes' in arg or 'minute' in arg :
		sleep=arg.split(' ')
		time.sleep(int(sleep[-2]*60))
		speak('Awake')
		q=q+1
		print('Awake !!')
	elif 'sleep' in arg  and 'for' in arg and 'seconds' in arg or 'second' in arg:
		sleep=arg.split(' ')
		time.sleep(int(sleep[-2]))
		speak('Awake')
		q=q+1
		print('Awake !!')
	elif 'what' in arg and 'your' in arg or 'name' in arg or 'who' in arg and 'you' in arg or 'you' in arg :
		speak('I am Murph , i was born on 1st of june 2019 and My creator is Samridh')
		q=q+1
		print('I am Murph , i was born on 1st of june 2019 and My creator is Samridh')
	if 'search' in arg and 'wikipedia' not in arg or 'calculate' in arg or 'find' in arg and 'connection' not in arg and 'map' not in arg:
		if 'calculate' in arg:
			speak('Expression to calculate')
			q=q+1
			print('Expression to calculate')
			search_query=input('')
			try :
				res = client.query(search_query)
				answer = next(res.results).text 
				speak(answer)
				print(answer)
				q=q+1
				work_list[search_query]=str(answer)
			except:
				speak('Sir i cant find any resource able to answer your question please elaborate your question ')
				q=q+1
				print('Sir i cant find any resource able to answer your question please elaborate your question ')
		else:
			speak('What shall i search')
			q=q+1
			print('What shall i search ?')
			search_query=input('')
			try :
				res = client.query(search_query)
				answer = next(res.results).text 
				speak(answer)
				print(answer)
				q=q+1
				work_list[search_query]=str(answer)
			except:
				speak('Sir i cant find any resource able to answer your question please elaborate your question ')
				q=q+1
				print('Sir i cant find any resource able to answer your question please elaborate your question ')
	elif 'brief' in arg or 'explain' in arg or 'search' and 'wikipedia' in arg:
		try:
			speak('what shall i search on wikipedia ')
			q=q+1
			print('what shall i search on wikipedia ')
			user_query=input('')
			result=wikipedia.summary(user_query)
			speak(result)
			q=q+1
			work_list[user_query]=str(result)
		except:
			print('I am unable to understand the wikipedia page you are referring to please elaborate')
	elif 'wake' in arg and 'me' in arg and 'up' in arg or 'alarm' in arg and 'set' in arg or 'alarm' in arg:
		speak('At what time will you like to wake up.\nPlease tell the time only')
		q=q+1
		print('At what time will you like to be alarmed.\nPlease tell the time only')
		alarm_time=input('')
		w_l=alarm_time.split(' ')
		month=time.localtime().tm_mon
		year=time.localtime().tm_year
		current_date=time.localtime().tm_mday
		time_wake=int(w_l[0])
		spinner = spinning_cursor()
		speak('Alarm Set all functions have been disabled')
		q=q+1
		print('Alarm Set all functions have been disabled')
		while time.localtime().tm_hour!=time_wake:
			wake_st=listen()
			if wake_st=='wakeup':
				time_wake=time.localtime().tm_hour
		else:
			print('Alarm off all functions enabled')
			speak('Alarm off all functions enabled')
			q=q+1
	elif 'email' in arg and 'this' not in arg:
		speak('What shall i email a text or data from internet')
		q=q+1
		i=str(input('What shall i email a text or data from internet \n'))
		if i.lower()=='text':
			port = 587  # For starttls
			smtp_server = "smtp.gmail.com"
			sender_email = "murph.intelligence01@gmail.com"
			speak('Whom shall i send this email to ')
			q=q+1
			receiver_email = str(input('Whom shall i send this email to ?\n'))
			id_check=str(input('Shall i spell the email (y/n)\n'))
			if id_check=='y':
				spell(receiver_email)
			speak('Please tell the text')
			q=q+1
			mail_data=str(input('text\n'))
			password = 'binary0101'
			message = mail_data
			context = ssl.create_default_context()
			with smtplib.SMTP(smtp_server, port) as server:
				server.ehlo()
				server.starttls(context=context)
				server.ehlo() 
				server.login(sender_email, password)
				server.sendmail(sender_email, receiver_email, message)
			speak('Email has been sent')
			q=q+1
			print('Email has been sent')
		elif i.lower()=='data':
			port = 587  
			smtp_server = "smtp.gmail.com"
			sender_email = "murph.intelligence01@gmail.com"
			speak('Whom shall i send this email to \n')
			q=q+1
			receiver_email = str(input('Whom shall i send this email to ?\n'))
			speak('Shall i spell the email')
			q=q+1
			id_check=str(input('Shall i spell the email (y/n) \n'))
			if id_check=='y':
				spell(receiver_email)
			speak('Please tell the data to search for')
			q=q+1
			user_query=str(input('Please tell the data to search for\n'))
			try:
				sub=str('Subject :{}\n'.format(user_query))
				mail_data=(sub+str(wikipedia.summary(user_query))).encode('utf-8')
			except:
				speak('I am unable to find anything please specify')
				q=q+1
				print('I am unable to find anything please specify')
			password = 'binary0101'
			message = mail_data
			context = ssl.create_default_context()
			with smtplib.SMTP(smtp_server, port) as server:
				server.ehlo()  # Can be omitted
				server.starttls(context=context)
				server.ehlo()  # Can be omitted
				server.login(sender_email, password)
				server.sendmail(sender_email, receiver_email, message)
			speak('Email has been sent')
			q=q+1
			print('Email has been sent')
	elif 'email' in arg and 'this' in arg:
		p=list(work_list.keys())
		sub=str('Subject :{}\n'.format(p[-1]))
		mail_data=(sub+str(work_list[p[-1]])).encode('utf-8')
		email(mail_data)
	
