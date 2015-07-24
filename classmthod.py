__author__ = 'cgiridhar'
class Song(object):
        def __init__(self,title):
                self.title = title

        def __str__(self):
                return ('"Title is:"%(title)' %self.__dict__)

        @classmethod
        def create_songs(cls, songlist):
                for title in songlist:
                        yield cls(title)


songlist = ["S1", "S2"]
for song in Song.create_songs(songlist):
        print(song)