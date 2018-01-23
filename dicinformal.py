import requests
import re
from bs4 import BeautifulSoup


class Query():
    """
    This is a scraper to look up words in dicionarioinformal.com.br,
    an informal Brazilian Portuguese dictionary written by Brazilians.
    """
    favicon = 'https://cdn.discordapp.com/attachments/398647613886431243/401099736884707329/favicon.png'
    disclaimer = 'O Dicionário inFormal® possui gírias e ' + \
                 'palavras de baixo calão. Use com discrição.'
                 
    def __init__(self, term=None):
        self.term = term
        alphanum = bool(re.search('[a-zA-Z0-9 ]', term))
        if term is None or not alphanum:
            self.term = 'Dicionário inFormal'
        self.url = 'http://www.dicionarioinformal.com.br/' + \
                    _urlify(self.term) + '/'
        r = requests.get(self.url)
        if r.status_code != 200:
            raise Exception(str(r.status_code) + 'Error')
        content = BeautifulSoup(r.content, 'html.parser')
        self.content = content

    def fetch(self, *args, **kwargs):
        value = self.content.find(*args, **kwargs)
        if value is None:
            raise ValueError('No results found.')
        value = value.text
        value = value.strip(' \t\n')
        value = _trim(value)
        return value
    
    def fetch_all(self, *args, **kwargs):
        value = self.content.find_all(*args, **kwargs)
        if value is None:
            raise ValueError('No results found.')
        value = [i.text for i in value]
        value = [i.strip(' \t\n') for i in value]
        value = list(map(_trim, value))
        return value

    @property
    def meanings(self):
        return self.fetch_all('p', class_='text-justify')

    @property
    def quotes(self):
        return self.fetch_all('blockquote', class_='text-justify')
    
    @property
    def meaning(self):
        return self.fetch('p', class_='text-justify')
    
    @property
    def quote(self):
        return self.fetch('blockquote', class_='text-justify')

    @property
    def description(self):
        value = '{}'.format(self.meaning)
        if self.quote:
            value = value + '\n\n*{}*'.format(self.quote)
        return value
    
    @property
    def definition(self):
        value = '**{}**\n'.format(self.term)
        value = value + self.description
        return value


def _urlify(s):
    # Remove all non-word characters
    s = re.sub(r'[^\w\s]', '', s)
    # Replace all runs of whitespace with %20
    s = re.sub(r'\s+', '%20', s)
    return s


def _trim(value):
    if len(value) > 400:
            value = value[:400] + '...'
    return value


if __name__ == "__main__":
    result = Query('teste')
    print(result.definition)
