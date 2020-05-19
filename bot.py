import requests
from bs4 import BeautifulSoup


def get_html(site):
    r = requests.get(site)
    return r.text


def get_page_data(html):
    try:  
     soup = BeautifulSoup(html, 'lxml')
     line = soup.find('table').find('tbody').find_all('tr')

     for tr in line:
        td = tr.find_all('td')
        ip = td[1].text
        port = td[2].text
        country = td[3].text
        anonym = td[4].text
        types = td[5].text
        time = td[6].text

         data = {'ip': ip,
                'Порт': port,
                'Страна': country,
                'Анонимность': anonym,
                'Тип': types,
                'Время отклика': time}
        
        
    except AttributeError: return False

        print(data)
    

def main():
    url = 'https://www.xbox-now.com/ru/deal-list'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
