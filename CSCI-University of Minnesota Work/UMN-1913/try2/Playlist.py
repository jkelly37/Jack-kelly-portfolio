from Song import Song
class Playlist:
    def __init__(self,spot = None, user ='jacklaxjk', playlist_id = None ):
        self.tracks = []
        self.playlist_id = ''
        self.trackCount = 0
        g = spot.user_playlist(user=user, playlist_id=playlist_id)
        self.name = g['name']
        t = spot.user_playlist_tracks(user=user, playlist_id=playlist_id)
        for tracks in enumerate(t["items"]):
            tr = tracks[1]
            tr = tr['track']
            song = Song(name=tr['name'],uri=tr['uri'], album=tr['album']['name'], artist= tr['artists'][0]['name'],id= tr['id'] )
            self.tracks.append(song)

    def __str__(self):
        s = 'THIS IS PLAYLIST'
        for songs in self.tracks:
            s = s + songs.__str__() + '\n'
        return s


