import scrapy

class TheGuardianSpider(scrapy.Spider):
    name = 'guardian'
    start_urls = ['https://www.theguardian.com/world/coronavirus-outbreak/all',
                  'https://www.theguardian.com/world/all',
                  'https://www.theguardian.com/science/all',
                  'https://www.theguardian.com/global-development/all',
                  'https://www.theguardian.com/technology/all',
                  'https://www.theguardian.com/business/all',
                  'https://www.theguardian.com/sport/all',
                  'https://www.theguardian.com/books/all',
                  'https://www.theguardian.com/music/all',
                  'https://www.theguardian.com/tv-and-radio/all',
                  'https://www.theguardian.com/artanddesign/all',
                  'https://www.theguardian.com/games/all',
                  'https://www.theguardian.com/stage/all',
                  'https://www.theguardian.com/fashion/all',
                  'https://www.theguardian.com/food/all',
                  'https://www.theguardian.com/tone/recipes/all',
                  'https://www.theguardian.com/tone/letters/all',
                  'https://www.theguardian.com/tone/cartoons',
                  'https://www.theguardian.com/lifeandstyle/all',
                  'https://www.theguardian.com/commentisfree/all'
    ]

    def parse(self, response):
        for article in response.css('.fc-slice-wrapper ul >li.u-faux-block-link'):

            article_link = article.css(
                'a.u-faux-block-link__overlay::attr(href)').get()
            headline = article.css('span.js-headline-text::text').get()
            posted_at = article.css('time::attr(datetime)').get()

            if '2017-12-31' == posted_at[:10]:
                return

            yield{
                'article_link': article_link,
                'headline': headline,
                'posted_at': posted_at,
                'is_sarcastic': 0
            }

        next_page = response.css('a[aria-label=" next page"]').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

class CBSNewsSpider(scrapy.Spider):
    name = 'cbs'
    start_urls = [  'https://www.cbsnews.com/us/',
                    'https://www.cbsnews.com/world/',
                    'https://www.cbsnews.com/politics/',
                    'https://www.cbsnews.com/entertainment/',
                    'https://www.cbsnews.com/health/',
                    'https://www.cbsnews.com/moneywatch/',
                    'https://www.cbsnews.com/cbsvillage/',
                    'https://www.cbsnews.com/technology/',
                    'https://www.cbsnews.com/science/',
                    'https://www.cbsnews.com/crime/'
    ]

    def parse(self, response):
        for article in response.css('section.list-river.component article.item--type-article'):

            article_link = article.css(
                'a.item__anchor::attr(href)').get()
            headline = article.css('h4::text').get().strip()
            posted_at = article.css('li.item__date::text').get()

            if 'Dec 31, 2020' == posted_at[:10]:
                return

            yield{
                'article_link': article_link,
                'headline': headline,
                'posted_at': posted_at,
                'is_sarcastic': 0
            }

        next_page = response.css('a.component__view-more.component__view-more--sm.lazyload::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
