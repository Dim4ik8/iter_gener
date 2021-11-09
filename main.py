import json
from urllib.parse import urljoin


class WikiCountryIterator:
    json_data = None
    page_list = []

    def __init__(self, input_filename) -> None:
        with open(input_filename) as json_file:
            self.json_data = iter(json.load(json_file))


        with open('links.txt', 'w', encoding='UTF-8') as f:
            f.write('')


    def __iter__(self):
        return self

    def __next__(self):
        next = self.json_data.__next__()['name']['common']
        url_next = next.replace(' ', '_')
        url = urljoin('https://en.wikipedia.org/wiki/', url_next)
        print(url)
        with open('links.txt', 'a', encoding='UTF-8') as f:
            f.write(f'{next}: {url}\n')

        return self.json_data.__next__()


if __name__ == '__main__':

    wiki = WikiCountryIterator('countries.json')
    for item in wiki:

        print(item['translations']['rus'])
        pass
