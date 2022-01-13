import random
class Playlist:
    def __init__(self,k):
        self.songs = ['A','B','C','D']
        self.karray = []
        self.k = k

    def output_song(self):
        song = random.choice(self.songs)
        print("From " + str(self.songs) + "        Played " + str(song))
        self.songs.remove(song)
        self.karray.append(song)
        if len(self.karray) >= self.k:
            self.songs.append(self.karray.pop(0))

play = Playlist(2)
for i in range(7):
    play.output_song()
