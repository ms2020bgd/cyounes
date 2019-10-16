import unittest
import requests
from bs4 import BeautifulSoup

URL_PAGE2 = "https://kim.fspot.org/cours/page2.html"
URL_PAGE3 = "https://kim.fspot.org/cours/page3.html"


# Write a function which extract some infos from the pages above.
# Example:
#     get_prices_from_url(URL_PAGE2) should return something like this:
#
#     {
#         'Personal': {
#             'price': '$5',
#             'storage': '1GB',
#             'databases': 1
#         },
#         'Small Business': {
#             'price': '$25',
#             'storage': '10GB',
#             'databases': 5
#         },
#         'Enterprise': {
#             'price': '$45',
#             'storage': '100GB',
#             'databases': 25
#         }
#     }
def get_prices_from_url(url):
    soup1 = get_soup_from_url(url)
    personal = '<span class="pricing-table-price">'
    test1 = soup1.find_all(class_="l-content")
    print(test1)


    return


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
URL_BEERLIST_AUTRICHE = "https://www.beerwulf.com/fr-FR/api/search/searchProducts?country=Autriche&container=Bouteille"


def get_soup_from_url(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'html.parser')
    return soup


get_prices_from_url(URL_PAGE2)

def extract_info(url):
    soup = BeautifulSoup(requests.get(URL_PAGE2).content)
    elems = {}
    for elems in soup.find_all('div',class_="pricing-=table"):
        product = elems.find('h2')
        storage, database = elems.find('span, class_="pricing-table-list').text.strip().split()[3:5]
        elems[product]={
            'price' : elems.find('span, class_="pricing-table-price').text.strip().split()[0],
            'storage': elems.find('span, class_="pricing-table-list').text.strip().split()[3],
            'databases': elems.find('span, class_="pricing-table-list').text.strip().split()[4]

        }
    return elems


def extract_beer_list_infos(url):
    import json
    data = requests.get(url).content
    data = json.load(data)
    beers = data['items']
    beers_urls = ['http://beerwulf.com' + b['contentReference']
                  for b in beers
                  ]

    from multiprocessing import Pool
    pool = Pool(processes=8)
    result = pool.map(extract_beer_info, )

    return[extract_beer_list_infos(beers_url) for beer_url in beers_urls]

45765889

list(first_elem.find('span', class_="pricing-table-price").strings)

extract_info(URL_PAGE2)