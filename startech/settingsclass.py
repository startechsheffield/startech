from os.path import exists
from startech.generalclass import checkToken, alignList
def __convert__(val):
	val = val.replace("\n","")
	if val.lower() == "false":
		return(False)
	elif val.lower() == "true":
		return(True)
	try:
		return(int(val))
	except:
		return(val)
def getList(tkn):
	if checkToken(tkn,True) == False:
		return([])
	try:
		f = open("/usr/share/stech/api/reg_"+tkn+".txt","r")
		lines = f.readlines()
		f.close()
	except:
		return([])
	olist = []
	for l in range(len(lines)):
		if not lines[l].find("#") == 0:
			olist.append(lines[l].split(" : ")[0])
	return(olist)
def get(tkn,ttl,sf=False):
	if checkToken(tkn,True) == False or not type(tkn) == str or not type(ttl) == str:
		return([])
	if not type(sf) == bool:
		sf = False
	try:
		f = open("/usr/share/stech/api/reg_"+tkn+".txt","r")
		lines = f.readlines()
		f.close()
	except:
		return([])
	for l in range(len(lines)):
		if not lines[l].find("#") == 0 and lines[l].split(" : ")[0] == ttl:
			if sf == False:
				return(__convert__(lines[l].split(" : ")[1]))
			return(lines[l].split(" : ")[1])
	return("")
def set(tkn,ttl,val):
	if checkToken(tkn,True) == False or not type(ttl) == str:
		return(False)
	if not (type(val) == str or type(val) == int or type(val) == bool):
		return(False)
	if exists("/usr/share/stech/api/reg_"+tkn+".txt") == False:
		try:
			f = open("/usr/share/stech/api/reg_"+tkn+".txt","w")
			f.write("# Please try to avoid editing this file manually if possible.\n")
			f.write("# 'stech-manager --config NAME=VALUE' edits these files.\n")
			f.write(ttl+" : "+str(val)+"\n")
			f.close()
			return(True)
		except:
			return(False)
	try:
		f = open("/usr/share/stech/api/reg_"+tkn+".txt","r")
		lines = f.readlines()
		f.close()
	except:
		return(False)
	found = False
	for l in range(len(lines)):
		if not lines[l].find("#") == 0 and lines[l].split(" : ")[0] == ttl:
			found = True
			lines[l] = ttl+" : "+str(val)+"\n"
			break
	if found == False:
		lines.append(ttl+" : "+str(val)+"\n")
	try:
		f = open("/usr/share/stech/api/reg_"+tkn+".txt","w")
		f.writelines(lines)
		f.close()
	except:
		return(False)
	return(True)
def unset(tkn,ttl):
	if checkToken(tkn,True) == False or not type(ttl) == str:
		return(False)
	try:
		f = open("/usr/share/stech/api/reg_"+tkn+".txt","r")
		lines = f.readlines()
		f.close()
	except:
		return(False)
	for l in range(len(lines)):
		if not lines[l].find("#") == 0 and lines[l].split(" : ")[0] == ttl:
			lines[l] == ""
			break
	lines = alignList(lines)
	try:
		f = open("/usr/share/stech/api/reg_"+tkn+".txt","w")
		f.writelines(lines)
		f.close()
		return(True)
	except:
		return(False)
def unsetAll(tkn):
	if checkToken(tkn,True) == False:
		return(False)
	lst = getList(tkn)
	if lst == []:
		return(False)
	for s in range(len(lst)):
		if unset(tkn,lst[s]) == False:
			return(False)
	return(True)