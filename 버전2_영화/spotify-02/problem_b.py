import requests
from pprint import pprint
from config.spotify_config import getHeaders


def get_popular_artists():
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()
    params = {
        'q' : 'KPOP HITS 2024-2025',
        'type' : 'artist',
        'market' : 'KR',
        'limit' : 20,
    }
    response = requests.get(f'{URL}/search', headers=headers, params=params)
    response = response.json()
    result = response.get('artists').get('items')
    # names = [artist['name'] for artist in result if 'name' in artist]
    pop_artists_lsit = [artist['name'] for artist in result if 'name' in artist if artist['popularity'] >= 70]

    return pop_artists_lsit #24-25 인기도 80이상은 내가 뽑아낸 아티스트에 없어서 70점 이상으로..


# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_popular_artists())
