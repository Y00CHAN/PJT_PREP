import requests
from pprint import pprint
from config.spotify_config import getHeaders


def get_artists_top_tracks(name):
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()
    params = {
        'q' : 'k-pop',
        'type' : 'artist',
        'market' : 'KR',
        'limit' : 20,
    }
    response = requests.get(f'{URL}/search', headers=headers, params=params)
    response = response.json()
    result = response.get('artists').get('items')
    names = [artist['name'] for artist in result if 'name' in artist]
    # pop_artists_lsit = [artist['name'] for artist in result if 'name' in artist if artist['popularity'] >= 80]

    return names 



# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_artists_top_tracks('BTS'))
    pprint(get_artists_top_tracks('OldShirts'))
