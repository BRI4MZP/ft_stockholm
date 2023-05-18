import argparse, sys, os
from pathlib import Path

mainDir = str(Path.home()) + "/infection"

def getArgs():
	getter = argparse.ArgumentParser(description="wanacry malware tool")
	getter.add_argument('-v', '--version',action='store_true', help='version')
	getter.add_argument('-s', '--silent', action='store_true', help='silent mode')
	getter.add_argument('-r', '--reverse', type=str, help='reverse mode')
	getter.add_argument('-p', '--path', default=mainDir, help='port')
	return(getter.parse_args())

def ft_stockholm():
	args = getArgs()
	if args.version:
		quit('version 1.0.1 (c) 2023')
	print(os.listdir(args.path))
	

if __name__ == '__main__':
	ft_stockholm()

