# Создайте класс Playlist с атрибутом songs (список), создайте метод add(), чтобы
# добавить песню в playlist.

class Playlist:

    def __init__(self, songs = None):
        self.songs= songs if songs is not None else []

    def add(self, song):
        self.songs.append(song)

    def __repr__(self):
        return f"Плейлист: {' , '.join(self.songs)}"



play = Playlist(["Lalalaa"])
print(play)
play.add("Mimimii")
print(play)