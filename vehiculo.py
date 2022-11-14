import pickle


class Vehicle():
    pass

coche=Vehicle()


f = open("archivo.bin",'wb')
pickle.dump(coche,f)
f.close()

f = open("archivo.bin",'rb')
turismo = pickle.load(f)
f.close()

