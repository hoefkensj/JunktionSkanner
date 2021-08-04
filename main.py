import multiprocessing
import os
import pickle
import sys

import win32api

storefile = '.\\store.bin'


class junction:
	def __init__(self):
		self.src = ""
		self.links = []
		self.link = []
		self.dict = {}
		self.key = self.src
		self.val = self.links
		self.prtline = ""
		self.tabs = 20
		sp1 = '\t' * (tabs - get_lnsrc(junktion[0]))
	
	def src(pth):
		path = os.path.realpath(pth)
		return path
	
	def path(pth):  # src                                 = os.path.realpath(pth)
		path = os.path.abspath(pth)
		return path
	
	def lnsrc(pth):
		charsin = len(pth)
		# tchain                              = '\t\t\t\t'
		lnblk = int((charsin + (4 - (charsin % 4))) / 4)
		return lnblk
	
	def make(link):
		new = [get_src(link), get_path(link)]
		store_dict = get_store(storefile)
		junction = make_entry(get_store(storefile), new)
		store_dict[list(junction.keys())[0]] = junction[list(junction.keys())[0]]
		return (store_dict)
	
	def prtline(junktion, tabs):
		sp1 = '\t' * (tabs - get_lnsrc(junktion[0]))
		sp2 = '\t' * 5
		line = f'{junktion[0]}{sp1}{make_prtsign(junktion[0])}{sp2}{junktion[1]}'
		return line


def make_prtsign(path):
	if os.path.exists(path):
		symbol = "<-"
	else:
		symbol = "(dead link)"
	return symbol


def get_drives():
	drives = win32api.GetLogicalDriveStrings()
	drives = drives.split('\000')[: -1]
	return drives


def get_store(path):
	with open(path, 'rb') as storage:
		data = storage.read()
		store = pickle.loads(data)
	return store


def printout(tmp):
	do_writeover(get_path(tmp))


def make_entry(storedct, lst):
	key = lst[0]
	value = []
	# if key in storedct:
	# q	value = storedct[key]
	val = value.append(lst[1])
	entry = {f'{key}': f'{value}'}
	return entry


def is_jlnk(path: str) -> bool:
	try:
		return bool(os.readlink(path))
	except OSError:
		return False


def make_prtline(junktion, tabs=20):
	sp1 = '\t' * (tabs - get_lnsrc(junktion[0]))
	sp2 = '\t' * 5
	line = f'{junktion[0]}{sp1}{make_prtsign(junktion[0])}{sp2}{junktion[1]}'
	return line


def do_writeout(line, action):
	switch = {
			"over": f'\r\r\r{line}\n',
			"new" : f'\r\r{line}'
			}
	sys.stdout.write(switch.get(action))


def do_save(storage, store):
	with open(storage, "wb") as binstore:
		pickle.dump(store, binstore)


def walk(drives, callback):
	for drive in drives:
		for current, folder, file in os.walk(drive, topdown=True):
			callback(current)


def hit(link):
	item = junction(link)
	do_save(storefile, item.make(link))
	do_writeout(make_prtline([item.src(link), item.path(link)]), "new")


def test(path):
	if is_jlnk(path):
		hit(path)
	return


def main():
	all_drives = get_drives()
	do_writeout(all_drives, "new")
	
	proc = multiprocessing.Process(target=walk, args=(all_drives, test))
	proc.start(), proc.join()
	# with concurrent.futures.ProcessPoolExecutor() as proc:
	# 	walk =  proc.submit(do_walk, all_drives, callback)
	#
	# 	if walk.done():
	# 		do_writenew("finished scanning drives.")
	
	userinput = input("\n\n\nenter Q to quit:")
	
	if ("q" in userinput) | (proc.exitcode == 0):
		do_writeout("Quitting ...", "new")


if __name__ == '__main__':
	main()
