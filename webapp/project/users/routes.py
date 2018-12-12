#################
#### imports ####
#################

from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, current_user, login_required, logout_user

from . import users_blueprint
from project.models import User
from project import db


################
#### routes ####
################

@users_blueprint.route('/profile')
@login_required
def profile():
    return render_template('recipes/index.html')


@users_blueprint.route('/register', methods=['GET', 'POST'])
def register():
	# If the User is already logged in, don't allow them to try to register
	if current_user.is_authenticated:
		flash('Already registered!  Redirecting to your User Profile page...')
		return redirect(url_for('recipes.index'))

	if request.method == 'POST':
		femail = request.form['email']
		fpassword = request.form['password']
		
		new_user = User(femail, fpassword)
		new_user.authenticated = True
		db.session.add(new_user)
		db.session.commit()
		login_user(new_user)
		flash('Thanks for registering, {}!'.format(new_user.email))
		return redirect(url_for('recipes.index'))
	return render_template('users/register.html')


@users_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    # If the User is already logged in, don't allow them to try to log in again
	if current_user.is_authenticated:
		flash('Already logged in!  Redirecting to your User Profile page...')
		return redirect(url_for('users.index'))

	if request.method == 'POST':
		femail = request.form['email']
		fpassword = request.form['password']

		user = User.query.filter_by(email=femail).first()
		if user and user.is_correct_password(fpassword):
			user.authenticated = True
			db.session.add(user)
			db.session.commit()
			login_user(user)
			#flash('Thanks for logging in, {}!'.format(current_user.email))
			return redirect(url_for('recipes.index'))
		flash('ERROR! Incorrect login credentials.')
	return render_template('users/login.html')


@users_blueprint.route('/logout')
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    flash('Goodbye!')
    return redirect(url_for('recipes.index'))
