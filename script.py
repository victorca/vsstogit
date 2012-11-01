#!C:\Python26 python

import os
import sys

##Bloque para introducir datos##############
print "Introducir proyecto, no es necesario incorporar el prefijo $/"
projectVss = str(raw_input("Proyecto a Migrar: $/"))
##Fin Bloque para introducir datos##############

##Bloque para comprobar la validez de los datos introducidos por el usuario###########
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



#print pathVss, pathDb, projectVss, userVss, passVss

#sys.exit()
#os.system('"C:\Archivos de programa\Microsoft Visual SourceSafe\ss.exe" history $/test1')
#print candela