from urllib import request
from bs4 import BeautifulSoup
import time


def get_html(url):
    response = request.urlopen(url)
    return response


def main():

    users = [4594998]
    for user in users:
        url = 'https://www.kinopoisk.ru/user/{}/list/1/filtr/all/sort/order/perpage/100/'.format(user)
        html = get_html(url)
        soup = BeautifulSoup(html, 'html5lib')

        table = soup.find('table', attrs={'class': 'ten_items'})
        movies = table.find_all('tr')
        user_votes = []
        for movie in movies:
            ratingBlock = movie.find('div', {'class': 'ratingBlockP'})
            kinopoisk_rating = ratingBlock.find('a').text.split(' ')[0]

            user_vote_block = movie.find('div', {'class': 'userVote'})
            user_vote = 0
            if user_vote_block is not None:
                user_vote = user_vote_block.find('p').text

            user_votes += [user_vote]
            # print('Общий рейтинг: {}'.format(kinopoisk_rating))
            # print('Рейнтинг пользователя: {}'.format(user_vote))

        print('Пользователь ' + user)
        print(*user_votes)
        print()
        time.sleep(2)


if __name__ == '__main__':
    main()
