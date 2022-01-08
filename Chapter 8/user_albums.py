def make_album(artist_name, album_title, num_of_songs = None):
    """Builds a dictionary describing a music album"""
    album = {'Artist': artist_name.title(), 'Album': album_title.title()}
    if num_of_songs:
        album['num_of_songs'] = num_of_songs
    return album

while True:
    print("\nPlease enter the artist and album name:")
    print("(enter 'q' to quit)")
    artist = input("Artist: ")
    if artist == 'q':
        break
    album = input("Album: ")
    if album == 'q':
        break
    songs = input("songs: ")
    if songs == 'q':
        break

    results = make_album(artist, album, songs)
    print(results)
    break
