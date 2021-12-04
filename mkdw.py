import markdown
import json
from os import listdir
import os
import codecs

# read raw_database.json to find "mkdw" and replace description with its computed html
# saves result as file "database.js"
with open('./raw_database.json', encoding='utf-8') as fh:
	data = json.load(fh)
	for comic in data['comics']:
		if 'mkdw' in comic:
			with open(comic['mkdw'], encoding='utf-8') as fh_mkdw:
				comic['description'] = markdown.markdown( fh_mkdw.read() )
			comic.pop('mkdw')
			#~ print(comic['mkdw'])
	with codecs.open('./database.js', 'w', 'utf-8') as output:
		json_string = json.dumps(data, ensure_ascii=False)
		output.write("var database = " + json_string)