import requests
from bs4 import BeautifulSoup


with open('skidki.html', 'r') as f: 
        html_string = f.read()


def html_string(html):
    soup = BeautifulSoup(html, 'lxml')
    line = soup.find('tbody').find_all('tr')
   
    

    for tr in line:
        td = tr.find_all('td')
        td = tr.find_all('td')
        aa = td[1].find('a')
        game = aa.text.replace('\n','').replace('\n','').replace('НОВИНКА','')
        sale = td[2].text.replace('\n','')
        bb = td[3].find('b')
        priceAU = bb.text.replace('\n','').replace('\n','').replace(' RUB','').replace(',','.').replace('\xa0','').replace('RUB','').replace('&nbsp;','').replace('&nbsp;','')
        priceA = priceAU
        price = round(float(float(priceA)*0.94*1.19))
        cc = td[4].find('b')
        priceRU = cc.text.replace('\n','').replace('\n','').replace(' RUB','').replace(',','.').replace('\xa0','').replace('RUB','').replace('&nbsp;','')
        priceR = float(float(priceRU)*72)
        priceU = round(priceR)
       
        if float(float(price)*2) < float(float(priceU)-200):
            print(game + ' - ' + str(price + price) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
        else:
       
            print(game + ' - ' + str(price) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')


def main():
   with open('skidki.html', 'r') as f: 
        html_string = f.read()


if __name__ == '__main__':
    main()
