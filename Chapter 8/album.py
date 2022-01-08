def make_album(artist_name, album_title, num_of_songs = None):
    """Builds a dictionary describing a music album"""
    album = {'Artist': artist_name.title(), 'Album': album_title.title()}
    if num_of_songs:
        album['num_of_songs'] = num_of_songs
    return album

#storing the album information correctly
album_1 = make_album('the weekend', 'starboy')
print(album_1)
album_2 = make_album('michael jackson', 'scream')
print(album_2)
album_3 = make_album('meek mill', 'expensive pain')
print(album_3)
# includes the number of songs on an album
album = make_album('the weekend', 'starboy', 18)
print(album)
