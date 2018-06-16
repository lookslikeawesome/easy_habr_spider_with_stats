# -*- coding: utf-8 -*-
import scrapy

class HabrSpider(scrapy.Spider):
    name = 'habr'

    # Так же можно спарсить любые другие статьи хабра не зависимо от хабов, тегов и т.д
    # Достаточно лишь в переменной allowed_domains вместо первого аргумента словаря,
    # Указать необходимую ссылку для парсинга. А вторую оставить как есть. Это важно.
    # Так-же, в переменной start_urls ссылку следует заменить.
    # Обратите внимание на присутствие и отсутствие http протокола в обеих переменных.

    allowed_domains = ['habr.com/hub/python', 'habr.com']
    start_urls = ['http://habr.com/hub/python']

    def parse(self, response):
        posts = response.xpath('//*[@class="post post_preview"]')
        for post in posts:
            author = post.xpath('.//*[@class="user-info__nickname user-info__nickname_small"]/text()').extract_first()
            author_url = post.xpath('.//*[@class="post__meta"]/a/@href').extract_first()

            scrapy.Request(author_url)
            user = response.xpath('//*[@class="media-obj__body media-obj__body_user-info"]')

            title = post.xpath('.//*[@class="post__title_link"]/text()').extract_first()
            tags_block = post.xpath('.//*[@class="post__hubs inline-list"]')
            tags = tags_block.xpath('.//*[@class="inline-list__item inline-list__item_hub"]/a/text()').extract()

            post_stats = post.xpath('.//*[@class="voting-wjt__counter voting-wjt__counter_positive  js-score"]/text()').extract_first()
            bookmarks = post.xpath('.//*[@class="bookmark__counter js-favs_count"]/text()').extract_first()
            views = post.xpath('.//*[@class="post-stats__views-count"]/text()').extract_first()
            comments = post.xpath('.//*[@class="post-stats__comments-count"]/text()').extract_first()

            data = {
                'Author': author,
                'Title': title,
                'Tags': tags,
                'Post stats': post_stats,
                'Bookmarks': bookmarks,
                'Views': views,
                'Comments': comments
            }

            yield data

        next_page_url = response.xpath('//*[@class="arrows-pagination__item-link arrows-pagination__item-link_next"]/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url, callback=self.parse)
