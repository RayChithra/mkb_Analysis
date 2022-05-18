import scrapy
import re
import csv

class ScrapeArticleSpider(scrapy.Spider):
    name = "get_urls"

    def start_requests(self):
        url = "https://www.pmindia.gov.in/en/mann-ki-baat/"

        yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):

        urls = []
        urls = response.xpath("//a[@class='bttn more-info sound-cloud-mann-ki-baat-read btn btn-primary btn-lg']/@href").extract()

        print(urls)

        # for url in urls:
        #     with open("/home/raychithra/SEM_6/Hons_II/speeches/bjp_speeches/all_urls_2.txt", "w") as f:
        #         f.write(url + "\n")
