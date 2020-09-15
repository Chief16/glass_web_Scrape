import scrapy


class GlassSpider(scrapy.Spider):
    name = 'glass'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['http://www.glassesshop.com/bestsellers/']

    def parse(self, response):
        glass = response.xpath("//div[@id='product-lists']/div")
        for a in glass:
            # url = a.xpath(".//div[4]/div[2]//a/@href").get()
            # image = a.xpath(".//div[3]//@src").get()
            # name = a.xpath("normalize_space(.//div[4]/div[2]//a/text())").get()
            # price = a.xpath(".//div[@class='p-price']//span/text()").get()
            yield{
                'product name': a.xpath("normalize-space(.//div[4]/div[2]//a/text())").get(),
                'product url': a.xpath(".//div[4]/div[2]//a/@href").get(),
                'product image link': a.xpath(".//div[3]//@src").get(),
                'product price': a.xpath(".//div[@class='p-price']//span/text()").get()

            }

        next_page = response.xpath("//ul[@class='pagination']/li[6]/a/@href").get()

        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
