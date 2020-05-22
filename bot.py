
from bs4 import BeautifulSoup

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    line = soup.find('tbody').find_all('tr')
    

    for tr in line:
        td = tr.find_all('td')
        td = tr.find_all('td')
        aa = td[1].find('a')
        game = aa.text.replace('\n','').replace('\n','').replace('НОВИНКА','')
        sale = td[2].text.replace('\n','').replace(' (GOLD)','')
        bb = td[3].find('b')
        priceAU = bb.text.replace('\n','').replace('\n','').replace(' RUB','').replace(',','.').replace('\xa0','').replace('RUB','').replace('&nbsp;','')
        priceA = float(float(priceAU)+30)
        price = round(priceA)
        cc = td[4].find('b')
        priceRU = cc.text.replace('\n','').replace('\n','').replace(' RUB','').replace(',','.').replace('\xa0','').replace('RUB','').replace('&nbsp;','')
        priceR = float(float(priceRU)*72)
        priceU = round(priceR)
       
        if float(price) < float(priceU):
            if float(float(price)*2) < float(float(priceU)-200):
                print(game + ' - ' + str(round(float(price)*2)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
            else:
                if float(float(price)*1.95) < float(float(priceU)-200):
                    print(game + ' - ' + str(round(float(price)*1.95)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                else:
                    if float(float(price)*1.9) < float(float(priceU)-200):
                       print(game + ' - ' + str(round(float(price)*1.9)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                    else:
                        if float(float(price)*1.85) < float(float(priceU)-200):
                           print(game + ' - ' + str(round(float(price)*1.85)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                        else:
                            if float(float(price)*1.8) < float(float(priceU)-200):
                               print(game + ' - ' + str(round(float(price)*1.8)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                            else:
                                if float(float(price)*1.75) < float(float(priceU)-200):
                                   print(game + ' - ' + str(round(float(price)*1.75)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                else:
                                    if float(float(price)*1.7) < float(float(priceU)-200):
                                       print(game + ' - ' + str(round(float(price)*1.7)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                    else:
                                         if float(float(price)*1.65) < float(float(priceU)-200):
                                            print(game + ' - ' + str(round(float(price)*1.65)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                         else:
                                             if float(float(price)*1.6) < float(float(priceU)-200):
                                                print(game + ' - ' + str(round(float(price)*1.6)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                             else:
                                                 if float(float(price)*1.55) < float(float(priceU)-200):
                                                    print(game + ' - ' + str(round(float(price)*1.55)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                 else:
                                                     if float(float(price)*1.5) < float(float(priceU)-200):
                                                        print(game + ' - ' + str(round(float(price)*1.5)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                     else:
                                                         if float(float(price)*2) < float(float(priceU)-150):
                                                            print(game + ' - ' + str(round(float(price)*2)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                         else:
                                                             if float(float(price)*1.95) < float(float(priceU)-150):
                                                                print(game + ' - ' + str(round(float(price)*1.95)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                             else:
                                                                    if float(float(price)*1.9) < float(float(priceU)-150):
                                                                        print(game + ' - ' + str(round(float(price)*1.9)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                    else:
                                                                        if float(float(price)*1.85) < float(float(priceU)-150):
                                                                            print(game + ' - ' + str(round(float(price)*1.85)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                        else:
                                                                            if float(float(price)*1.8) < float(float(priceU)-150):
                                                                                print(game + ' - ' + str(round(float(price)*1.8)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                            else:
                                                                                if float(float(price)*1.75) < float(float(priceU)-150):
                                                                                    print(game + ' - ' + str(round(float(price)*1.75)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                                else:
                                                                                    if float(float(price)*1.7) < float(float(priceU)-150):
                                                                                        print(game + ' - ' + str(round(float(price)*1.7)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                                    else:
                                                                                        if float(float(price)*1.65) < float(float(priceU)-150):
                                                                                            print(game + ' - ' + str(round(float(price)*1.65)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                                        else:
                                                                                            if float(float(price)*1.6) < float(float(priceU)-150):
                                                                                                print(game + ' - ' + str(round(float(price)*1.6)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                                            else:
                                                                                                if float(float(price)*1.55) < float(float(priceU)-150):
                                                                                                    print(game + ' - ' + str(round(float(price)*1.55)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                                                else:
                                                                                                    if float(float(price)*1.5) < float(float(priceU)-150):
                                                                                                        print(game + ' - ' + str(round(float(price)*1.5)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                                                    else:
                                                                                                         if float(float(price)*2) < float(float(priceU)-100):
                                                                                                            print(game + ' - ' + str(round(float(price)*2)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                                                         else:
                                                                                                             if float(float(price)*1.95) < float(float(priceU)-100):
                                                                                                                    print(game + ' - ' + str(round(float(price)*1.95)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                                                             else:
                                                                                                                    if float(float(price)*1.9) < float(float(priceU)-100):
                                                                                                                        print(game + ' - ' + str(round(float(price)*1.9)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                                                                    else:
                                                                                                                        if float(float(price)*1.85) < float(float(priceU)-100):
                                                                                                                            print(game + ' - ' + str(round(float(price)*1.85)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                                                                        else:
                                                                                                                            if float(float(price)*1.8) < float(float(priceU)-100):
                                                                                                                                print(game + ' - ' + str(round(float(price)*1.8)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                                                                            else:
                                                                                                                                if float(float(price)*1.75) < float(float(priceU)-100):
                                                                                                                                    print(game + ' - ' + str(round(float(price)*1.75)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                                                                                else:
                                                                                                                                    if float(float(price)*1.7) < float(float(priceU)-100):
                                                                                                                                        print(game + ' - ' + str(round(float(price)*1.7)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                                                                                    else:
                                                                                                                                        if float(float(price)*1.65) < float(float(priceU)-100):
                                                                                                                                            print(game + ' - ' + str(round(float(price)*1.65)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                                                                                        else:
                                                                                                                                            if float(float(price)*1.6) < float(float(priceU)-100):
                                                                                                                                                print(game + ' - ' + str(round(float(price)*1.6)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                                                                                            else:
                                                                                                                                                if float(float(price)*1.55) < float(float(priceU)-100):
                                                                                                                                                    print(game + ' - ' + str(round(float(price)*1.55)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                                                                                                else:
                                                                                                                                                    if float(float(price)*1.5) < float(float(priceU)-100):
                                                                                                                                                        print(game + ' - ' + str(round(float(price)*1.5)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                                                                                                    else:
                                                                                                                                                        if float(float(price)*1.45) < float(float(priceU)-200):
                                                                                                                                                            print(game + ' - ' + str(round(float(price)+1000)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                                                                                                        else:
                                                                                                                                                            if float(float(price)*1.4) < float(float(priceU)-200):
                                                                                                                                                                print(game + ' - ' + str(round(float(price)+900)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                                                                                                            else:
                                                                                                                                                                if float(float(price)*1.35) < float(float(priceU)-200):
                                                                                                                                                                    print(game + ' - ' + str(round(float(price)+800)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                                                                                                                else:
                                                                                                                                                                    if float(float(price)*1.3) < float(float(priceU)-200):
                                                                                                                                                                        print(game + ' - ' + str(round(float(price)+700)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                                                                                                                    else:
                                                                                                                                                                        if float(float(price)*1.45) < float(float(priceU)-150):
                                                                                                                                                                            print(game + ' - ' + str(round(float(price)+650)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                                                                                                                        else:
                                                                                                                                                                            if float(float(price)+1.4) < float(float(priceU)-150):
                                                                                                                                                                                print(game + ' - ' + str(round(float(price)+600)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                                                                                                                            else:
                                                                                                                                                                                if float(float(price)*1.35) < float(float(priceU)-150):
                                                                                                                                                                                    print(game + ' - ' + str(round(float(price)+550)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                                                                                                                                else:
                                                                                                                                                                                    if float(float(price)*1.3) < float(float(priceU)-150):
                                                                                                                                                                                        print(game + ' - ' + str(round(float(price)+500)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                                                                                                                                    else:
                                                                                                                                                                                        if float(float(price)*1.45) < float(float(priceU)-100):
                                                                                                                                                                                            print(game + ' - ' + str(round(float(price)+450)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                                                                                                                                        else:
                                                                                                                                                                                            if float(float(price)*1.4) < float(float(priceU)-100):
                                                                                                                                                                                                print(game + ' - ' + str(round(float(price)+400)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                                                                                                                                            else:
                                                                                                                                                                                                    if float(float(price)*1.35) < float(float(priceU)-100):
                                                                                                                                                                                                        print(game + ' - ' + str(round(float(price)+1000)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                                                                                                                                                    else:
                                                                                                                                                                                                        if float(float(price)*1.3) < float(float(priceU)-100):
                                                                                                                                                                                                            print(game + ' - ' + str(round(float(price)+900)) + ' рублей' + '.' + '(Скидка ' + sale+') ' + 'В магазине Майкрософт: ' + str(priceU) + ' рублей')
                                                                                                                                                                                                        else:
                                                                                                                                                                                                            print('') 

                                                                                                                                                    
                                                                                                                                                    
                                                                                                                                                                        
        

def main():
    url = open('ski.html', 'r')
    get_page_data(url)


if __name__ == '__main__':
    main()
