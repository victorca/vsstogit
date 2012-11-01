#!C:\Python26 python

import os
import sys

##Bloque para introducir datos##############
print "Se asume: C:\Archivos de programa\Microsoft Visual SourceSafe"
pathVss = str(raw_input("Directorio VSS (PATH):"))

print "Introducir camino a la carpeta de la DB donde se encuentra el fichero srcsafe.ini"
pathDb = str(raw_input("Camino a Base de Datos (SSDIR):"))

print "Introducir proyecto, no es necesario incorporar el prefijo $/"
projectVss = str(raw_input("Proyecto a Migrar: $/"))

print "Introducir usuario VSS"
userVss = str(raw_input("Usuario VSS (SSUSER):"))

print "Introducir password del usuario VSS"
passVss = str(raw_input("Password Usuario VSS (SSPWD):"))
##Fin Bloque para introducir datos##############

##Bloque para comprobar la validez de los datos introducidos por el usuario###########
if pathVss == '':
  pathVss = "C:\Archivos de programa\Microsoft Visual SourceSafe"

if pathDb == '':
  print "ERROR: Debe introducir un camino"
  print "Cerrando script"
  sys.exit()
  
if projectVss == '':
  print "ERROR: Debe introducir el nombre del proyecto a migrar"
  print "Cerrando script"
  sys.exit()

if projectVss.find('$/') == -1:
  projectVss = '$/' + projectVss
  
if userVss == '':
  print "ERROR: Debe introducir un usuario de VSS"
  print "Cerrando script"
  sys.exit()
  
if passVss == '':
  print "ERROR: Debe introducir un password de usuario de VSS"
  print "Cerrando script"
  sys.exit()
##FIN Bloque para comprobar la validez de los datos introducidos por el usuario###########

##Bloque para establecer las variables de ambiente con las que trabajar############
print 'set SSDIR=' + pathDb
os.system('set SSDIR="' + pathDb + '"')
##FIN Bloque para establecer las variables de ambiente con las que trabajar############

#print pathVss, pathDb, projectVss, userVss, passVss

#sys.exit()
#os.system('"C:\Archivos de programa\Microsoft Visual SourceSafe\ss.exe" history $/test1')
#print candela