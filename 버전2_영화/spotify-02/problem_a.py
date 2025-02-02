import requests
from pprint import pprint
from config.spotify_config import getHeaders, API_CLIENT_ID, API_CLIENT_SECRET



def get_artists():
    # 여기에 코드를 작성합니다.
    URL = 'https://api.spotify.com/v1'
    headers = getHeaders()
    params = {
        'q' : 'BEST KPOP 2025-TOP HITS',
        'type' : 'artist',
        'market' : 'KR',
        'limit' : 20,
    }
    response = requests.get(f'{URL}/search', headers=headers, params=params)
    response = response.json()
    result = response.get('artists').get('items')
    names = [artist['name'] for artist in result if 'name' in artist]

    return names

# 아래 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_artists())
