import spotipy
from spotipy import util

from user_info import get_user, get_user_playlists



def print_playlists():
  playlists = get_user_playlists(get_user(), 10)


if __name__ == "__main__":
  print_playlists()