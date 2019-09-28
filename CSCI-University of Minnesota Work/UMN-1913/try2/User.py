from Playlist import Playlist
class publicUser:
    def __init__(self,spot,userName):
        self.userPlaylists = []
        playlists = spot.user_playlists(user=userName)
        print("this is items")

        for playlist in enumerate(playlists['items']):
            #print(playlist[1]['uri'])
            #print(playlist)
            newPlaylist = Playlist(spot=spot, user= userName, playlist_id= playlist[1]['uri'])
            #print(newPlaylist)
            self.userPlaylists.append(newPlaylist)

    def __str__(self):
        s = ''


        for playlists in self.userPlaylists:
            s= s + playlists.__str__()
            if type(s) != str:
                print('issa problem')
        return s
