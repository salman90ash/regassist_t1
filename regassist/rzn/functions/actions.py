from rzn.functions.settings import RZN_DOMAIN, RZN_TYPES
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup
import json


def set_url_for_py(rzn_number: str, rzn_date: str) -> str:
    return RZN_DOMAIN + '/services/cab_mi?type_search=1&letters=0&in_doc_num=' + rzn_number + '&in_doc_dt=' + rzn_date


def set_url_for_vird(rzn_number: str, rzn_date: str) -> str:
    return RZN_DOMAIN + '/services/cab_mi?type_search=1&letters=0&in_doc_num=' + rzn_number + '&in_doc_dt=' + rzn_date


def set_url_for_duplicate(rzn_number: str, rzn_date: str) -> str:
    return RZN_DOMAIN + '/services/cab_mi?type_search=4&letters=0&in_doc_num=' + rzn_number + '&in_doc_dt=' + rzn_date


# doc_type=1 - входящий
# doc_type=2 - исходящий
def set_url_for_letters(number: str, date: str, rzn_requisites: bool = False) -> str:
    if rzn_requisites:
        return RZN_DOMAIN + '/services/le?&doc_type=1&doc_num=' + number + '&doc_dt=' + date
    return RZN_DOMAIN + '/services/le?&doc_type=2&doc_num=' + number + '&doc_dt=' + date


# 1	РУ
# 2	Ввоз
# 3	Обращения по вх.
# 4	ВИРД
# 5	Дубликат
# 6	Обращения по исх.


def get_type_title(type_id):
    global RZN_TYPES
    for type_ in RZN_TYPES:
        if type_[0] == type_id:
            return type_[1]
    return False


def set_url(number: str, date: str, rzn_type: int) -> str:
    url = ''
    if rzn_type == 1:
        url = set_url_for_py(number, date)
    elif rzn_type == 2 or rzn_type == 3:
        url = set_url_for_letters(number, date, rzn_requisites=True)
    elif rzn_type == 4:
        url = set_url_for_vird(number, date)
    elif rzn_type == 5:
        url = set_url_for_duplicate(number, date)
    elif rzn_type == 6:
        url = set_url_for_letters(number, date)
    return url


def get_page(url: str, proxy: dict = {}) -> str:
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
    r = requests.get(url, headers=HEADERS, proxies=proxy, verify=False)
    return r.text


def get_table_of_cab_mi(html: str) -> str:
    soup = BeautifulSoup(html, 'lxml')
    return soup.find('div', class_='m-cabinet-results-table').text.strip()


def get_table_of_le(html: str) -> str:
    soup = BeautifulSoup(html, 'lxml')
    return soup.find('div', class_='m-cabinet-results-table').text.strip()


def get_key_of_cab_mi(table: str) -> list:
    rows = table.split('\n\n')
    list_rows = [row[1:].split('\n') for row in rows if row != '' or row.find('\n') != -1]
    return list_rows


def get_key_of_le(table: str) -> list:
    # return table.split('\n')
    return [row for row in table.split('\n') if row != '' or row.find('\n') != -1]

