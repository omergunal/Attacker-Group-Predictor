from bs4 import BeautifulSoup
import requests
import re
import os


f = open('groupNames.txt')
contents = f.read()
groups = contents.splitlines()
data = {}

for group in groups:
	groupName = group.split(",")[0]
	groupID = group.split(",")[1]
	data[groupName] = {}
	data[groupName]["techniques"] = []
	url = "https://attack.mitre.org/groups/" + groupID
	r = requests.get(url)
	source = BeautifulSoup(r.content,"lxml")
	for link in source.findAll('a'):
		if "software" in str(link):
			string = str(link.string).replace(",","")
			data[groupName]["techniques"].append(string)
		if "techniques" in str(link):
			string = str(link.string).replace(",","")
			data[groupName]["techniques"].append(string)


cur_path = os.path.dirname(__file__)

new_path = os.path.relpath('../groupInfo.txt', cur_path)
with open(new_path, 'w') as f:
    f.write(str(data))
f.close()
