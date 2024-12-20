# artist info: user gives artist URI, get artist info
# for future update: user gives artist name, get artist info
# EXAMPLE USE: TAYLOR SWIFT URI: 'spotify:artist:06HL4z0CvFAxyc27GXpf02'

import spotipy
from spotipy import util
from auth import authenticate

def print_albums(albums):
  albums = get_albums(get_sp())
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

def get_sp():
  sp = authenticate()
  return sp


def prompt_user():  
  artist_uri = input("Enter the artist URI: ")
  if not artist_uri:
    artist_uri = input("Enter the artist URI: ")
  return artist_uri


if __name__ == "__main__":
  print_albums(get_albums(get_sp()))

# right now its asking for artist URI twice, need to fix that
# also need to add exception handling for invalid URI