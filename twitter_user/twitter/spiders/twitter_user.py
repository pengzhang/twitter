import scrapy
import json
from twitter.twapi import get_api
from twitter.items import TwitterItem

class TwpostSpider(scrapy.Spider):
    name = 'twitter_user'
    allowed_domains = ['twitter.com']
    start_urls = ['https://twitter.com']

    def __init__(self, user_id='', screen_name='', *args, **kwargs):
        super().__init__(*args, ** kwargs)
        self.param = dict(user_id = user_id, screen_name = screen_name)

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls[0], body=json.dumps(self.param))

    def parse(self, response):
        res = json.loads(response.body)

        item = TwitterItem()
        item['tw_id'] = res.get('id_str')
        item['name'] = res.get('name')
        item['screenname'] = res.get('screen_name')
        item['statuses_count'] = res.get('statuses_count')
        item['like_count'] = res.get('')
        item['listed_count'] = res.get('listed_count')
        item['head_url'] = res.get('profile_image_url')
        item['visit_url'] = res.get('url')
        item['description'] = res.get('description')
        item['location'] = res.get('location')
        item['time_zone'] = res.get('time_zone')
        item['verified'] = res.get('verified')
        item['friends_count'] = res.get('friends_count')
        item['follower_count'] = res.get('followers_count')
        item['lang'] = res.get('lang')
        item['media_count'] = res.get('media_count')
        item['following'] = res.get('following')
        item['is_translator'] = res.get('is_translator')
        item['favourites_count'] = res.get('favourites_count')
        item['geo_enabled'] = res.get('geo_enabled')
        item['contributors_enabled'] = res.get('contributors_enabled')
        item['created_at'] = res.get('created_at')
        item['fast_followers_count'] = res.get('fast_followers_count')
        item['normal_followers_count'] = res.get('normal_followers_count')
        item['profile_location'] = res.get('profile_location')

        print(item)
        return item

