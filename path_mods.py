import os

from win32api import GetLogicalDriveStrings


def is_jlnk(path: str) -> bool:
	try:
		return bool(os.readlink(path))
	except OSError:
		return False


def drvs():
	drvs = GetLogicalDriveStrings()
	drvs = drvs.split('\000')[:-1]
	return drvs


def abss(pth):
	jlink = os.path.abspath(pth)
	src = os.readlink(pth)
	# print(jlink, "->" , target)
	return src, jlink
