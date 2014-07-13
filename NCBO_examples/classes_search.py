import urllib2
import json
import os
from pprint import pprint

def get_api_key():
    f = open('ncbo_api_key.txt')
    key = f.readline().strip('\n')
    print('Found Key: ', key)
    f.close()
    return key

REST_URL = "http://data.bioontology.org"
API_KEY = get_api_key()

def get_json(url):
    opener = urllib2.build_opener()
    opener.addheaders = [('Authorization', 'apikey token=' + API_KEY)]
    return json.loads(opener.open(url).read())

# Get list of search terms
path = os.path.join(os.path.dirname(__file__), 'classes_search_terms.txt')
terms_file = open(path, "r")
terms = []
for line in terms_file:
    terms.append(line)

# Do a search for every term
search_results = []
for term in terms:
    search_results.append(get_json(REST_URL + "/search?q=" + term)["collection"])

# Print the results
for result in search_results:
    pprint(result)
