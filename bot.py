import requests
from bs4 import BeautifulSoup

def get_html(site):
    r = requests.get(site)
    return r.text


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    line = soup.find('tbody').find_all('tr')
    

    for tr in line:
        td = tr.find_all('td')
        game = td[1].text.replace('\n\n\n\n\n\n','').replace('\nНОВИНКА\n\n\n','').replace('\n\n\n','').replace('\n\n','')
        sale = td[2].text.replace('\n','')
        b = td[3].find('b')
        AU = [e.text for e in b.children if e.name is not None]
        country = str(AU)
        priceRU = b.replace('\n','').replace('\n','').replace(' RUB','')
        priceAU = (priceRU) * 50
        ru = td[4].text.replace('\n\n\n\n\n\nСША**\n\n','').replace('RUB\n\n','$').replace('\n\n\n\n\n\n','')
        
        
        data = {'Игра': game,
                'Скидка': sale,
                'Страна ': priceAU,
                'в ру': ru}

        print(data)


def main():
    url = 'https://www.xbox-now.com/ru/deal-list'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
