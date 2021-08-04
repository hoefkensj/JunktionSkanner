import os
import pickle
from sys import stdout

import _is


def write_over(line):
	stdout.write('\r{txt}'.format(txt=line))


def write_new(line):
	stdout.write('\r\r{txt}\n'.format(txt=line))


def save(storage, store):
	binstore = open(storage, "wb")
	pickle.dump(store, binstore)
	binstore.close()


def walk(drive, callback_tmp, callback_new):
	for current, folder, file in os.walk(drive, topdown=True):
		callback_tmp(current)
		
		try:
			is_jlnk = _is.jlnk(current)
			if is_jlnk:
				callback_new(current)
				continue
		except OSError:
			pass
