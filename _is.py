from os import readlink


def jlnk(path: str) -> bool:
	try:
		return bool(readlink(path))
	except OSError:
		return False
