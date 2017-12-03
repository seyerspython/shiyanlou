

import scrapy

class GithubUserSpider(scrapy.Spider):

	name='github-user'


	@property
	def start_urls(self):
		url_tmp1='https://github.com/shiyanlou?page={}&tab=repositories'
		return (url_tmp1.format(i) for i in range(1,5))

	def parse(self,response):
		for li in response.xpath('//li[contains(@class,"border-bottom")]'):
			yield{
				'name':li.xpath('.//div[contains(@class,"d-inline-block")]/h3/a/text()').re_first('\s+(.+)'),
				'update_time':li.xpath('.//div[contains(@class,"text-gray mt-2")]/relative-time/@datetime').extract_first()
			}

