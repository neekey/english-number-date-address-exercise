import urllib.request
import json
from urllib.parse import urlencode
from collections import OrderedDict
from time import sleep


def build_google_place_search_url(api='', query='', city='', country='', pagetoken=''):
    url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'
    query_string = urlencode(OrderedDict(
        key=api,
        query=query + '+' + city + '+' + country,
        pagetoken=pagetoken
    ))
    return url + query_string


def request_search(api, query='', city='', country='', pagetoken='', result=list()):
    url = build_google_place_search_url(api, query, city, country, pagetoken)
    ret = json.loads(urllib.request.urlopen(url).read())
    new_result = ret.get('results')
    next_page_token = ret.get('next_page_token', None)
    if next_page_token is not None:
        # according to the doc, there is a delay before a next page token is issued
        # https://developers.google.com/places/web-service/search#PlaceSearchPaging
        sleep(2)
        return request_search(api, query, city, country, next_page_token, result + new_result)
    else:
        return result + new_result


def transform_place_results(results):
    return [place.get('formatted_address') for place in results]





