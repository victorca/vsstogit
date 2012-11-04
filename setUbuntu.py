#!/usr/bin/python

import sys
import os
import glob

f = open('outHistoryComplete', 'r')
historyComplete = f.read() #Leer todo el historial
f.close()

f = open('outHistoryComplete', 'r')
historyCompleteReadlines = f.readlines() #Leer todo el historial pero por lineas
f.close()

countVersions = historyComplete.count('User:') #Cantidad de versiones que tiene el proyecto

splitDos = historyCompleteReadlines[4].split(' ')

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

#originalDirectory = os.getcwd()
#os.mkdir('tmp1')
#os.chdir('tmp1')
#f = open('check-git-1', 'w')
#f.close()
#os.chdir(originalDirectory)
#f = open('check-git-2', 'w')
 
print listVersions[8]
print os.getcwd() 
print countVersions
print "Cantidad de elementos de la lista listComments: " + str(listComments)
print len(listVersions)
print listVersions
#print listVersions[4]
#print listVersions
#print retireOfList(splitDos, "")

#print historyComplete
