import json
	
if __name__=='__main__':
	
	ids = []
	with open('response.json', 'r') as f :
		data = json.load(f)
		for dt in data["data"] : 
			ids.append(dt['_id'])
			print(dt['_id'])
		f.close()
		
	with open('tasks.txt', 'w') as ft :
		for idstr in ids :
			ft.write(idstr + "\n")
		ft.close()
