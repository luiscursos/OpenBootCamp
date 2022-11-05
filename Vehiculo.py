class Vehiculo:
    color = "Rojo"
    ruedas = 4
    puertas = 5


class Coche(Vehiculo):
    velocidad = 120
    cilindrada = 1600


obj = Coche() 

print(obj.color)
print(obj.ruedas)
print(obj.puertas)
print(obj.velocidad)
print(obj.cilindrada)
