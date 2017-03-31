from urllib import request
from bs4 import BeautifulSoup
import time


def get_html(url):
    response = request.urlopen(url)
    return response


def main():
    users = [145918, 2961108, 3962681, 7155177, 316688, 2521043, 606004, 2379794, 2632907, 1971057, 6760336, 707741,
             3534867, 6880365, 1700000, 179882, 1138038, 579327, 1006811, 5010580, 4210787, 7044946, 2817979, 881867,
             1573883, 1655008, 2611479, 4990235, 892460, 519115, 6344772, 1181079, 3364306, 19645, 3772982, 1419136,
             5853184]
    for user in users:
        url = 'https://www.kinopoisk.ru/user/{}/list/1/filtr/all/sort/order/perpage/100/'.format(user)
        html = get_html(url)
        soup = BeautifulSoup(html, 'html5lib')

        table = soup.find('table', attrs={'class': 'ten_items'})
        movies = table.find_all('tr')
        user_votes = []
        for movie in movies:
            rating_block = movie.find('div', {'class': 'ratingBlockP'})
            kinopoisk_rating = rating_block.find('a').text.split(' ')[0]

            user_vote_block = movie.find('div', {'class': 'userVote'})
            user_vote = 0
            if user_vote_block is not None:
                user_vote = user_vote_block.find('p').text

            user_votes += [user_vote]
            # print('Общий рейтинг: {}'.format(kinopoisk_rating))
            # print('Рейнтинг пользователя: {}'.format(user_vote))

        print('Пользователь {}'.format(user))
        print(*user_votes)
        print()
        time.sleep(4)


if __name__ == '__main__':
    main()
