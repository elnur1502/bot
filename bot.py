
from bs4 import BeautifulSoup

def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    line = soup.find('tbody').find_all('tr')
    

    for tr in line:
        td = tr.find_all('td')
        aa = td[1].find('a')
        
def main():
    url = open('ski.html', 'r')
    get_page_data(url)


if __name__ == '__main__':
    main()
