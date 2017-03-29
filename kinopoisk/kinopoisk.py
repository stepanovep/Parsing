import time
from urllib import request
from bs4 import BeautifulSoup


def get_html(url):
    page = request.urlopen(url)
    return page


def main():
    users = ['4594997']
    main_url = 'http://www.myliverpool.ru/'
    for user in users:
        html = get_html('https://www.kinopoisk.ru/user/{}/list/1/filtr/all/sort/order/perpage/100/'.format(user))
        print(html)
        soup = BeautifulSoup(html, 'html.parser')
        print(soup)

        #table = soup.find('table', attrs={'class': 'ten_items'})
        #print(table)

if __name__ == '__main__':
    main()
