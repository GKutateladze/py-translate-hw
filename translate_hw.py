import requests
import os


def file_dir_path(file):
    dir_path = os.path.dirname(os.path.realpath(file))
    return dir_path

def read_file_by_path(file):
    with open(file) as f:
        return f.read()


def write_file_by_path(file, new_file):
    file_dir_path(file)
    with open(file, 'wt', encoding='utf8') as f:
        f.write(new_file)


def translate(source_file_path, result_file_path, lang_from='fr', lang_to='ru'):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    params = {
        'key': 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152',
        'text': read_file_by_path(source_file_path),
        'lang': {lang_from.lower()}-{lang_to.lower()}
    }

    response = requests.get(url, params=params)
    write_file_by_path(
        result_file_path,
        (' '.join(response.get('text', [])))
    )

translate("FR.txt", "new.txt")