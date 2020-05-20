import requests
from bs4 import BeautifulSoup
from skidki.html import parse
# Получаем страничку
page = parse(skidki.html).getroot()
# Ищем все теги <a> с css классом topic
hrefs = page.cssselect("a.topic")
for row in hrefs:
    # Получаем атрибут href
    print row.get("href")
