import logging
import csv
import re

def clean_lineup(lineup):
	lineup = {
		'QB': '',
		'RB1:': '',
		'RB2:': '',
		'WR1': '',
		'WR2:': '',
		'WR3:': '',
		'TE:': '',
		'FLEX:': '',
		'DST:': '',
	}


def load_data(file):
	with open('week4_results.csv') as csv_file:
	    csv_reader = csv.reader(csv_file, delimiter=',')
	    line_count = 0
	    for row in csv_reader:
	        if line_count == 0:
	        	print row
	        elif line_count == 1:
	        	for column in row:
	        		print column
	        	# clean_lineup(row)

	        line_count += 1
	        #     print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
	        #     line_count += 1

load_data('week4_results.csv')