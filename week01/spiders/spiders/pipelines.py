# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pandas


class SpidersPipeline:

    def process_item(self, item, spider):
        name = item['name']
        link = item['link']
        tag = item['tag']
        time = item['time']
        output = [f'name: {name.strip()} tag: {tag.strip()} time: {time.strip()} link: {link.strip()}']
        movie = pandas.DataFrame(data=output)
        movie.to_csv('../movie2.csv', mode='a', index=False, encoding='utf8')
        return item
