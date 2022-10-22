# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import json
from scrapy import signals
from scrapy.http import TextResponse
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from twitter.twapi import get_api

class TwitterSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class TwitterDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    def __init__(self):
        self.api = get_api({})

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called

        param = json.loads(request.body)

        tweets = []
        params = self.api.get_params({"count": param["count"]})
        if param["user_id"]:
            params["user_id"] = param["user_id"]
        elif param["screen_name"]:
            params["screen_name"] = param["screen_name"]
        else:
            raise TwitterError(f"user_id and screen_name are both null")

        while len(tweets) < int(params["count"]):
            if param["since_id"]:
                params["since_id"] = param["since_id"]
            elif param["max_id"]:
                params["max_id"] = param["max_id"]

            data = self.api.req_twitter(url="https://api.twitter.com/1.1/statuses/user_timeline.json", params=params)
            tweets = tweets + data
            # 如果没有新数据了 直接返回
            if len(data) <= 1:
                break
            # 获取一下下一页的游标
            max_id = data[-1]["id_str"]

        # 过滤掉翻页时断点处产生的重复推文
        tweet_ids = set()
        for tweet in tweets:
            tweet_id = tweet["id_str"]
            if tweet_id in tweet_ids:
                tweets.remove(tweet)
            else:
                tweet_ids.add(tweet_id)
        return TextResponse(url=request.url, body=json.dumps(tweets), encoding='utf8')

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
