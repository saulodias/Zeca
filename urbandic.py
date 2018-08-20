from urllib.request import urlopen
import json
import re


class UDQuery:
    """
    Looks a word up in the Urban Dictionary using Urban Dictionary's API.
    All the definitions found are stored in 'data', but the property 'definition'
    contains the definition which corresponds to 'index', which defaults
    to zero if none is entered, that is, the first definition.
    """
    def __init__(self, entry, index=0):
        self.entry = entry
        baseurl = 'http://api.urbandictionary.com/v0/define?term={}'
        url = baseurl.format(_urlify(self.entry))
        response = urlopen(url)
        self.data = json.loads(response.read())
        self.definition = self.data['list'][index]['definition']
        self.permalink = self.data['list'][index]['permalink']
        self.favicon = 'https://cdn.discordapp.com/attachments/477837663488180244/481154213288738837/udico.png'
        self.disclaimer = 'Urban Dictionary contains slang and profanity. Use it discreetly.'

def _urlify(s):
    # Remove all non-word characters
    s = re.sub(r'[^\w\s]', '', s)
    # Replace all runs of whitespace with +
    s = re.sub(r'\s', '+', s)
    return s


if __name__ == '__main__':
    myquery = UDQuery('porb', 0)
    print(myquery.definition)
