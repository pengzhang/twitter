import requests

def get_user_post(user_id):
	url = "http://twitter.hanyubook.com/api/tasks/run"
	payload='{  "spider_id": "6360a0073608b3c28665bcb1",  "cmd": "scrapy crawl twitter_user_post",  "param": "-a user_id=\'' + user_id +'\'",  "mode": "random",  "priority": 1}'
	headers = {
	  'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYzNWU0OTE5MzYwOGIzYzI4NjY1YmM1MSIsIm5iZiI6MTY2NzI3Njg3OCwidXNlcm5hbWUiOiJjcGphZG1pbiJ9.hupkSLIyZK6P67Zen6NIAZaBr_5MmqAre4KtUQ43mS0',
	  'Content-Type': 'application/json'
	}
	print(payload)
	response = requests.request("POST", url, headers=headers, data=payload)
	print(response.text)
	
if __name__=='__main__':
	f = open("user_ids.txt", 'r')
	for user_id in f.readlines():
		get_user_post(user_id.strip())





