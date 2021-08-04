import os
import pickle

import win32api


# from win32api import GetLogicalDriveStrings

def drvs():
	drives = win32api.GetLogicalDriveStrings()
	drives = drives.split('\000')[:-1]
	return drives


def src(pth):
	path = os.path.realpath(pth)
	return path


def path(pth):
	#	src = os.path.realpath(pth)
	path = os.path.abspath(pth)
	# tmp= '\\\\?\\{path}'.format(path=os.path.realpath(pth))
	return path


def ln_src(path):
	charsin = len(path)
	# tchain = '\t\t\t\t'
	lnblk = int((charsin + (4 - (charsin % 4))) / 4)
	return lnblk


def store_key(store, key):
	value = []
	if key in store:
		value = store[key]
	else:
		value = []
	return value


def store(path):
	with open(path, 'rb') as storage:
		data = storage.read()
		store = pickle.loads(data)
	return store


def helpme(text):
	# txt =str(text)
	print(text)


if __name__ == "__main__":
	store("store.bin")
