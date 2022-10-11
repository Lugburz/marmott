import markdown
import json
from os import listdir
import os
import codecs

# little trick for global file watcher
file_path = os.path.realpath(__file__)
dirname = os.path.dirname(file_path)
os.chdir(dirname)

# read raw_database.json to find "mkdw" and replace description with its computed html
# saves result as file "database.json"
with open('./raw_database.json', encoding='utf-8') as fh:
	data = json.load(fh)
	for comic in data['comics']:
		if 'mkdw' in comic:
			with open("src/assets/" + comic['mkdw'], encoding='utf-8') as fh_mkdw:
				comic['description'] = markdown.markdown( fh_mkdw.read() )
			comic.pop('mkdw')
	with codecs.open('src/assets/database.json', 'w', 'utf-8') as output:
		json_string = json.dumps(data, ensure_ascii=False)
		output.write(json_string)
		
# pfff  to improve so badly
	for comic in data['hentais']:
		if 'mkdw' in comic:
			with open("src/assets/" + comic['mkdw'], encoding='utf-8') as fh_mkdw:
				comic['description'] = markdown.markdown( fh_mkdw.read() )
			comic.pop('mkdw')
	with codecs.open('src/assets/database.json', 'w', 'utf-8') as output:
		json_string = json.dumps(data, ensure_ascii=False)
		output.write(json_string)