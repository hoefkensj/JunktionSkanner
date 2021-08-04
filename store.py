import configparser
import os

# app_name = "testapp"
# config_folder = os.path.join(os.path.expanduser("~"), '.config', app_name)


config_folder = "."
os.makedirs(config_folder, exist_ok=True)
ini_file = "store.ini"


def read_config(file):
	junktion_lib = {}
	config = configparser.ConfigParser()
	config.read(file)
	
	if config.has_section('JUNKTIONS'):
		for key in list(config['JUNKTIONS'].keys()):
			junktion_lib[key] = config['JUNKTIONS'][key]
	# print(junktion_lib)
	for key in list(junktion_lib.keys()):
		print(key, "\t\t\t", junktion_lib[key])
		val = junktion_lib.get(key)
		print(list(val))
		print(val)
		for item in val:
			print("\n", item)
	
	return junktion_lib


def new_entry(config, pair):
	pass


if __name__ == "__main__":
	read_config(ini_file)
