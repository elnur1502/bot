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
        aa = td[1].find('a')
        game = aa.text.replace('\n','').replace('\n','')
        sale = td[2].text.replace('\n','')
        bb = td[3].find('b')
        priceAU = (float(str(bb))+20)
        
        data = {game + ' - ' + str(priceAU) + ' рублей' + '.' + '(Скидка ' + sale+')'}
      
        print(data)
        

def main():
    url = 'https://www.xbox-now.com/ru/deal-list'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
