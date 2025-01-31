import json
from pathlib import Path

current_dir = Path(__file__).resolve().parent
artists_dir = current_dir / 'data' / 'artists'
print(artists_dir)
json_files = list(artists_dir.glob('*.json'))

artists_dict = {}

for artist in json_files:
    with open(artist, encoding='utf-8') as file:
        artists_dict[artist.name] = json.load(file)

# a= (','.join(map(str, artists_dict.values())))
print(artists_dict)


# def max_popularity(artists):
#     global artists_dict
#     pop_list = []
#     for artist in artists_dict:
#         pop_list.append(artists_dict['popularity'])
#         return pop_list

# max_popularity(artist)

# # 아래의 코드는 수정하지 않습니다.
# if __name__ == '__main__':
#     from pathlib import Path

#     current_dir = Path(__file__).resolve().parent

#     artist_json = open(current_dir / 'data' / 'artists.json', encoding='utf-8')
#     artists_list = json.load(artist_json)

#     print(max_popularity(artists_list))

# a = [3, 434, 132, 4]
# print(max(a))