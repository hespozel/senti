# encoding: utf-8
from flask import (
  Flask, render_template, request, flash, redirect, url_for, session
)
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, Users
import  time 
import requests
from requests.auth import HTTPDigestAuth
import json

senti = Flask(__name__)

# load config from the config file we created earlier
senti.config.from_object('config')

# initialize and create the database
db.init_app(senti)
db.create_all(app=senti)

@senti.route('/')
def home():
    return render_template('index.html')

@senti.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':

        # get the user details from the form
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']

        # hash the password
        password = generate_password_hash(password)

        user = Users(email=email, username=username, password=password)

        db.session.add(user)
        db.session.commit()

        flash('Thanks for signing up please login')

        return redirect(url_for('home'))

    # it's a GET request, just render the template
    return render_template('signup.html')

@senti.route('/login', methods=['GET', 'POST'])
def login():

	if request.method == 'POST':
		# we don't need to check the request type as flask will raise a bad request
		# error if a request aside from POST is made to this url

		username = request.form['username']
		password = request.form['password']

		# search the database for the User
		user = Users.query.filter_by(username=username).first()

		if user:
			password_hash = user.password
			if check_password_hash(password_hash, password):
				# The hash matches the password in the database log the user in
				session['user'] = username
				flash('Login was succesfull')
				return redirect(url_for('home'))
			else:
				# user wasn't found in the database
				flash('Username or password is incorrect please try again', 'error')
		
	# it's a GET request, just render the template
	return render_template('login.html')

@senti.route('/test', methods=['GET', 'POST'])
def test():
	if request.method == 'POST':
		question = request.form['qt']
		print (question)
		url="http://127.0.0.1:5001/?query="+question
		myResponse = requests.get(url, verify=True)
		if(myResponse.ok):

				# Loading the response data into a dict variable
				# json.loads takes in only binary or string variables so using content to fetch binary content
				# Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
				jData = json.loads(myResponse.content)
				retstr=""
				for key in jData:
				   retstr=retstr+key+":"+str(jData[key])+"\n" 
				print (retstr)
		else:
			  # If response code is not ok (200), print the resulting http error code with description
				myResponse.raise_for_status()
				retstr="Error"
				print ("error")
		return render_template('test.html', qt=question, results=retstr)
	else:
	
		return render_template('test.html', qt="How big is my gun?" ,results="Vazio")

@senti.route('/logout')
def logout():
	if 'user' in session:
		session.pop('user')
		flash('We hope to see you again!')
	return redirect(url_for('home'))



if __name__ == '__main__':
	senti.run()



