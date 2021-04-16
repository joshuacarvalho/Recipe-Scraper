
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import random
from urllib.request import urlopen, Request

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) ' 
                      'AppleWebKit/537.11 (KHTML, like Gecko) '
                      'Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'none',
        'Accept-Language': 'en-US,en;q=0.8',
        'Connection': 'keep-alive'}

websites = ['https://themodernproper.com/30-best-ground-beef-recipes', 'https://themodernproper.com/30-best-chicken-thigh-recipes', 'https://themodernproper.com/30-best-shrimp-recipes', 'https://themodernproper.com/60-best-vegetarian-meals', 'https://themodernproper.com/30-best-salmon-recipes']



recipe_websites = []

def get_recipe_url(url, length):
    reg_url = url
    req = Request(url=reg_url, headers=headers) 
    html = urlopen(req)
    bs = BeautifulSoup(html, "html.parser")

    x = bs.find_all('li')
    for i in x[5:length]:
        i = str(i)
        parse1 = i.split('ref="')
        parse2 = parse1[1].split('"')
        recipe_websites.append((parse2[0]))

for i in range(len(websites)):
    if i != 3:
        get_recipe_url(websites[i], 35)
    else:
        get_recipe_url(websites[i], 65)

recipe_num = random.randint(0, len(recipe_websites)-1)
recipe = recipe_websites[recipe_num]

#this gets the title of recipe
req = Request(url=recipe, headers=headers) 
html = urlopen(req)
bs = BeautifulSoup(html, "html.parser")
z = bs.find('h1', {'class': "post-hero__title"})

if z != None:
    print("your recipe is {} for info on how to make visit {}".format(z.get_text(), recipe))
else:
    print('For info on making recipe visit {}'.format(recipe))
"""
req = Request(url='https://themodernproper.com/braised-chicken-with-potatoes-and-chive-butter-sauce', headers=headers) 
html = urlopen(req)
bs = BeautifulSoup(html, "html.parser")
z = bs.find_all('li')

     """   
        

    



