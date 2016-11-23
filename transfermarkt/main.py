import requests
from bs4 import BeautifulSoup
import csv
import codecs
import operator

England = 'http://www.transfermarkt.com/premier-league/startseite/wettbewerb/GB1'
Germany = 'http://www.transfermarkt.com/1-bundesliga/startseite/wettbewerb/L1'
Italy = 'http://www.transfermarkt.com/serie-a/startseite/wettbewerb/IT1'
France = 'http://www.transfermarkt.com/ligue-1/startseite/wettbewerb/FR1'
Spain = 'http://www.transfermarkt.com/laliga/startseite/wettbewerb/ES1'
BASE_URL = 'http://www.transfermarkt.com/'


def get_html(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    return response.content


def parse_league_table(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('div', {'class': 'box tab-print'})
    clubs_raw = table.find_all('tr')[1:]

    clubs = {}
    for rank, club_raw in enumerate(clubs_raw):
        a_tag = club_raw.find_all('a', {'class': 'vereinprofil_tooltip'})[1]
        link = BASE_URL + a_tag['href']
        team_name = a_tag.text.strip()
        info = club_raw.find_all('td')[-3:]
        matches = int(info[0].text)
        gd = int(info[1].text)
        points = int(info[2].text)
        clubs[team_name] = {'Rank': rank+1, 'Link': link, 'Matches': matches, 'GD': gd, 'Points': points}

    return clubs


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


def parse_players(club_url):
    html = get_html(club_url)
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('div', {'class': 'grid-view'})
    print(soup.prettify())


def main():
    table = parse_league_table(England)
    save_league_table(table, 'England/table.csv')
    clubs = parse_clubs(Italy)


if __name__ == '__main__':
    main()
