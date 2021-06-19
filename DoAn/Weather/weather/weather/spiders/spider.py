import numpy

from datetime import date, timedelta
from scrapy import Spider
from scrapy.http import FormRequest

BASE = date(2018, 1, 1)
DATES = numpy.array(
    [(BASE + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(365)])


class WorldWeatherOnlineScraper(Spider):
    name = 'world-weather-online'

    provinces = [
        {
            "url": "https://www.worldweatheronline.com/bac-lieu-weather-history/vn.aspx",
            "title": "Bac Lieu"
        },

        {
            "url": "https://www.worldweatheronline.com/ho-chi-minh-city-weather-history/vn.aspx",
            "title": "Ho Chi Minh City"
        },

        {
            "url": "https://www.worldweatheronline.com/tam-ky-weather-history/vn.aspx",
            "title": "Tam Ky"
        },

        {
            "url": "https://www.worldweatheronline.com/ben-tre-weather-history/vn.aspx",
            "title": "Ben Tre"
        },

        {
            "url": "https://www.worldweatheronline.com/hoa-binh-weather-history/vn.aspx",
            "title": "Hoa Binh"
        },

        {
            "url": "https://www.worldweatheronline.com/tan-an-weather-history/vn.aspx",
            "title": "Tan An"
        },

        {
            "url": "https://www.worldweatheronline.com/bien-hoa-weather-history/vn.aspx",
            "title": "Bien Hoa"
        },

        {
            "url": "https://www.worldweatheronline.com/hong-gai-weather-history/vn.aspx",
            "title": "Hong Gai"
        },

        {
            "url": "https://www.worldweatheronline.com/thai-nguyen-weather-history/vn.aspx",
            "title": "Thai Nguyen"
        },

        {
            "url": "https://www.worldweatheronline.com/buon-me-thuot-weather-history/vn.aspx",
            "title": "Buon Me Thuot"
        },

        {
            "url": "https://www.worldweatheronline.com/hue-weather-history/vn.aspx",
            "title": "Hue"
        },

        {
            "url": "https://www.worldweatheronline.com/thanh-hoa-weather-history/vn.aspx",
            "title": "Thanh Hoa"
        },

        {
            "url": "https://www.worldweatheronline.com/ca-mau-weather-history/vn.aspx",
            "title": "Ca Mau"
        },

        {
            "url": "https://www.worldweatheronline.com/long-xuyen-weather-history/vn.aspx",
            "title": "Long Xuyen"
        },

        {
            "url": "https://www.worldweatheronline.com/tra-vinh-weather-history/vn.aspx",
            "title": "Tra Vinh"
        },

        {
            "url": "https://www.worldweatheronline.com/cam-pha-weather-history/vn.aspx",
            "title": "Cam Pha"
        },

        {
            "url": "https://www.worldweatheronline.com/my-tho-weather-history/vn.aspx",
            "title": "My Tho"
        },

        {
            "url": "https://www.worldweatheronline.com/tuy-hoa-weather-history/vn.aspx",
            "title": "Tuy Hoa"
        },

        {
            "url": "https://www.worldweatheronline.com/cam-ranh-weather-history/vn.aspx",
            "title": "Cam Ranh"
        },

        {
            "url": "https://www.worldweatheronline.com/nam-dinh-weather-history/vn.aspx",
            "title": "Nam Dinh"
        },

        {
            "url": "https://www.worldweatheronline.com/uong-bi-weather-history/vn.aspx",
            "title": "Uong Bi"
        },

        {
            "url": "https://www.worldweatheronline.com/can-tho-weather-history/vn.aspx",
            "title": "Can Tho"
        },

        {
            "url": "https://www.worldweatheronline.com/nha-trang-weather-history/vn.aspx",
            "title": "Nha Trang"
        },

        {
            "url": "https://www.worldweatheronline.com/viet-tri-weather-history/vn.aspx",
            "title": "Viet Tri"
        },

        {
            "url": "https://www.worldweatheronline.com/chau-doc-weather-history/vn.aspx",
            "title": "Chau Doc"
        },

        {
            "url": "https://www.worldweatheronline.com/phan-rang-weather-history/vn.aspx",
            "title": "Phan Rang"
        },

        {
            "url": "https://www.worldweatheronline.com/vinh-weather-history/vn.aspx",
            "title": "Vinh"
        },

        {
            "url": "https://www.worldweatheronline.com/da-lat-weather-history/vn.aspx",
            "title": "Da Lat"
        },

        {
            "url": "https://www.worldweatheronline.com/phan-thiet-weather-history/vn.aspx",
            "title": "Phan Thiet"
        },

        {
            "url": "https://www.worldweatheronline.com/vinh-long-weather-history/vn.aspx",
            "title": "Vinh Long"
        },

        {
            "url": "https://www.worldweatheronline.com/ha-noi-weather-history/vn.aspx",
            "title": "Ha Noi"
        },

        {
            "url": "https://www.worldweatheronline.com/play-cu-weather-history/vn.aspx",
            "title": "Play Cu"
        },

        {
            "url": "https://www.worldweatheronline.com/vung-tau-weather-history/vn.aspx",
            "title": "Vung Tau"
        },

        {
            "url": "https://www.worldweatheronline.com/hai-duong-weather-history/vn.aspx",
            "title": "Hai Duong"
        },

        {
            "url": "https://www.worldweatheronline.com/qui-nhon-weather-history/vn.aspx",
            "title": "Qui Nhon"
        },

        {
            "url": "https://www.worldweatheronline.com/yen-bai-weather-history/vn.aspx",
            "title": "Yen Bai"
        },

        {
            "url": "https://www.worldweatheronline.com/hai-phong-weather-history/vn.aspx",
            "title": "Hai Phong"
        },

        {
            "url": "https://www.worldweatheronline.com/rach-gia-weather-history/vn.aspx",
            "title": "Rach Gia"
        },

        {
            "url": "https://www.worldweatheronline.com/hanoi-weather-history/vn.aspx",
            "title": "Hanoi"
        },

        {
            "url": "https://www.worldweatheronline.com/soc-trang-weather-history/vn.aspx",
            "title": "Soc Trang"
        }
    ]

    def start_requests(self):
        for province in self.provinces:
            for date in DATES:
                formData = {
                    '__VIEWSTATE': 'bOAHi1DyKKoI9N1Qi+rf+0IvttQsK/6dn42d1vyJy+qwH80ZOp2nufB40lX87UOIMSOBjwX4emWaVLSUQISMP/HbOdb+Zw1rT9gwufTGsiKnsBUO',
                    '__VIEWSTATEGENERATOR': 'F960AAB1',
                    'ctl00$MainContentHolder$butShowPastWeather': 'Get+Weather',

                    'ctl00$MainContentHolder$txtPastDate': date,
                    'ctl00$hdlat': '15.34300',
                    'ctl00$hdlon': '107.80500',
                    'ctl00$rblTemp': '1',
                    'ctl00$rblPrecip': '1',
                    'ctl00$rblWindSpeed': '2',
                    'ctl00$rblheight': '1'
                }

                yield FormRequest(province['url'],
                                  formdata=formData,
                                  meta={
                    'date': date,
                    'province': province['title']
                }
                )

    def parse(self, response):
        history = response.css('.row.text-center.wwo-tabular')

        # 9 first element is columns name
        records = history.css('.col.mr-1::text').getall()[9:]

        for i in range(0, len(records), 9):
            yield{
                'province': response.meta['province'],
                'day': response.meta['date'][8:10],
                'month': response.meta['date'][5:7],
                'year': records[i],
                'max': records[i+1],
                'min': records[i+2],
                'wind': records[i+3],
                'wind_d': records[i+4],
                'rain': records[i+5],
                'humidity': records[i+6],
                'cloud': records[i+7],
                'pressure': records[i+8],
            }
