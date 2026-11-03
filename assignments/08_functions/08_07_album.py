''''''
def make_album(artist_name, album_title, num_songs=None):
    """Build a dictionary describing a music album."""
    album = {
        'artist': artist_name,
        'title': album_title,
    }

    if num_songs:
        album['songs'] = num_songs

    return album


album1 = make_album('Drake', 'Take Care')
album2 = make_album('SZA', 'SOS')
album3 = make_album('Kendrick Lamar', 'DAMN.')

album4 = make_album('Beyonce', 'Lemonade', 12)

print(album1)
print(album2)
print(album3)
print(album4)