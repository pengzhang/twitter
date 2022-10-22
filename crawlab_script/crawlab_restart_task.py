import requests

def crawlab_restart_task(task_id):
	print('task id: ' + task_id)
	url = "http://10.103.2.18/api/tasks/" + task_id + "/restart"
	headers = {
	  'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYzMzJhYmY5Yzk5M2IxYmM1ZWFkYWMzNiIsIm5iZiI6MTY2NjQxMzk1MSwidXNlcm5hbWUiOiJhZG1pbiJ9.LLJzwGk7CeydeDjiyztuP4QV7O62Z9Yn3nPMblCRkOQ',
	  'Content-Type': 'application/json'
	}
	response = requests.request("POST", url, headers=headers)
	print(response.text)
	
if __name__=='__main__':
	f = open("tasks.txt", 'r')
	for task_id in f.readlines():
		crawlab_restart_task(task_id.strip())





