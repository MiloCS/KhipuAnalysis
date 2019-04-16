import xlrd
import os, sys

def xlsx_to_row(filename):
	vals = []
	with xlrd.open_workbook(filename) as wb:
		sheet = wb.sheets()[0]
		vals = [x[1] for x in sheet.col_values(5) if not x == '']
	vals = vals[1:]
	#vals = [str(x)[0] for x in vals if not x == 0]
	return filename[:-5].split('\\')[-1] + ' ' + ' '.join(vals)


def process_dir(dirpath):
	files = os.listdir(dirpath)
	with open('table.txt', 'w+') as f:
		for file in files:
			f.write(xlsx_to_row(dirpath + '\\' + file) + '\n')

if __name__ == '__main__':
	process_dir(sys.argv[1])