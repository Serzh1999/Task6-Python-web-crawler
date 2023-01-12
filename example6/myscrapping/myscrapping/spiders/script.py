import scrapy

class RankScraper(scrapy.Spider):
    name = "rankings"

    def start_requests(self):
        urls = ["https://www.shanghairanking.com/rankings/arwu/2022"]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for row in response.xpath('//*[@class = "rk-table"]//tbody//tr'):
            yield {
                'rank': row.xpath('td[1]//text()').extract_first().strip(),
                'name': row.xpath('td[2]//*[@class="univ-name"]//text()').extract_first().strip(),
                'score': row.xpath('td[5]//text()').extract_first().strip(),
            }
