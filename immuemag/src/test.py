import json
import os

jsondata = open("data.js").read()
jsonload = json.loads(jsondata)


for num in range(len(jsonload)):
	for file in os.listdir(jsonload[num]['src']):
		if 'jpg' in file:
			os.rename(os.path.join(jsonload[num]['src']+"/",file),jsonload[num]['src']+"/index.jpg")


