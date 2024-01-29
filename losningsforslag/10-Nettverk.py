import requests
import argparse


def wikipedia_get(params):
    url = 'https://en.wikipedia.org/w/api.php'
    response = requests.get(url, params=params)
    return response.json()


def wikipedia_search(word):
    return wikipedia_get({'action': 'opensearch',
                          'search': word})


def wikipedia_lang(page):
    return wikipedia_get({'action': 'parse',
                          'page': page,
                          'prop': 'langlinks',
                          'format': 'json'})


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument('--query', type=str, default='github',
                        help="Word to search for")
    parser.add_argument('--lang', type=str, default='no',
                        help="Language to search for")
    return parser.parse_args()


def main():

    args = parse_args()

    result = wikipedia_search(args.query)

    for page in result[1]:
        print(page)

        lang = wikipedia_lang(page)

        for lang_entry in lang['parse']['langlinks']:
            language = lang_entry['lang']
            if language.lower() == args.lang:
                print(lang_entry)


if __name__ == "__main__":
    main()
