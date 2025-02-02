"""
    팔로워가 5,000,000 이상, 10,000,000 미만인 아티스트의 이름과 팔로워를 목록으로 출력하기
"""

import json
from pprint import pprint
from pathlib import Path

current_dir = Path(__file__).resolve().parent
# current_dir = Path(__file__).resolve().parent
# artists_dir = current_dir / 'data' / 'artists'
# print(artists_dir)
# json_files = list(artists_dir.glob('*.json'))

# artists_dict = {}

# for artist in json_files:
#     with open(artist, encoding='utf-8') as file:
#         artists_dict[artist.name] = json.load(file)

def get_popular():
    current_dir = Path(__file__).resolve().parent
    artists_dir = current_dir / 'data' / 'artists'
    print(artists_dir)
    json_files = list(artists_dir.glob('*.json'))

    artists_dict = {}

    for artist in json_files:
        with open(artist, encoding='utf-8') as file:
            artists_dict[artist.name] = json.load(file)

    pop_artists_list = []

    for artist in artists_dict.values():
        if 'followers' in artist and 'name' in artist:
            if 5000000 <= artist['followers']['total'] <= 10000000:
                pop_artists_dict = {
                    'name' : artist['name'],
                    'followers' : artist['followers']['total']
                }

                pop_artists_list.append(pop_artists_dict)

    return pop_artists_list 


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(get_popular())
