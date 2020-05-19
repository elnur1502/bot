import requests
from bs4 import BeautifulSoup
url = "https://www.xbox-now.com/ru/deal-list"
ua = UserAgent()
header = {
    'User-Agent': ua.random,
    'upgrade-insecure-requests': '1',
    'cookie': 'mos_id=CllGxlx+PS20pAxcIuDnAgA=; session-cookie=158b36ec3ea4f5484054ad1fd21407333c874ef0fa4f0c8e34387efd5464a1e9500e2277b0367d71a273e5b46fa0869a; NSC_WBS-QUBG-jo-nptsv-WT-443=ffffffff0951e23245525d5f4f58455e445a4a423660; rheftjdd=rheftjddVal; _ym_uid=1552395093355938562; _ym_d=1552395093; _ym_isad=2'
    }

def get_html(site):
    r = requests.get(site)
    return r.text


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    line = soup.find('table', class='table').find('tbody').find_all('tr')

    for tr in line:
        td = tr.find_all('td')
        new = td[1].text
        sale = td[2].text
        country = td[3].text
        ru = td[4].text

        data = {'new': new,
                'Скидка': sale,
                'Страна': country,
                'в ру': ru}

        print(data)


def main():
    url = 'https://www.xbox-now.com/ru/deal-list'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
