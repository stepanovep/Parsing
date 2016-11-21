import urllib.request
from bs4 import BeautifulSoup


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def get_solved_tasks(author_url):
    html = get_html(author_url)
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find_all('p', {'class': 'text'})
    solved_raw = table[0]
    failed_raw = table[1]

    solved = set()
    for href in solved_raw.find_all('a'):
        solved.add(int(href.text))

    failed = set()
    for href in failed_raw.find_all('a'):
        failed.add(int(href.text))

    return solved


def get_difference(author1_url, author2_url):
    solved1 = get_solved_tasks(author1_url)
    solved2 = get_solved_tasks(author2_url)
    return solved2.difference(solved1)


def get_tasks_url(tasks_id):
    base_url = 'http://acmp.ru/?main=task&id_task='
    tasks_url = []
    for task in tasks_id:
        tasks_url.append('{}{}'.format(base_url, task))

    return tasks_url


def main():
    author_url = 'http://acmp.ru/?main=user&id=106586'
    author_url2 = 'http://acmp.ru/?main=user&id=85473'

    tasks = get_tasks_url(get_difference(author_url2, author_url))
    for task in tasks:
        print(task)


if __name__ == '__main__':
    main()
