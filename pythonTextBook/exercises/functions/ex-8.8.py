def make_album(artist: str, album_name: str) -> dict:
    return {"artist": artist.title(), "album_name": album_name.title()}


while True:
    artist = input("Enter artist or 'q' to exit: ")
    if artist == "q":
        break

    name = input("Enter album name or 'q' to exit: ")
    if name == "q":
        break

    album = make_album(artist=artist, album_name=name)
    print(album)