
f = open("archivo.txt",'w')
f.write("Primera linea\n")
f.close()
f = open("archivo.txt",'a')
f.write("Segunda linea\n")
f.close()