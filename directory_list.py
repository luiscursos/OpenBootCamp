from os import listdir, scandir, getcwd, stat
import humanize

# Muestra los archivos y sus tamaños del directorio desde donde se ejecute

pwd = getcwd()
directory=scandir(path=pwd)

print ("\nDirectorio: ",pwd,"\n")
for i in directory:
    total=stat(i).st_size
    human = humanize.naturalsize(total)
    print( i, total)