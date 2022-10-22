import requests

def get_user_info(user_id):
	url = "http://10.103.2.18/api/tasks/run"
	payload='{  "spider_id": "635373f41bd6764e147ead98",  "cmd": "scrapy crawl twitter_user",  "param": "-a user_id=\'' + user_id +'\'",  "mode": "random",  "priority": 1}'
	headers = {
	  'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYzMzJhYmY5Yzk5M2IxYmM1ZWFkYWMzNiIsIm5iZiI6MTY2NjQxMzk1MSwidXNlcm5hbWUiOiJhZG1pbiJ9.LLJzwGk7CeydeDjiyztuP4QV7O62Z9Yn3nPMblCRkOQ',
	  'Content-Type': 'application/json'
	}
	print(payload)
	response = requests.request("POST", url, headers=headers, data=payload)
	print(response.text)
	
if __name__=='__main__':
	f = open("user_ids.txt", 'r')
	for user_id in f.readlines():
		print(user_id)
		get_user_info(user_id.strip())





