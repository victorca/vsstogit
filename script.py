#!C:\Python26 python

import os
import sys
import glob
import shutil

##Bloque para introducir variables##########
formatDate = '/' #Ejemplo si el formato de fechas fuera 2/11/12
print "Formato de Fecha: " + formatDate + " Ejemplo: 2/11/12"
 
formatHour = ':' #Ejemplo si el formato de hora fuera 14:06
print "Formato de Horas: " + formatHour + " Ejemplo: 14:06"

pathExeGit = "C:/Archivos de programa/Git/bin/git.exe" #Ejecutable Git
print "Camino al ejecutable GIT: " + pathExeGit
##FIN Bloque para introducir variables##########

##Bloque para introducir datos##############
print "Se asume: C:\Archivos de programa\Microsoft Visual SourceSafe"
pathVss = str(raw_input("Directorio VSS (PATH):"))

print "Introducir proyecto, no es necesario incorporar el prefijo $/"
projectVss = str(raw_input("Proyecto a Migrar: $/"))
projectVssGit = projectVss #Variable para crear repo GIT para que no salga $/<repoGit>

originalDirectory = os.getcwd() #Directorio original raiz del script
##Fin Bloque para introducir datos##############

##Bloque para comprobar la validez de los datos introducidos por el usuario###########
if pathVss == '':
  pathVss = "C:\Archivos de programa\Microsoft Visual SourceSafe"

if projectVss == '':
  print "ERROR: Debe introducir el nombre del proyecto a migrar"
  print "Cerrando script"
  sys.exit()

if projectVss.find('$/') == -1:
  projectVss = '$/' + projectVss
##FIN Bloque para comprobar la validez de los datos introducidos por el usuario###########

##Bloque para establecer las variables de ambiente con las que trabajar############

#set PATH=C:\Archivos de programa\Microsoft Visual SourceSafe
#set SSDIR=C:\Documents and Settings\victor\Escritorio\newDB
#set SSUSER=victor
#set SSPWD=victor
##FIN Bloque para establecer las variables de ambiente con las que trabajar############

##Bloque de Funciones para Utilizar###############################################

#Function para de una lista eliminar todos los valores que queremos que tenga, 
#por ejemplo si tenemos la lista ['1', '', '2', '3', '', ''] y queremos que se 
#eliminen todos los valores '' y que quede ['1', '2', '3'] entonces
#listParser: es la lista
#varReject: esel valor a desechar
def retireOfList(listParser, varReject):
	result = []
	for i in listParser:
		if i != varReject:
			result.append(i)
	return result

	
#Function para copiar todos los ficheros y archivos de un directorio a otro
#En este caso cuandos se obtenga(get) en la carpeta 'tmp' una version se copiara para
#la carpeta de git todo su contenido y luego se dara commit
def copyInTo(dirIn, dirOut):
	fileList = os.listdir(dirIn)  
	dest = dirOut 
	for i in fileList:  
		src = dirIn + '/' + i  
		shutil.move(src,dest)

#Function para remover dentro de una carpeta todo menos la carpeta .git
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

##FIN Bloque de Funciones para Utilizar###############################################

#Camino al ejecutable C:\Archivos de programa\Microsoft Visual SourceSafe\ss.exe de VSS
comandSS = pathVss + '\ss.exe' #Queda por ejemplo: "C:\Archivos de programa\Microsoft Visual SourceSafe\ss.exe"
print "Camino al ejecutable VSS: " + comandSS

#Obtener todo el historial y ponerlo en el fichero outHistoryComplete
os.system('"' + comandSS + '"' + ' history ' + projectVss + ' -R > outHistoryComplete')
print "Obtenido Historial del Proyecto: " + projectVss

#Obtener en forma de string todo el historial para obtener la cantidad de versiones
f = open('outHistoryComplete', 'r')
historyComplete = f.read() #Leer todo el historial
f.close()

#Obtener en una lista cada linea del historial
f = open('outHistoryComplete', 'r')
historyCompleteReadlines = f.readlines() #Leer todo el historial pero por lineas
f.close()

countVersions = historyComplete.count('User:') #Cantidad de versiones que tiene el proyecto
print "Obteniendo cantidad de versiones de VSS para migrar a GIT: "

nameProjectGitGenerate = projectVssGit + 'GIT'
print "Creando nombre de Proyecto GIT: " + nameProjectGitGenerate

#Crear repositorio GIT con nombre del proyecto pasado por el usuario
os.system('"' + pathExeGit + '" init ' + nameProjectGitGenerate)
print "Creado repositorio GIT: " + nameProjectGitGenerate

