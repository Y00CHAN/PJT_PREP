import requests
from pprint import pprint
from config.spotify_config import getHeaders


def get_recently_tracks():
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()
    params = {
        'q' : 'recent classic genre music',
        'type' : 'track',
        'market' : 'KR',
        'limit' : 10,
    }
    response = requests.get(f'{URL}/search', headers=headers, params=params)
    response = response.json()
    result = response.get('tracks').get('items')

    albums = [
        {
            '발매일': artist['album']['release_date'],
            '아티스트': artist['name'],
            '앨범명': artist['album']['name']
        }
        for artist in result if 'album' in artist and 'name' in artist
    ]

    albums.sort(key=lambda x: x['발매일'], reverse=True)

    return albums[:5]


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_recently_tracks())
