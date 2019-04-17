import xlrd
import os, sys

def xlsx_to_row(filename):
	vals = []
	with xlrd.open_workbook(filename) as wb:
		if filename[-1] == 's':
			sheet = wb.sheets()[1]
			vals = [str(x)[0] for x in sheet.col_values(3) if not x == '']
			vals = vals[7:]
		else:
			sheet = wb.sheets()[0]
			vals = [str(x)[1] for x in sheet.col_values(5) if not x == '']
			vals = vals[1:]
			
		
	#vals = [str(x)[0] for x in vals if not x == 0]
	ext_length = 5 if filename[-1] == 'x' else 4
	return filename[:-ext_length].split('\\')[-1] + ' ' + ' '.join(vals)


def process_dir(dirpath):
	files = os.listdir(dirpath)
	with open('table.txt', 'w+') as f:
		for file in files:
			f.write(xlsx_to_row(dirpath + '\\' + file) + '\n')

if __name__ == '__main__':
	process_dir(sys.argv[1])