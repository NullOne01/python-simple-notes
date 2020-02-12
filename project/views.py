from flask import Flask, redirect, url_for, make_response, session, request, render_template, flash
import os
from .wizard_world import *
from . import app

@app.route('/')
def index():
	if 'username' in session:
		notes = get_note_list(session['username'])
		return render_template('notes.html', notes=notes, name=session['username'])
	return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		if username and password and authenticate(username, password):
			session['username'] = username
			return redirect(url_for('index'))
	return render_template('login.html')

@app.route('/register', methods=['POST', 'GET'])
def register_user():
	if request.method == "POST":
		username = request.form['username']
		password = request.form['password']
		email = request.form['email']
		if username and password and email and register(username, password, email):
			session['username'] = username
			return redirect(url_for('index'))
		else:
			flash(u'User exists. Check your login and email')
	return render_template("register.html")