# requirement: secret.py containning CLIENT_ID, CLIENT_SECRET, REDIRECT_URI
# description: authenticate user & get access token

import spotipy
from spotipy import util
from spotipy.oauth2 import SpotifyOAuth
from secret import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, SCOPE


def authenticate():
  token = util.prompt_for_user_token('user', SCOPE, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI)
  if token:
    return spotipy.Spotify(auth=token)
  else:
    print("Can't get token for", 'user')
    return None
    
if __name__ == '__main__':
  sp = authenticate()
  if sp:
    print("Successfully authenticated")
  else:
    print("Failed to authenticate")


