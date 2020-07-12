class Painting:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year
        self.info = f'"{self.title}" by {self.artist} ({self.year}) hangs in the Louvre.'


title = input()
artist = input()
year = input()

painting = Painting(title, artist, year)

print(painting.info)