##Bloque Obtener lista de Diccionarios, cada diccionario es una version VSS del proyecto#############
listVersions = [] #Lista de Diccionarios, cada Diccionario sera los datos de una version
verbose = '--'
listLabels = []
countLabels = 0
listLabelComment = []
countLabelComment = -1
listComments = []
countComments = -1
for i in historyCompleteReadlines:
	dictionary = {} #Se inicializa el diccionario
	dictionary['label'] = ''
	dictionary['label_comment'] = ''
	dictionary['comment'] = ''
	dictionaryComment = {}
	dictionaryLabelComment = {}
	dictionaryLabel = {}
	if i != '\r\n' or i.count('*') == 0: #Si no es linea en blanco ni * entonces son datos a guardar
		if i.count('Label:') > 0:
			splitFragment = i.split(':')
			if len(splitFragment) > 1 and splitFragment[1] != ' ':
				splitFragment = i.split('"')
				dictionaryLabel['index'] = countLabels
				dictionaryLabel['label'] = splitFragment[1]
				print dictionaryLabel['index']
				print dictionaryLabel['label']
				listLabels.append(dictionaryLabel)
		if i.count('Label comment:') > 0:
			splitFragment = i.split(':')
			if len(splitFragment) > 1 and splitFragment[1] != ' ':
				dictionaryLabelComment['index'] = countLabelComment
				dictionaryLabelComment['label_comment'] = splitFragment[1]
				listLabelComment.append(dictionaryLabelComment)
		if i.count('Comment:') > 0:
			splitFragment = i.split(':')
			if len(splitFragment) > 1 and splitFragment[1] != ' ':
				dictionaryComment['index'] = countComments
				dictionaryComment['comment'] = splitFragment[1]
				listComments.append(dictionaryComment)
		if i.count('User:') > 0:
			splitFragment = i.split(' ') #Realizar split a los espacios en blanco para obtener los elementos
			fragment = retireOfList(splitFragment, "") 
			dictionary['user'] = fragment[1]
			dictionary['date'] = fragment[3]
			dictionary['dateGit'] = '20' + dictionary['date']
			dictionary['time'] = fragment[5]
			verbose = verbose + '--'
			print verbose
			listVersions.append(dictionary)
			countComments = countComments + 1
			countLabelComment = countLabelComment + 1
			countLabels = countLabels + 1
	
if len(listVersions) > 0:
	if len(listComments) > 0:
		del listComments[-1]
		for i in listComments:
			listVersions[i['index']]['comment'] = i['comment']
		
	if len(listLabelComment) > 0:
		del listLabelComment[-1]
		for i in listLabelComment:
			listVersions[i['index']]['label_comment'] = i['label_comment']
		
	if len(listLabels) > 0:
		for i in listLabels:
			listVersions[i['index']]['label'] = i['label']

	listVersions = listVersions[::-1] #Obtener la lista ordenada de menor a mayor, asi es el orden del historial
else:
	print "Error al parsear el historial de VSS"
	sys.exit()
##FIN Bloque Obtener lista de Diccionarios, cada diccionario es una version VSS del proyecto#############

toCountVersions = 0 #Contar las versiones por las que vaya el ciclo
for i in listVersions:
	if i['comment'] == '':
		commentGit = 'Ejecutado por ' + i['user'] + ' en la fecha ' + i['dateGit'] + '; ' + i['time'] 
	else:
		commentGit = i['comment']
	
	if i['label_comment'] != '':
		commentGit += ' ' + i['label_comment']
	commentGit = commentGit.replace(' ', '-')
	
	#createDir = 'tmp' + str(listVersions.index(i))
	checkGit = 'check-git-' + str(listVersions.index(i))
	#if len(glob.glob(createDir)) == 0:
	#if os.path.isdir(createDir):
	#	shutil.rmtree(createDir)
	#os.mkdir(createDir)
	print i
	os.chdir(nameProjectGitGenerate)
	f = open(checkGit, 'w')
	f.close()
	#os.system('"' + comandSS + '"' + ' history ' + projectVss + ' -R > outHistoryComplete')
	os.system('"' + comandSS + '"' + ' get ' + projectVss + ' -Vd' + i['dateGit'] + ';' + i['time'])
	
	#os.chdir(originalDirectory)
	#copyInTo(createDir, nameProjectGitGenerate)
	
	#os.chdir(nameProjectGitGenerate)
	#os.chdir(nameProjectGitGenerate)
	os.system('"' + pathExeGit + '" config --global user.email ' + i['user'] + '@' + projectVssGit)
	os.system('"' + pathExeGit + '" config --global user.name ' + i['user'])
	os.system('"' + pathExeGit + '" add .')
	os.system(r'"' + pathExeGit + '" commit -m ' + commentGit + ' --date=' + i['dateGit'] + ';' + i['time'])
	#os.system('"' + pathExeGit + '" config --global user.email victor@gmail.com')
	#os.system('"' + pathExeGit + '" config --global user.name victor')
	#os.system('"' + pathExeGit + '" add .')
	#os.system(r'"' + pathExeGit + '" commit -m candela')
	
	if i['label'] != '':
		os.system('"' + pathExeGit + '" tag ' + i['label'])
	
	os.remove(checkGit)
	#fileList = os.listdir(os.getcwd())
	#for i in fileList:
	#	if i != '.git':
	#		if os.path.isdir(i):
	#			shutil.rmtree(i)
	#		else:
	#			os.remove(i)
	
	#print '"' + pathExeGit + '" commit -m "Candela"'
	os.chdir(originalDirectory)
	#removeExceptGit(nameProjectGitGenerate) #Remover todo menos la carpeta .git
	#os.chdir(originalDirectory)
	
	#shutil.copytree(nameProjectGitGenerate + '/.git', '.git')
	#shutil.rmtree(nameProjectGitGenerate)
	#os.mkdir(nameProjectGitGenerate)
	#shutil.copytree('.git', nameProjectGitGenerate + '/.git')
	#sshutil.rmtree('.git')
	
	#os.chdir(originalDirectory)
	#shutil.rmtree(createDir)
	#os.remove(checkGit)
	#os.chdir(originalDirectory)
	#shutil.move(createDir + "/*", nameProjectGitGenerate)
	#os.chdir(originalDirectory)
	#shutil.rmtree(createDir)
	
	#print commentGit
	#print listVersions
	#print len(listVersions)


#print listVersions
#print countVersions

#print pathVss, pathDb, projectVss, userVss, passVss

#sys.exit()
#os.system('"C:\Archivos de programa\Microsoft Visual SourceSafe\ss.exe" history $/test1')
#print candela
