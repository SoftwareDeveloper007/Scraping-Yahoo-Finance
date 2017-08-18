from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

def get_historical_data(name, number_of_days):
	data = []
	url = "https://finance.yahoo.com/quote/" + name + "/history/"
	rows = BeautifulSoup(urlopen(url).read(), 'html.parser').findAll('table')[1].tbody.findAll('tr')

	for each_row in rows:
		divs = each_row.findAll('td')
		if divs[1].span.text  != 'Dividend': #Ignore this row in the table
			#I'm only interested in 'Open' price; For other values, play with divs[1 - 5]
			data.append({'Date': divs[0].span.text, 'Open': float(divs[1].span.text.replace(',',''))})

	print(len(data))

	return data[:number_of_days]

#Test

result = get_historical_data('AAPL', 365)

csv_file = open('result.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)
headers = ['date', 'stock price']
writer.writerow(headers)

cnt = len(result)

for i in range(cnt-1, -1, -1):
	row = [result[i]['Date'], result[i]['Open']]
	writer.writerow(row)

csv_file.close()

