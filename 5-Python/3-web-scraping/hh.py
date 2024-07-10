import os.path
import requests
import bs4
import lxml
from fake_headers import Headers
import hashlib
import re
import json

# ссылка, вилка зп, название компании, город

INTERESTING_URL = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'

def get_headers():
    return Headers(os='win', browser = 'firefox').generate()
    

def get_soup_bs4(url=INTERESTING_URL):
    fname = 'hash/' + hashlib.md5(url.encode()).hexdigest()
    if os.path.isfile(fname):
        with open(fname) as f:
            soup = bs4.BeautifulSoup(f.read(), features = 'lxml')
    else:
        response = requests.get(url, headers=get_headers())
        soup = bs4.BeautifulSoup(response.text, features = 'lxml')
        with open(fname, 'w') as f:
            f.write(response.text)
    return soup

def check_details(url, check_list):
    soup = get_soup_bs4(url).find(
            'div', class_=re.compile('vacancy-description'))
    if soup is None:
        print('No description')
        return False
    print(f'{soup.name=}')
    for detail in check_list:
        print(f'{detail=}')
        if soup(string = re.compile(detail)) != []:
            print('T')
            return True
    return False

if __name__ == '__main__' :
    result_data = []

    soup = get_soup_bs4()
    vacancy_list = soup(class_=re.compile('vacancy-search-item__card'))
    for vacancy_item in vacancy_list:
        position = vacancy_item.find(class_=re.compile('vacancy-name'))
        link = vacancy_item.find(class_=re.compile('bloko-link'))
        salary = vacancy_item.find(class_=re.compile('fake-magritte-primary-text--Hdw8FvkOzzOcoR4xXWni compensation-text--kTJ0_rp54B2vNeZ3CTt2 separate-line-on-xs--mtby5gO4J0ixtqzW38wh'))
        employer = vacancy_item.find(class_=re.compile('company-info-text'))
        city = vacancy_item.find(
                attrs={'data-qa':'vacancy-serp__vacancy-address'})

        result_item = {
            'position': (position.string if position is not None else None),
            'link': (link['href'] if link is not None else None),
            'salary': (
                salary.text.replace(u'\u202f000', '').replace(u'\xa0', ' ')
                if salary is not None else None),
            'employer': (employer.string if employer is not None else None),
            'city': (city.string if city is not None else None)}

        if check_details(result_item['link'], ['Django', 'Flask']):
            result_data.append(result_item)

    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(result_data, f, ensure_ascii=False)



