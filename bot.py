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
        td = tr.find_all('td')
        aa = td[1].find('a')
        game = aa.text.replace('\n','').replace('\n','').replace('НОВИНКА','')
        sale = td[2].text.replace('\n','')
        bb = td[3].find('b')
        priceAU = bb.text.replace('\n','').replace('\n','').replace(' RUB','').replace(',','.').replace('\xa0','').replace('RUB','').replace('&nbsp;','')
        priceA = float(float(priceAU)*0.94*1.19)
        price = round(priceA)
        cc = td[4].find('b')
        priceRU = cc.text.replace('\n','').replace('\n','').replace(' RUB','').replace(',','.').replace('\xa0','').replace('RUB','').replace('&nbsp;','')
        priceR = float(float(priceRU)*72)
        priceU = round(priceR)
       
        if (price*2) < priceU
        print(game + ' - ' + str(price + price) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
        else:
       
        print(game + ' - ' + str(price) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')


def main():
    url = 'https://www.xbox-now.com/ru/deal-list'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
