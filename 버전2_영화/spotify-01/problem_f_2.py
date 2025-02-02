"""
    장르에 acoustic이 포함된 아티스트 이름 목록 출력하기
"""

import json
from pprint import pprint
from pathlib import Path

current_dir = Path(__file__).resolve().parent


def acoustic_artists():
    current_dir = Path(__file__).resolve().parent
    artists_dir = current_dir / 'data' / 'artists'
    print(artists_dir)
    json_files = list(artists_dir.glob('*.json'))

    artists_dict = {}

    for artist in json_files:
        with open(artist, encoding='utf-8') as file:
            artists_dict[artist.name] = json.load(file)

    acoustic_artists_list = []

    for artist in artists_dict.values():
        if 'genres_ids' in artist and 'name' in artist:
            if 339 in artist['genres_ids']:
                acoustic_artists_list.append(artist['name'])

    return acoustic_artists_list 


'''
=============================================================================
아래는 GPT의 도움
339라는 'acoustic' 번호를 직접 안쓰고
genres.json에서 정보를 가져와서 출력
=============================================================================
'''


# import json
# from pathlib import Path

# def acoustic_artists():
#     current_dir = Path(__file__).resolve().parent
#     artists_dir = current_dir / 'data' / 'artists'
#     genres_file = current_dir / 'data' / 'genres.json'  # genres.json 경로 추가

#     # artists 데이터 불러오기
#     json_files = list(artists_dir.glob('*.json'))
#     artists_dict = {}

#     for artist in json_files:
#         with open(artist, encoding='utf-8') as file:
#             artists_dict[artist.name] = json.load(file)

#     # genres 데이터 불러오기
#     with open(genres_file, encoding='utf-8') as file:
#         genres_data = json.load(file)

#     # 'acoustic' 장르의 ID 찾기
#     acoustic_genre_id = None
#     for genre in genres_data:
#         if genre.get('name') == 'acoustic':
#             acoustic_genre_id = genre.get('id')
#             break

#     # 'acoustic' 장르가 존재하는 경우에만 필터링 수행
#     acoustic_artists_list = []
#     if acoustic_genre_id is not None:
#         for artist in artists_dict.values():
#             if 'genres_ids' in artist and 'name' in artist:
#                 if acoustic_genre_id in artist['genres_ids']:
#                     acoustic_artists_list.append(artist['name'])

#     return acoustic_artists_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    pprint(acoustic_artists())
