import bs4 as bs
import requests
import pickle

# html = requests.get('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
# soup = bs.BeautifulSoup(html.text, 'html.parser')
#
# tickers = []
# table = soup.find('table', {'class': 'wikitable sortable'})
# rows = table.findAll('tr')[1:]
# for row in rows:
#     ticker = row.findAll('td')[0].text
#     tickers.append(ticker[:-1])
#
# with open('snp500.pickle', 'wb') as f:
#     pickle.dump(tickers, f)

with open('snp500.pickle', 'rb') as f:
    tickers = pickle.load(f)

print(tickers)