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
        bb = td[3].find('b')
        priceAU = bb.text.replace('\n','').replace('\n','').replace(' RUB','')
        ru = td[4].text.replace('\n\n\n\n\n\nСША**\n\n','').replace('RUB\n\n','$').replace('\n\n\n\n\n\n','')
        
        
        data = {game + '-' + priceAU '.' + 'Скидка': sale}
        
        global  b
        d = " "
        for i in data:            
            b = data[i]
            c = i+": "+data[i]
            d = d+c+', '
            
        with open('sale.txt', 'a') as f:
            print(data, file=f)
            
        print(data)


def main():
    url = 'https://www.xbox-now.com/ru/deal-list'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
