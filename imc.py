
def imc():
    peso_user = float(input("Introduce tu peso en Kg: "))
    altura_user = float(input ("Introduce tu altura : "))
    imc = peso_user // (altura_user**2)
    print("Tu imc es:", imc)
... 


imc()

