from credentials import client_id, client_secret, redirect_uri
from flask import Flask, render_template, request, redirect, session
from auth.oauth2 import OAuth2

oauth2_session = OAuth2(client_id, client_secret, redirect_uri, "DRIVE READONLY")

app = Flask(__name__)
app.secret_key = 'super secret key'

@app.route('/')
def connect():
	return render_template('connector.html', auth_url=oauth2_session.get_authorization_url())    

@app.route('/google_oauth2/callback')
def oauth2_callback():
	auth_code = request.values['code']

	access_token = oauth2_session.fetch_access_token(auth_code)
	return redirect("http://localhost:5000/", code=302)
