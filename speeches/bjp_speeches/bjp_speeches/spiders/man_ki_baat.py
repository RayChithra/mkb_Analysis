import scrapy
import csv
import re

class ScrapeArticleSpider(scrapy.Spider):
    name = "get_mann_ki_baat"

    def start_requests(self):

        urls = []
        with open("all_urls.txt", "r") as f:
            urls = f.readlines()

        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)

    def parse(self, response):

        DELIM = '|'
        
        try:
            date = response.css("span.date ::text").get()
            speech = response.css("div.news-bg p::text").getall()

        except Exception as E:
            print("Cannot read from {url}\n")

        def clean(content):
            try:
                return re.sub(r"\s", " ", content).replace(DELIM, "")
            except:
                return ""
        
        date = clean(date)
        speech = " ".join([clean(x) for x in speech])

        with open("mann_ki_baat.csv", "a") as f:
            article_writer = csv.writer(f, delimiter=DELIM)
            # print(title + "\n")
            # print(date + "\n")
            article_writer.writerow([response.request.url, date, speech]
            )