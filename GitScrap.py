import json
from operator import itemgetter
from pprint import pprint
import requests
from bs4 import BeautifulSoup
from github import Github
from jupyter_core import application

token = "c5780ed32424dd99a3a4665504a438c1d1473e9a"
login = "cyounesv"
url = "https://gist.github.com/paulmillr/2657075"
apiurl = "https://api.github.com/users/"
tokenurl = "?access_token=" + token
dict_token = {"access_token": "c5780ed32424dd99a3a4665504a438c1d1473e9a"}


g = Github(token)
def get_soup_from_url(url):
    return BeautifulSoup(requests.get(url).text, 'html.parser')


def get_contributors_from_page(soup):
    table = soup.find('tbody')
    list_of_contributors = []
    i = 1
    for row in table.find_all("tr"):
        if i <= 256:
            list_of_contributors.append(row.find("a").text)
            i += 1
    print(list_of_contributors)
    return list_of_contributors


def get_average_stars(user_id, g):
    #url = apiurl + user + "/repos" + tokenurl
    #req = requests.get(url, params=dict_token).text
    #js = json.loads(req)
    #average_star = 0
    curr_user = g.get_user(user_id)
    repos = curr_user.get_repos()
    stars_user = 0.0
    count = 0
    for repo in repos:
        #stars_user += repo["stargazers_count"]
        stars_user += repo.stargazers_count
        count += 1
        try:
            average_star = stars_user / count
        except ZeroDivisionError:
            average_star = 0.0
    return stars_user / count


avg_stars_user = {}
get_contributors_from_page(get_soup_from_url(url))
for user in get_contributors_from_page(get_soup_from_url(url)):
    avg_stars_user[user] = get_average_stars(user, g)
   # print(user, avg_stars_user[user])


sorted_avg_stars_user = sorted(avg_stars_user.items(), key=itemgetter(1), reverse=True)
print(sorted_avg_stars_user)