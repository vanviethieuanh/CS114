import grequests
import datetime
import csv

import logging
logging.basicConfig(level=logging.DEBUG)


class Firewild():
    def __init__(self, start, end, provinceCode) -> None:
        self.province = provinceCode
        self.start = datetime.datetime.strptime(start, "%d/%m/%Y")
        self.end = datetime.datetime.strptime(end, "%d/%m/%Y")

    def GetStat(self, path):
        request_list = []
        days = (self.start-self.end).days
        print(f'Get data from {days} days')
        for i in range(days):
            d = (self.start - datetime.timedelta(days=i))
            dateString = d.strftime("%d!%m!%Y")
            url = f'http://firewatchvn.kiemlam.org.vn/fwdata/search/diaphuong/{self.province}/0/0/{dateString}/{dateString}/1/100'

            request_list.append(grequests.get(url))

        file = csv.writer(open(path, 'a'), lineterminator='\n')
        for resp in grequests.imap(request_list):
            json = resp.json()
            if json:
                for district in json:
                    for ward in district['xas']:
                        file.writerow([resp.url.split('/')[9],
                                        self.province,
                                       district['huyen'],
                                       ward['xa'],
                                       district['sdc']])

firewild = Firewild('1/6/2020','01/01/2008', 45)
firewild.GetStat('stat.csv')
