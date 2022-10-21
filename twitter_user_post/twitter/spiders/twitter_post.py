import scrapy
import json
from twitter.twapi import get_api
from twitter.items import TwitterItem

class TwpostSpider(scrapy.Spider):
    name = 'twitter_user_post'
    allowed_domains = ['twitter.com']
    start_urls = ['https://twitter.com']

    def __init__(self, user_id='', screen_name='', count=200, since_id='', max_id='', *args, **kwargs):
        super().__init__(*args, ** kwargs)
        self.param = dict(user_id = user_id, screen_name = screen_name, count = count, since_id = since_id, max_id = max_id)

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], body=json.dumps(self.param))

    def parse(self, response):
        res = json.loads(response.body)

        items =[]
        results = json.loads(response.body)
        for res in results :
            item = TwitterItem()
            item['id'] = res.get('id_str')
            item['full_text'] = res.get('full_text')
            item['truncated'] = res.get('truncated')
            item['display_text_range'] = res.get('display_text_range')
            item['source'] = res.get('source')
            item['in_reply_to_status_id'] = res.get('in_reply_to_status_id_str')
            item['in_reply_to_user_id'] = res.get('in_reply_to_user_id_str')
            item['in_reply_to_screen_name'] = res.get('in_reply_to_screen_name')
            item['user_id'] = res.get('user').get('id_str')
            item['username'] = res.get('user').get('name')
            item['screen_name'] = res.get('user').get('screen_name')
            item['geo'] = res.get('geo')
            item['coordinates'] = res.get('coordinates')
            item['place'] = res.get('place')
            item['contributors'] = res.get('contributors')
            item['is_quote_status'] = res.get('is_quote_status')
            item['retweet_count'] = res.get('retweet_count')
            item['favorite_count'] = res.get('favorite_count')
            item['reply_count'] = res.get('reply_count')
            item['quote_count'] = res.get('quote_count')
            item['favorited'] = res.get('favorited')
            item['retweeted'] = res.get('retweeted')
            item['lang'] = res.get('lang')
            item['created_at'] = res.get('created_at')
            items.append(item)
        return items

