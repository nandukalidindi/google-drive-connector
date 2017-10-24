REDIRECT_URI = "http://localhost:5000/google_oauth2/callback"

access_token = ""

import pdb
from credentials import client_id, client_secret
from flask import Flask, render_template, request, redirect
from requests_oauthlib import OAuth2Session


scope = ['https://www.googleapis.com/auth/drive.readonly']
oauth = OAuth2Session(client_id, redirect_uri=REDIRECT_URI, scope=scope)

app = Flask(__name__)

@app.route('/')
def connect():
    return render_template('connector.html', auth_url=authorization_url())

@app.route('/google_oauth2/callback')
def oauth2_callback():
	authorization_code = request.values['code']
	token = oauth.fetch_token(token_url="https://accounts.google.com/o/oauth2/token", code=authorization_code, client_secret=client_secret)
	access_token = token.get('access_token')	
	return redirect("http://localhost:5000/", code=302)


def authorization_url():	
	authorization_url, state = oauth.authorization_url('https://accounts.google.com/o/oauth2/auth')
	return authorization_url
