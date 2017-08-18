from yahoo_finance import Share
import csv
import datetime

class main():
    def __init__(self):
        self.ticker = 'AAPL'
        self.csv_file = open('result.csv', 'w', encoding='utf-8', newline='')
        self.writer = csv.writer(self.csv_file, dialect='excel')
        headers = ['date', 'stock price']
        self.writer.writerow(headers)

    def scraping_data(self):
        print('Scraping data...')
        yahoo = Share(self.ticker)
        yahoo.refresh()
        print(yahoo.get_name())
        self.total_data = yahoo.get_historical('2017-07-11', '2017-07-12')

        for data in self.total_data:
            row = [data['Date'], data['Adj_Close']]
            self.writer.writerow(row)

        self.csv_file.close()
        print('\nAll done successfully!!!')


if __name__ == '__main__':
    app = main()
    app.scraping_data()


