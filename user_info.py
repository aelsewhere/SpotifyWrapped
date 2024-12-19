# description: get info about the user

import spotipy
from spotipy import util
from auth import authenticate


def user_info():
  sp = authenticate()
  get_user_info(sp)

def get_user_info(sp):
  user = sp.current_user()
  display_name = user['display_name']
  followers = user['followers']['total']
  print(f"User: {display_name}")
  print(f"Followers: {followers}")

if __name__ == "__main__":
  user_info()
  