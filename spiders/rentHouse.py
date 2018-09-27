import scrapy
from ..items import RenthouseItem


class rentHouseSpider(scrapy.Spider):
  name = "rent"
  start_urls = ['https://rent.591.com.tw/?kind=2&mrtline=100&region=1&mrt=1&rentprice=2&area=0,10&hasimg=1&not_cover=1&floor=2,6&order=nearby&orderType=desc&mrtcoods=4185,4187,4186,4188,4189']

  def parse(self, response):
    print(response)
    rH = RenthouseItem()
    title_list = response.xpath('//ul[@class="listInfo clearfix "]/li[2]/h3/a/text()').extract()
    money_list = response.xpath('//ul[@class="listInfo clearfix "]/div/i/text()').extract()
    for i, j in zip(title_list, money_list):
      rH['title'] = i
      rH['money'] = j
      yield rH
      # print(i,":", j)
