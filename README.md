vsstogit
========

Migrate VSS repository to GIT

---------------------------------------------------------------------------------------

VSS – Visual SourceSafe
Todo el procedimiento se debe ejecutar sobre una PC Windows.

Tener instalado:
GIT
python
VSS

Tener el paquete “vsstogit.tar.gz”

- Descomprimir vsstogit.tar.gz en C:\

- Posicionarse dentro de la carpeta vsstogit obtenida luego de descomprimir vsstogit.tar.gz  
Abrir un terminal y escribir:
cd C:\vsstogit

Antes de ejecutar el script “convertVSStoGIT.py” hay que especificar el camino hasta la carpeta donde se encuentra la Base de Datos del Proyecto que se migrará a GIT y también el usuario y el password con el cual accederla. Para ello:

- En la misma terminal que está abierta escribir:
set SSDIR=<Camino a la DB>
ejemplo: set SSDIR=C:\Documents and Settings\victor\Escritorio\newDB

También:

set SSUSER=<Usuario de VSS para Acceder a la DB>
ejemplo: set SSUSER=victor

set SSPWD=<Password del SSUSER para Acceder a la DB>
ejemplo: set SSPWD=123

El script necesita que el sistema tenga el siguiente estándar en la fecha interna para poder trabajar con ella:

- Ir a Panel de Control → Configuración regional y de idioma → Personalizar → Fecha:

En Formato de fecha corta escoger aaaa-MM-dd
En Separador de fecha escoger -

Finalmente ya se puede ejecutar el script “convertVSStoGIT.py”, en la misma terminal escribir:
"C:\Python26\python.exe" convertVSStoGIT.py

Hasta aquí todo el procedimiento para ejecutar el script de migración de VSS a GIT. En caso de que sea necesario en el fichero “convertVSStoGIT.py” se puede hacer algunas configuraciones extras como por ejemplo:

La variable pathExeGit especifica el camino al ejecutable de git, por defecto es:
pathExeGit = "C:/Archivos de programa/Git/bin/git.exe"

---------------------------------------------------------------------------------------

VSS – Visual SourceSafe
The whole procedure must be run on a Windows PC.

Have installed:
GIT
python
VSS

Having the package "vsstogit.tar.gz"

- Unzip vsstogit.tar.gz in C: \

- Positioning in the vsstogit folder after unzipping vsstogit.tar.gz.
Open a terminal and type:
cd C: \ vsstogit

Before running the script "convertVSStoGIT.py" must specify the path to the folder where the Project database to be migrated to GIT and the user name and password with which to access it. To do this:

- In the same terminal:
set SSDIR=<Path to DB>
example: set SSDIR=C:\Documents and Settings\victor\Escritorio\newDB

also:

set SSUSER=<User of VSS>
example: set SSUSER=victor

set SSPWD=<Password of SSUSER>
example: set SSPWD=123

The script requires that the system has the following standard internal date to work with it:

- Go to Control Panel → Regional and Language Settings → Personalize → Date:

In Short date format aaaa-MM-dd
In choosing Date separator -

Finally you can run the script "convertVSStoGIT.py", in the same terminal type:
"C:\Python26\python.exe" convertVSStoGIT.py
