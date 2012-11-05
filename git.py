#!C:\Python26 python

import os
import sys
import glob
import shutil

def removeExceptGit(pathDir):
	originalDirectory = os.getcwd() #Directorio original raiz del script
	fileList = os.listdir(pathDir)
	os.chdir(pathDir)
	
	for i in fileList:
		if i != '.git':
			if os.path.isdir(i):
				shutil.rmtree(i)
			else:
				os.remove(i)
	os.chdir(originalDirectory)

originalDirectory = os.getcwd() #Directorio original raiz del script

i = {}
projectVssGit = 'test1Git'
commentGit = "Testeando el comentario"
commentGit = commentGit.replace(' ', '-')
i['user'] = 'victor'
i['date'] = '2012-11-03'
i['time'] = '15:45'
i['label'] = 'label_test'

print i

pathExeGit = "C:/Archivos de programa/Git/bin/git.exe" #Ejecutable Git
nameProjectGitGenerate = 'test1GIT'


listVersions = ['0', '1', '2']
count = 0
for ii in listVersions:
	checkGit = 'check-git-' + str(count)
	os.chdir(nameProjectGitGenerate)
	f = open(checkGit, 'w')
	f.close()
	
	userGit = i['user'] + '@' + projectVssGit
	os.system('"' + pathExeGit + '" config --global user.email ' + i['user'] + '@' + projectVssGit)
	os.system('"' + pathExeGit + '" config --global user.name ' + i['user'])
	os.system('"' + pathExeGit + '" add .')
	os.system(r'"' + pathExeGit + '" commit -m ' + commentGit + ' --date=2012-11-03;15:41')
	
	os.remove(checkGit)
	
	#removeExceptGit(nameProjectGitGenerate)
	os.chdir(originalDirectory)
	count = count + 1

