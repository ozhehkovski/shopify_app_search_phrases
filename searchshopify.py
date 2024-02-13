import scrapy
import json
from rustore.items import ShopItem


class SearchshopifySpider(scrapy.Spider):
    name = "searchshopify"

    urls = []
    for letter1 in "abcdefghijklmnopqrstuvwxyz":
        for letter2 in "abcdefghijklmnopqrstuvwxyz":
            for letter3 in "abcdefghijklmnopqrstuvwxyz":
                query = letter1 + letter2 + letter3
                urls.append(f"https://apps.shopify.com/search/autocomplete?v=3&q={query}&st_source=autocomplete")
    start_urls = urls


    def parse(self, response):
        data = json.loads(response.text)
        for s in data["searches"]:
            item = ShopItem()
            item["name"] = s["name"]
            yield item
