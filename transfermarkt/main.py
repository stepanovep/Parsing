import requests
from bs4 import BeautifulSoup
import csv
import codecs
import operator
import os

England = 'http://www.transfermarkt.com/premier-league/startseite/wettbewerb/GB1'
Germany = 'http://www.transfermarkt.com/1-bundesliga/startseite/wettbewerb/L1'
Italy = 'http://www.transfermarkt.com/serie-a/startseite/wettbewerb/IT1'
France = 'http://www.transfermarkt.com/ligue-1/startseite/wettbewerb/FR1'
Spain = 'http://www.transfermarkt.com/laliga/startseite/wettbewerb/ES1'
BASE_URL = 'http://www.transfermarkt.com/'


def get_html(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    return response.content


def parse_league_table(league_url):
    html = get_html(league_url)
    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', {'class': 'box tab-print'})
    table_raw = temp.find_all('tr')[1:]

    table = {}
    for rank, club_raw in enumerate(table_raw):
        a_tag = club_raw.find_all('a', {'class': 'vereinprofil_tooltip'})[1]
        link = BASE_URL + a_tag['href']
        team_name = a_tag.text.strip()
        info = club_raw.find_all('td')[-3:]
        matches = int(info[0].text)
        gd = int(info[1].text)
        points = int(info[2].text)
        table[team_name] = {'Rank': rank+1, 'Link': link, 'Matches': matches, 'GD': gd, 'Points': points}

    return table


def save_league_table(table, path):
    with codecs.open(path, 'w', 'utf-8') as csvfile:
        sorted_clubs = sorted(table.items(), key=lambda x: operator.getitem(x[1], 'Rank'))
        fieldnames = ['Rank', 'Team', 'Matches', 'GD', 'Points']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()

        for club in sorted_clubs:
            d = club[1]
            d['Team'] = club[0]
            del d['Link']
            writer.writerow(d)


def parse_clubs(league_url):
    clubs = {}
    html = get_html(league_url)
    soup = BeautifulSoup(html, 'html.parser')
    clubs_raw = soup.find('div', {'class': 'responsive-table'}).find('tbody').find_all('tr')
    for club_raw in clubs_raw:
        temp = club_raw.find_all('td')[1]
        team, rel_link = temp.text.strip(), temp.a['href']
        link = BASE_URL + rel_link
        clubs[team] = link

    return clubs


def save_clubs(clubs, path):
    with codecs.open(path, 'w', 'utf-8') as csvfile:
        fieldnames = ['Team', 'Link']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')
        writer.writeheader()

        for club in clubs:
            d = {'Team': club, 'Link': clubs[club]}
            writer.writerow(d)


def parse_players(club_url):
    html = get_html(club_url)
    soup = BeautifulSoup(html, 'html.parser')
    players_raw = soup.find('div', {'id': 'yw1'}).find('tbody').find_all('tr', recursive=False)

    players = []
    for player_raw in players_raw:
        td_tags = player_raw.find_all('td', recursive=False)
        number = td_tags[0].find('div', {'class': 'rn_nummer'}).text
        if number == '-':
            number = -1
        else:
            number = int(number)

        name_raw = td_tags[1].find('table', {'class': 'inline-table'}).find('img')
        name = name_raw.get('title').strip()

        position = player_raw.find('td').get('title')

        born = td_tags[3].text.strip()[:-5]

        nation = td_tags[4].find('img').get('title').strip()

        value = td_tags[5].text.strip()

        players.append(
            {'number': number,
             'name': name,
             'position': position,
             'born': born,
             'nation': nation,
             'value': value}
        )

    return players


def save_league_players(league, path):
    directory = '{}clubs/'.format(path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    clubs = parse_clubs(league)
    for i, club in enumerate(clubs):
        print('Parsing progress {}%'.format((i+1)*5))
        with codecs.open('{}{}.csv'.format(directory, club), 'w', 'utf-8') as csvfile:
            fieldnames = ['number', 'name', 'position', 'born', 'nation', 'value']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter='\t')
            writer.writeheader()
            players = parse_players(clubs[club])
            for player in players:
                writer.writerow(player)


def get_variable_name(p):
    import inspect
    import re
    for line in inspect.getframeinfo(inspect.currentframe().f_back)[3]:
        m = re.search(r'\bget_variable_name\s*\(\s*([A-Za-z_][A-Za-z0-9_]*)\s*\)', line)
        if m:
            return m.group(1)


def main():
    table = parse_league_table(England)
    save_league_table(table, 'England/table.csv')

    clubs = parse_clubs(England)

    save_league_players(Italy, 'Italy/')


if __name__ == '__main__':
    main()
