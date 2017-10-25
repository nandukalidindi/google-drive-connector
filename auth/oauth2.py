from requests_oauthlib import OAuth2Session

OAUTH2_AUTH_URL = "https://accounts.google.com/o/oauth2/auth"
OAUTH2_TOKEN_URL = "https://accounts.google.com/o/oauth2/token"

SCOPE_DICT = { "DRIVE READONLY": "https://www.googleapis.com/auth/drive.readonly" }

class OAuth2:
	def __init__(self, client_id, client_secret, redirect_uri, scope):
		self.client_id = client_id
		self.client_secret = client_secret
		self.redirect_uri = redirect_uri
		self.scope = SCOPE_DICT.get(scope)
		self.initialize_oauth2_session()

	def initialize_oauth2_session(self):
		try:
			self.oauth2_session = OAuth2Session(self.client_id, redirect_uri=self.redirect_uri, scope=self.scope)
		except:
			self.oauth2_session = None


	def get_authorization_url(self):
		try:
			auth_url, state = self.oauth2_session.authorization_url(OAUTH2_AUTH_URL)
		except:
			auth_url = None

		return auth_url

	def fetch_access_token(self, auth_code):
		try:
			token_obj = self.oauth2_session.fetch_token(token_url=OAUTH2_TOKEN_URL, code=auth_code, client_secret=self.client_secret)
			access_token = token_obj.get('access_token')
		except:
			access_token = None

		return access_token

	@staticmethod
	def get_active_session(self):
		if self.oauth2_session:
			return self.oauth2_session
		else:
			self.initialize_oauth2_session()
			return self.oauth2_session




