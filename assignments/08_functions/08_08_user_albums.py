""""""
def make_album(artist_name, album_title, num_songs=None):
    album = {
        'artist': artist_name,
        'title': album_title
    }

    if num_songs:
        album['num_songs'] = num_songs

    return album


while True:
    print("\nPlease enter an album's information:")
    print("(enter 'quit' at any time to stop)")

    artist = input("Artist name: ")
    if artist == 'quit':
        break

    title = input("Album title: ")
    if title == 'quit':
        break

    album_info = make_album(artist, title)
    print(album_info)
    