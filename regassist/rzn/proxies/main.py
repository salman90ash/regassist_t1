import requests
from bs4 import BeautifulSoup

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
    'Accept-Language': 'ru,ru-RU;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6'
}


# HEADERS = {
#     'user-agent': ua.chrome,
#     'Accept-Language': 'ru,ru-RU;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6'
# }


def get_list_ip_from_hidemy(url='https://hidemy.name/ru/proxy-list/?country=KZRU&type=hs#list'):
    r = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(r.text, 'lxml')
    table_block = soup.find('div', class_='table_block')
    tbody = table_block.find('tbody')
    draft_list_of_proxy = []
    for tr in tbody.find_all('tr'):
        proxy = {
            'ip': tr.find_all('td')[0].text.strip(),
            'port': tr.find_all('td')[1].text.strip(),
            'protocol': tr.find_all('td')[4].text.strip().lower(),
        }
        draft_list_of_proxy.append(proxy)
    return draft_list_of_proxy


def get_ip(url='https://2ip.ru/', proxy=None):
    r = requests.get(url, headers=HEADERS, proxies=proxy)
    soup = BeautifulSoup(r.text, 'lxml')
    ip = soup.find('div', class_='ip').text.strip()
    # ip = soup.find('div', class_='ip').find('big').text.strip()
    # location = soup.find('div', class_='value value-country').text.strip()
    return ip


def get_white_list_of_proxy(list_of_proxy):
    white_list_of_proxy = []
    for proxy in list_of_proxy:
        p = {proxy['protocol']: proxy['ip'] + ':' + proxy['port']}
        two_ip = get_ip(proxy=p)
        # print(f"2ip={two_ip}, hideme={proxy['ip']}")
        if two_ip == proxy['ip']:
            white_list_of_proxy.append(p)
    return white_list_of_proxy


#
list_of_proxyy = get_list_ip_from_hidemy('https://hidemy.name/ru/proxy-list/?country=RU&type=hs#list')

print(list_of_proxyy)
print(get_white_list_of_proxy(list_of_proxyy))

# proxy = {'http': '193.138.178.6:8282'}
# print(get_ip(proxy=proxy))
