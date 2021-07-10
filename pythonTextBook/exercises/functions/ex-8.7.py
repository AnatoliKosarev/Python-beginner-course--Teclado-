def make_album(artist: str, album_name: str, recording_tech: int = None) -> dict:
    if recording_tech:
        return {"artist": artist.title(), "album_name": album_name.title(), "rec_tech": recording_tech}
    else:
        return {"artist": artist.title(), "album_name": album_name.title()}


print(make_album("the beatles", "revolver"))
print(make_album(recording_tech=2, album_name="Master of puppets", artist="metallica"))