import requests
import os, sys, re
from bs4 import BeautifulSoup

def fetch_to_dir(dirname, links):
	#check input directory existence
	if not os.path.exists(dirname):
		os.makedirs(dirname)

	for url_pair in links:
		if (url_pair[0][-1] == 's'):
			continue
		r = requests.get(url_pair[0], allow_redirects=True)
		ext = '.xlsx'
		with open(dirname + '\\' + url_pair[1].replace(' ', '_') + ext, 'wb') as f:
			f.write(r.content)

def is_valid_row(row):
	row_soup = BeautifulSoup(str(row), 'html.parser')
	elems = row_soup.find_all('td')
	if len(elems) > 0 and re.match('UR*', elems[0].get_text()):
		return True
	return False

def get_link(row):
	row_soup = BeautifulSoup(str(row), 'html.parser')
	elems = row_soup.find_all('td')
	result = None
	try:
		result = str(elems[1]).split('"')[3]
		return result
	except:
		return result

def get_row_name(row):
	row_soup = BeautifulSoup(str(row), 'html.parser')
	elems = row_soup.find_all('td')
	return elems[0].get_text()

def collect_data_links():
	r = requests.get('https://khipukamayuq.fas.harvard.edu/DataTables.html')
	#parsing html data and gathering data links
	mysoup = BeautifulSoup(r.content, 'html.parser')
	table_list = mysoup.find_all('table', {'summary':'Table for links to UR data tables'})
	result = []
	for table in table_list:
		table_soup = BeautifulSoup(str(table), 'html.parser')
		rows = table_soup.find_all('tr')
		rows = [(r, get_row_name(r)) for r in rows if is_valid_row(r)]
		result += rows
	filtered_result = []
	for i in result:
		l = get_link(i[0])
		if l is not None:
			filtered_result.append(('https://khipukamayuq.fas.harvard.edu/' + l.replace('&lt;', '<'), i[1]))
	#['https://khipukamayuq.fas.harvard.edu/' + get_link(x) for x in result]
	return filtered_result

if __name__ == '__main__':

	fetch_to_dir(sys.argv[1], collect_data_links())