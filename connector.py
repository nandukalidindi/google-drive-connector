from credentials import client_id, client_secret, redirect_uri
from flask import Flask, render_template, request, redirect, session, jsonify
from auth.oauth2 import OAuth2
import pdb

oauth2 = OAuth2(client_id, client_secret, redirect_uri, "DRIVE_READONLY")

app = Flask(__name__)
app.debug = True
app.secret_key = 'super secret key'

@app.route('/')
def connect():
	return render_template('connector.html', auth_url=oauth2.get_authorization_url())    

@app.route('/google_oauth2/callback')
def oauth2_callback():
	auth_code = request.values['code']

	access_token = oauth2.fetch_access_token(auth_code)
	session['access_token'] = access_token
	return redirect("http://localhost:5000/", code=302)

@app.route('/driveV3/<drive_endpoint>')
def get_drive_response(drive_endpoint="about?fields=*"):
	if session.get('access_token') == None:
		return

	query_parameters = ",".join([str(k) + "=" + str(v) for k, v in request.args.items()])
	return jsonify(oauth2.session.get("https://www.googleapis.com/drive/v3/" + drive_endpoint + "?" + query_parameters).json())