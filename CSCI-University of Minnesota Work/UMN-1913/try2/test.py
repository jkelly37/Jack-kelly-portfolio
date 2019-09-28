import spotipy
import requests
import base64
import sys
from Playlist import Playlist
from spotipy.oauth2 import SpotifyClientCredentials
from User import publicUser
import spotipy.util as util
s = spotipy.Spotify()


from spotipy.oauth2 import SpotifyClientCredentials
st = "0e57bf8a5bc0404aa228a4ad5374683b:6ee1722e4bf14ae499a1ceda45c81e92"
base64.b64decode(st)


auth = requests.post("https://accounts.spotify.com/api/token", data ={"Authorization": st, "grant_type": "client_credentials"})
#print(auth)

client_credentials_manager = SpotifyClientCredentials(client_id="0e57bf8a5bc0404aa228a4ad5374683b", client_secret="6ee1722e4bf14ae499a1ceda45c81e92",)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
results = sp.search(q='artist' + "21 savage", type='artist')
#print(results.get)
playlists = sp.user_playlists('jacklaxjk')
#results = sp.search(q='artist:' + "21 savage", type='artist')
#items = results['artists']['items']
#print(items)
#print(playlists)
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
scope = 'playlist-modify-private'

token = util.prompt_for_user_token("jacklaxjk", scope, client_id= "0e57bf8a5bc0404aa228a4ad5374683b", client_secret="6ee1722e4bf14ae499a1ceda45c81e92", redirect_uri="http://localhost/")
print("i mean we got here")
if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    #sp.user_playlist_create(user= "jacklaxjk", name="name", public=False)
    print("did we?")
    #play = Playlist(spot=sp,user="jacklaxjk", playlist_id="03GhzO0WmepgkGyCuskQEG")
    jackUser = publicUser(spot=sp, userName= 'jacklaxjk')
    #print(jackUser)
    matthewUser = publicUser(spot=sp, userName = 'hlovig2')
    userlist = [jackUser,matthewUser]



    #createPlaylist
    b = sp.user_playlist_create("jacklaxjk", "testbig", public=False)
    print(b['id'])
    songIDlist = []
    #big = Playlist(spot= sp, user= "jacklaxjk")
    for users in userlist:
        for playlists in users.userPlaylists:
            for songs in playlists.tracks:
                songIDlist.append(songs.uri)
    k = 0
    j=10
    while j< len(songIDlist):
        sp.user_playlist_add_tracks(user="jacklaxjk",  playlist_id= b['uri'], tracks=songIDlist[k:j], position=None)
        k= j
        j = j+10






