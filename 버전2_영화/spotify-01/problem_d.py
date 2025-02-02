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


def max_popularity(artists):
    max_pop = float('-inf')
    max_pop_artist = ''
    
    for artist in artists_dict.values():
        if 'popularity' in artist and 'name' in artist:
            if artist['popularity'] > max_pop:
                max_pop = artist['popularity']
                max_pop_artist = artist['name']

    return max_pop_artist


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    artist_json = open(current_dir / 'data' / 'artists.json', encoding='utf-8')
    artists_list = json.load(artist_json)

    print(max_popularity(artists_list))

