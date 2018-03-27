from bs4 import BeautifulSoup
import requests
from time import gmtime, strftime, sleep
import sqlite3

dbname = 'monero.db'
monero_prices = {}
prices = []
times = []


def createSQLdb(in1):
	conn = sqlite3.connect('in1')
	c = conn.cursor()
	c.execute('''CREATE TABLE historicaldata
             (date text, open real, high real, low real, close real)''')
	conn.commit()
	conn.close()

def runningPrice():
	while True:
		curprice = {}
		r = requests.get('https://coinmarketcap.com/currencies/monero/')
		soup = BeautifulSoup(r.content, 'lxml')
		for i in soup.find_all('span', {'id': 'quote_price'}):
			price = i.contents[1].text
			time = strftime("%Y-%m-%d %H:%M:%S")
			curprice['Time'] = time
			curprice['Price'] = price
			print('Time: ', curprice['Time'], 'Price: ', curprice['Price'])
			monero_prices = dict(zip(times, prices))
			sleep(1)


def historicalData():
	data = {}
	r = requests.get('httpteSQLdb():
	conn = sqlite3.connect('monero.db')
	c = conn.cursor()
	c.execute('''CREATE TABLE historicaldata
             (date text, open real, high real, low real, close real)''')
	conn.commit()
conn.close()https://www.coinmarketcap.com/currencies/monero/historical-data/')
	soup = BeautifulSoup(r.content, 'lxml')
	value = lambda td: td.attrs.get('data-format-value', td.text)
	for row in soup.select('table.table tbody tr'):
		data = ([value(td) for td in row.select('td')])
		for i in data:
			print(data)
			
if __name__ == '__main __':
	createSQLdb(dbname)
	historicalData()
	runningPrice()
