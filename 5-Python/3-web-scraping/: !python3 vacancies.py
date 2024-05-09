import requests
import bs4
import lxml
from fake_headers import Headers
import json
import re

# ссылка, вилка зп, название компании, город

interests_template = ['position','link', 'salary', 'emloyer', 'city']
train_data = [['Стажер-разработчик Python',
               'https://spb.hh.ru/vacancy/98465024?query=python&hhtmFrom=vacancy_search_list', 
               'до 10 000 ₽', 
               "ООО Дивергент",  
               "Москва"}]

INTERESTING_URL = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'


def get_headers():
    return Headers(os='win', browser = 'chrome').generate()

def create_pattern(soup, train_file_name):
#    with open(train_file_name) as f:
#        train_data = json.load(f)
    for example in train_data:
        for interest in example:
            interest_tag = (
                soup(href=interest or soup(string=interest)[0].parent)
            print(interest_tag)
    return 

def validate_template():
    pass

def get_template():
    pass

def scraping_bs4():
    response = requests.get(INTERESTING_URL, headers=get_headers())
    soup = bs4.BeautifulSoup(response.text, features = 'lxml')
    

if __name__ == '__main__' :
    scraping_bs4()

