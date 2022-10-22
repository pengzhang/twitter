# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TwitterItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    tw_id	=	scrapy.Field()
    name	=	scrapy.Field()
    screenname	=	scrapy.Field()
    statuses_count	=	scrapy.Field()
    like_count	=	scrapy.Field()
    listed_count	=	scrapy.Field()
    head_url	=	scrapy.Field()
    visit_url	=	scrapy.Field()
    description	=	scrapy.Field()
    location	=	scrapy.Field()
    time_zone	=	scrapy.Field()
    verified	=	scrapy.Field()
    friends_count	=	scrapy.Field()
    follower_count	=	scrapy.Field()
    lang	=	scrapy.Field()
    media_count	=	scrapy.Field()
    following	=	scrapy.Field()
    is_translator	=	scrapy.Field()
    favourites_count	=	scrapy.Field()
    geo_enabled	=	scrapy.Field()
    contributors_enabled	=	scrapy.Field()
    created_at	=	scrapy.Field()
    fast_followers_count	=	scrapy.Field()
    normal_followers_count	=	scrapy.Field()
    profile_location	=	scrapy.Field()
