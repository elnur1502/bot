
from bs4 import BeautifulSoup

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    line = soup.find('tbody').find_all('tr')
    

    for tr in line:
        td = tr.find_all('td')
        aa = td[1].find('a')
        game = aa.text.replace('\n','').replace('\n','')
        sale = td[2].text.replace('\n','').replace(' (GOLD)','')
        bb = td[3].find('b')
        priceAU = bb.text.replace('\n','').replace('\n','').replace(' RUB','').replace(',','').replace('\xa0','').replace('RUB','').replace('&nbsp;','')
        priceA = float(float(priceAU)+30)
        price = round(priceA)
        cc = td[4].find('b')
        priceRU = cc.text.replace('\n','').replace('\n','').replace(' RUB','').replace(',','.').replace('\xa0','').replace('RUB','').replace('&nbsp;','')
        priceR = float(float(priceRU)*72)
        priceU = round(priceR)
       
        if float(price) < float(priceU):
            if float(float(price)*2) < float(float(priceU)-200):
                print(game + ' - ' + str(round(float(price)*2)) + ' rub' + '.' + '(Skidka ' + sale+') ' + 'ssd: ' + str(priceU) + ' rub')
            else:
                print('')                                                                                                               
                                                                                                                                                                        
        

def main():
    url = open('ski.html', 'r')
    get_page_data(url)


if __name__ == '__main__':
    main()
