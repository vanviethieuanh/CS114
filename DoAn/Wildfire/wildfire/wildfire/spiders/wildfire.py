from scrapy import Spider
import scrapy
from .provinces import provinces
from datetime import datetime, timedelta

class Wildfire(Spider):
    name = 'firewatch'
    start = datetime.strptime("1/6/2020", "%d/%m/%Y")
    end = datetime.strptime("1/5/2020", "%d/%m/%Y") #1/1/2008
    domain = 'http://firewatchvn.kiemlam.org.vn'

    def start_requests(self):
        requests_list = []
        for province in provinces:
            requests_list.append(scrapy.Request(
                f'{self.domain}/fwdata/hanhchinh/{province["ma"]}/0',
                meta={
                    'province': province['ten'],
                    'provinceCode': province['ma']
                },
                callback=self.get_district
            ))

        return requests_list

    def get_district(self, response):
        # http://firewatchvn.kiemlam.org.vn/fwdata/search/diaphuong/45/466/0/25!06!2020/25!06!2021/1/100
        request_list = []
        for district in response.json():
            start_date = {self.start.strftime("%d!%m!%Y")}
            request_list.append(scrapy.Request(
                f'{self.domain}/fwdata/search/diaphuong/{response.meta["provinceCode"]}/{district["ma"]}/0/{start_date}/{start_date}/1/1000',
                meta={
                    'province':response.meta["province"],
                    'provinceCode': response.meta["provinceCode"],
                    'district':district['ten'],
                    'districtCode': district['ma'],
                    'date':self.start
                }, 
                callback=self.parse
            ))
        return request_list

    def parse(self, response, **kwargs):
        if response.meta['date'] == self.end:
            return
        yesterday = response.meta['date'] - timedelta(days=1)
        yesterdayStrf = yesterday.strftime("%d!%m!%Y")
 
        for ward in response.json():
            for wildfire in ward['hp']:
                yield{
                    'date': response.meta['date'].strftime("%d/%m/%Y"),
                    'province':response.meta["province"],
                    'district':response.meta['district'],
                    'ward':ward['xa'],
                    'long':wildfire['x'],
                    'lat':wildfire['y']
                }
        
        yield response.follow(
                f'{self.domain}/fwdata/search/diaphuong/{response.meta["provinceCode"]}/{response.meta["districtCode"]}/0/{yesterdayStrf}/{yesterdayStrf}/1/1000',
                meta={
                    'province':response.meta["province"],
                    'provinceCode': response.meta["provinceCode"],
                    'district':response.meta['district'],
                    'districtCode': response.meta['districtCode'],
                    'date':yesterday
                }, 
                callback=self.parse
            )


class WildfireByDate(Spider):
    name = 'firewatch-date'
    start = datetime.strptime("1/6/2020", "%d/%m/%Y")
    end = datetime.strptime("1/1/2008", "%d/%m/%Y")
    days = (start-end).days
    domain = 'http://firewatchvn.kiemlam.org.vn'

    def start_requests(self):
        requests_list = []
        for i in range(self.days):
            d = (self.start - timedelta(days=i))
            dateString = d.strftime("%d!%m!%Y")
            
            url = f'{self.domain}/fwdata/search/diaphuong/0/0/0/{dateString}/{dateString}/1/100'
            requests_list.append(scrapy.Request(
                url,
                meta={
                    'date':d,
                },
                callback=self.get_district
            ))
        return requests_list

    def get_district(self, response):
        request_list = []
        d = response.meta['date']
        for province in response.json():
            for district in province['huyens']:
                request_list.append(scrapy.Request(
                    f'{self.domain}/fwdata/search/diaphuong/{province["code"]}/{district["code"]}/0/{d.strftime("%d!%m!%Y")}/{d.strftime("%d!%m!%Y")}/1/1000',
                    meta={
                        'province':province["tinh"],
                        'provinceCode': province["code"],
                        'district':district['huyen'],
                        'districtCode': district['code'],
                        'date':d
                    }, 
                    callback=self.parse
                ))
        return request_list

    def parse(self, response, **kwargs):
        if response.meta['date'] == self.end:
            return
        yesterday = response.meta['date'] - timedelta(days=1)
        yesterdayStrf = yesterday.strftime("%d!%m!%Y")
 
        for ward in response.json():
            for wildfire in ward['hp']:
                yield{
                    'date': response.meta['date'].strftime("%d/%m/%Y"),
                    'province':response.meta["province"],
                    'district':response.meta['district'],
                    'ward':ward['xa'],
                    'long':wildfire['x'],
                    'lat':wildfire['y']
                }
        
        yield response.follow(
                f'{self.domain}/fwdata/search/diaphuong/{response.meta["provinceCode"]}/{response.meta["districtCode"]}/0/{yesterdayStrf}/{yesterdayStrf}/1/1000',
                meta={
                    'province':response.meta["province"],
                    'provinceCode': response.meta["provinceCode"],
                    'district':response.meta['district'],
                    'districtCode': response.meta['districtCode'],
                    'date':yesterday
                }, 
                callback=self.parse
            )