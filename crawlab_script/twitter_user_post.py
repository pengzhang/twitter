import requests

def get_user_post(user_id):
	url = "http://vp99.hanyubook.com/api/tasks/run"
	payload='{  "spider_id": "6354f349145b0fb3bbda1b21",  "cmd": "scrapy crawl twitter_user_post",  "param": "-a user_id=\'' + user_id +'\'",  "mode": "random",  "priority": 1}'
	headers = {
	  'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYzNTRlMThiOTJjYjMzYTQ3NTYyN2NiOCIsIm5iZiI6MTY2NjUwOTEwMywidXNlcm5hbWUiOiJhZG1pbiJ9.TS4Et58xSlpMI8gGeX2J-elhpKSlhs2w8n25D0zXBNo',
	  'Content-Type': 'application/json'
	}
	print(payload)
	response = requests.request("POST", url, headers=headers, data=payload)
	print(response.text)
	
if __name__=='__main__':
	f = open("user_ids.txt", 'r')
	for user_id in f.readlines():
		get_user_post(user_id.strip())





