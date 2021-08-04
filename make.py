import os

import get


def new_junction(path):
	pair = {get.src(path): get.path(path)}
	return pair


def sign(path):
	if os.path.exists(path):
		symbol = "<-"
	else:
		symbol = "(dead link)"
	return symbol


def prt_line(junktion, tabs=20):
	line = '{src}{sp1}{sign}{sp2}{lnk}'.format(src=list(junktion.keys())[0],
											   sp1='\t' * (tabs - get.ln_src(list(junktion.keys())[0])),
											   sp2='\t' * 5,
											   sign=sign(list(junktion.keys())[0]),
											   lnk=junktion[list(junktion.keys())[0]])
	return line
