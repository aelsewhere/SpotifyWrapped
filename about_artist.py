# artist info: user gives artist URI, get artist info
# for future update: user gives artist name, get artist info
# EXAMPLE USE: TAYLOR SWIFT URI: 'spotify:artist:06HL4z0CvFAxyc27GXpf02'

import spotipy
from spotipy import util
from user_info import get_user

def print_albums():
  albums = get_albums(get_user())
  for album in albums:
    print(album['name'])

def get_albums(sp):
  artist_uri = prompt_user()
  results = sp.artist_albums(artist_uri, album_type='album')
  albums = results['items']
  while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])
  return albums


def prompt_user():  
  artist_uri = input("Enter the artist URI: ")
  if not artist_uri:
    artist_uri = input("Enter the artist URI: ")
  return artist_uri


if __name__ == "__main__":
  print_albums()

