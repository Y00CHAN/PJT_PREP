import json
from pprint import pprint


# artist : dict
# artists, genres : list
def artist_info(artists, genres):
    genre_dict = {genre['id']: genre['name'] for genre in genres}
    
    for artist in artists:
        artist['genres_names'] = [genre_dict.get(genre_id) for genre_id in artist.get('genres_ids')]
        artist.pop('external_urls')
        artist.pop('uri')
        artist.pop('genres_ids')

    return artists


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    artist_json = open(current_dir / 'data' / 'artists.json', encoding='utf-8')
    artists_list = json.load(artist_json)

    genres_json = open(current_dir / 'data' / 'genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(artist_info(artists_list, genres_list))






