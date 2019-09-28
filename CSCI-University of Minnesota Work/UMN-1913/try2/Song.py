class Song:
    def __init__(self, name, artist, album, uri, id):
        self.name = name
        self.uri = uri
        self.id = id
        self.artist = artist
        self.album = album



    def getName(self):
        return self.name
    def getUri(self):
        return self.uri
    def getArtist(self):
        return self.artist
    def getAlbum(self):
        return self.album

    def __str__(self):
        s = ("(Song object) name: " + self.getName() + " Artist: " +self.getArtist()).encode('utf-8')
        if type(s) != str:
            print("its not tho")
            print(s)
        return ("(Song object) name: " + self.getName() + " Artist: " +self.getArtist()).encode('utf-8')



