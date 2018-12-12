# encoding: utf-8
#################
#### imports ####
#################

from flask import render_template

from . import recipes_blueprint
from flask import render_template, request, flash, redirect, url_for
import requests
from flask_login import login_user, current_user, login_required, logout_user
import json

################
#### routes ####
################

@recipes_blueprint.route('/')
def index():
    return render_template('recipes/index.html')

@recipes_blueprint.route('/test', methods=['GET', 'POST'])
def test():

    # If the User is already logged in, don't allow them to try to log in again
	if (current_user.is_authenticated)==False:
		flash('Por Favor -  Login')
		return redirect(url_for('users.index'))

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
		return render_template('recipes/test.html', qt=question, results=retstr)
	else:
	
		return render_template('recipes/test.html', qt="How big is my gun?" ,results="Vazio")
