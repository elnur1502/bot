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
        game = td.find('a').find('span').text
        sale = td[2].text.replace('\n','')
        country = td[3].text.replace('\n\n\n\n\n\n','').replace('\r','').replace('\n\n\n','').replace('**\n\n                                    от:\n                                \n\n',' ').replace('RUB\n\n','')
        ru = td[4].text.replace('\n\n\n\n\n\nСША**\n\n','').replace('RUB\n\n','$').replace('\n\n\n\n\n\n','')

        data = {'Игра': game,
                'Скидка': sale,
                'Страна ': country,
                'в ру': ru}

        print(data)


def main():
    url = 'https://www.xbox-now.com/ru/deal-list'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
