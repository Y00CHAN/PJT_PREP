import json
from pathlib import Path
from pprint import pprint


current_dir = Path(__file__).resolve().parent
artists_dir = current_dir / 'data' / 'artists'
print(artists_dir)
json_files = list(artists_dir.glob('*.json'))

artists_dict = {}

for artist in json_files:
    with open(artist, encoding='utf-8') as file:
        artists_dict[artist.name] = json.load(file)



def dec_artists(artists):
    dec_artists_list = []

    for artist in artists_dict.values():
        if 'followers' in artist and 'name' in artist and 'uri' in artist:
            if artist['followers']['total'] >= 10000000:
                dec_artists_dict = {
                    'name' : artist['name'],
                    'uri' : artist['uri'].split(':')[2]
                }

                dec_artists_list.append(dec_artists_dict)

    return dec_artists_list


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    from pathlib import Path

    current_dir = Path(__file__).resolve().parent

    artist_json = open(current_dir / 'data' / 'artists.json', encoding='utf-8')
    artists_list = json.load(artist_json)

    pprint(dec_artists(artists_list))



