import os
import pickle
import win32api
from multiprocessing import Process
from os import readlink
from sys import stdout

storefile = '.\\store.bin'


def jlnk(path: str) -> bool:
	try:
		return bool(readlink(path))
	except OSError:
		return False


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
			is_jlnk = jlnk(current)
			if is_jlnk:
				callback_new(current)
				continue
		except OSError:
			pass


# from win32api import GetLogicalDriveStrings
def new_junction(path):
	pair = {get_src(path): path(path)}
	return pair


def sign(path):
	if os.path.exists(path):
		symbol = "<-"
	else:
		symbol = "(dead link)"
	return symbol


def prt_line(junktion, tabs=20):
	line = '{src}{sp1}{sign}{sp2}{lnk}'.format(src=list(junktion.keys())[0],
											   sp1='\t' * (tabs - ln_src(list(junktion.keys())[0])),
											   sp2='\t' * 5,
											   sign=sign(list(junktion.keys())[0]),
											   lnk=junktion[list(junktion.keys())[0]])
	return line


def get_drvs():
	drives = win32api.GetLogicalDriveStrings()
	drives = drives.split('\000')[:-1]
	return drives


def get_src(pth):
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


def store_key(store, key, value=[]):
	myval = value
	if key in store:
		myval = store[key]
	else:
		pass
	value = myval
	return value


def do_store(path):
	with open(path, 'rb') as storage:
		data = storage.read()
		store = pickle.loads(data)
	return store


def helpme(text):
	# txt =str(text)
	print(text)


def callback_dir(dir):
	write_over(path(dir))


def callback_new(dir):
	junction = new_junction(dir)
	store = do_store(storefile)
	value = store_key(store, list(junction.keys())[0])
	value.append(junction[list(junction.keys())[0]])
	store[list(junction.keys())[0]] = value
	save(storefile, store)
	write_new(prt_line(junction))


def new(link):
	lnk = path(link)
	src = get_src(link)
	junction = {src: lnk}
	return junction


def main():
	drvs = get_drvs()
	write_new(drvs)
	for drive in drvs:
		
		proc = Process(
				target=walk,
				args=(drive, callback_dir, callback_new))
		
		proc.start(), proc.join()
		if proc.exitcode == 0:
			continue


if __name__ == '__main__':
	main()

# drvs = ['A:\\', ] #temp

# Jnktions = {}
# Jnktions["C:\\_examplefolder_\\"] = ["D:\\junction1_examplefolder","E:\\junction1_examplefolder"]

# dir = '.\\7-Zip\\'

# if is_junction(dir):
#	print('\nPoints to:', os.readlink(dir))
#
# for currentpath, folders, files in os.walk('..'):
# 	#print(currentpath, folders, files)
# 	print (currentpath)
# 	if is_junction(currentpath):
# 		junction = "{path} points to:	{dir}  ".format(path=currentpath, dir=os.readlink(currentpath))
# 		history.append(junction)
# 		print(str(junction))
# 	else:
# 		for found in history:
# 			print(found)
# 		print(currentpath)
# 		pyautogui.click(x = 999, y = 1075)
# 		pyautogui.hotkey('ctrl', ';')
# 		for found in history:
#	# 			print(found)
# p = Process(target = XmasLED, args = (OUTp,))
# p.start(), p.join()
# print(os.path.isdir(dir))
# print(os.path.isfile(dir))
# print(os.path.isabs(dir))
# print(os.path.islink(dir))
# print(os.path.ismount(dir))
# stat_info = os.lstat(dir)
# print('\nFile Permissions:', oct(stat_info.st_mode))
# print('\nPoints to:', os.readlink(dir))
# _winapi.CreateJunction(".\\test\\", ".\\Games\\")
