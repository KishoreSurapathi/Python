import random
class Playlist:
    def __init__(self,k):
        self.songs = ['A','B','C','D']
        self.karray = []
        self.k = k

    def output_song(self):
        song = random.choice(self.songs)
        print("From " + str(self.songs) + "        Played " + str(song))
        if len(self.karray) >= self.k:
            self.songs.remove(song)
            self.karray.append(song)
            self.songs.append(self.karray.pop(0))
        else:
            self.songs.remove(song)
            self.karray.append(song)

play = Playlist(2)
for i in range(6):
    play.output_song()
