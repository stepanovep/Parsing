import csv
import codecs
import urllib.request
from bs4 import BeautifulSoup
from acmp.solved_tasks import get_tasks_count

best_solutions_url = 'http://acmp.ru/index.asp?main=bstatus&id_t='
tasks_count = get_tasks_count()


def save_task(task, path):
    with codecs.open(path, 'w', 'utf-8') as csvfile:
        fieldnames = ['Rank', 'Date', 'Author', 'Language', 'Time', 'Memory', 'Size']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')

        writer.writeheader()
        for author in task:
            writer.writerow(author)


def save_all():
    one_percent = tasks_count // 100
    for j in range(1, tasks_count+1):
        if j % one_percent == 0:
            print('Parsing progress: {}%'.format(j // one_percent))
        task = get_best_solutions('{}{}'.format(best_solutions_url, j))
        save_task(task, 'tasks/{}.csv'.format(str(j).zfill(4)))


def load_task(task_id):
    task = []
    with codecs.open('tasks/{}.csv'.format(str(task_id).zfill(4)), encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        for ind, row in enumerate(reader):
            if ind == 0:
                continue

            task.append({
                'Rank': int(row[0]),
                'Date': row[1],
                'Author': row[2],
                'Language': row[3],
                'Time': float(row[4]),
                'Memory': row[5],
                'Size': int(row[6])
            })
    return task


def load_all():
    tasks = []
    tasks.append([])
    for j in range(1, tasks_count+1):
        tasks.append(load_task(j))

    return tasks


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def get_best_solutions(url):
    html = get_html(url)

    soup = BeautifulSoup(html, "html.parser")
    best_solutions_raw = soup.find_all('tr', {'class': 'white'})

    best_solutions = []
    for row in best_solutions_raw:
        row = row.find_all('td')
        best_solutions.append({
            'Rank': int(row[0].text),
            'Date': row[1].text,
            'Author': row[2].text,
            'Language': row[3].text,
            'Time': float(row[4].text.replace(',', '.')),
            'Memory': row[5].text,
            'Size': int(row[6].text)
        })

    return best_solutions


def tasks_on_top(tasks, name):
    on_top = []
    for task_id, task in enumerate(tasks):
        for solution in task:
            if name.lower() in solution['Author'].lower():
                on_top.append(task_id)

    return on_top


def main():
    save_all()
    tasks = load_all()
    print(tasks_on_top(tasks, 'Егор Степанов спбгу').__len__())


if __name__ == '__main__':
    main()
