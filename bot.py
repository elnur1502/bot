
from bs4 import BeautifulSoup

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    line = soup.find('div', 'row')
    divs5 = line.find_all('div', 'col-xs-12 col-lg-5')
    divs6 = line.find_all('div', 'col-xs-12 col-lg-6')
    for div in divs5:
    	aa = div.find('a').find('span').text.replace("вЂ","'").replace("в„ў","").replace("В®","").replace("™","").replace("Ђ","'").replace("пј†","&").replace("Bundle","Комплект").replace(" '“ "," ").replace("Game of The Year Edition","Издание «Игра года»")
        print(aa)
    print(divs6)
    
    
    
    
def main():
    url = open('ski.html', 'r')
    get_page_data(url)


if __name__ == '__main__':
    main()
