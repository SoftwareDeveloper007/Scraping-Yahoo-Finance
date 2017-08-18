from yahoo_finance import Share
import csv

class main():
    def __init__(self):
        self.tickers = ['AET', 'ANTM', 'CI', 'HUM', 'DVA', 'FMS', 'CVS', 'ABC', 'CAH', 'WBA', 'ESRX',
                   'PMC', 'TGT', 'SPLS', 'DG', 'SRCL', 'CMN', 'STE', 'RSG', 'AAPL']
        self.csv_file = open('result.csv', 'w', encoding='utf-8', newline='')
        self.writer = csv.writer(self.csv_file, dialect='excel')
        headers = ['ticker', 'Company', 'date', 'stock price']
        self.writer.writerow(headers)

    def scraping_data(self):
        for key in self.tickers:
            yahoo = Share(key)
            print(key + ": saving data...")
            #print(yahoo.get_name(), yahoo.get_price(), yahoo.get_trade_datetime())
            row = [key, yahoo.get_name(), yahoo.get_trade_datetime(), yahoo.get_price()]
            self.writer.writerow(row)

        self.csv_file.close()
        print('\nAll done successfully!!!')


if __name__ == '__main__':
    app = main()
    app.scraping_data()


