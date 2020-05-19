import requests
from bs4 import BeautifulSoup


def get_html(site):
    r = requests.get(site)
    return r.text


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    line = soup.find('table', class='table-striped').find('tbody').find_all('tr')

    for tr in line:
        td = tr.find_all('td')
        new = td[1].text
        sale = td[2].text
        country = td[3].text.replace('\xa0', '')
        ru = td[4].text.replace('\r\n        ', '')

        data = {'new': ip,
                'Скидка': port,
                'Страна': country,
                'в ру': ru}

        print(data)


def main():
    url = 'https://www.xbox-now.com/ru/deal-list'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
