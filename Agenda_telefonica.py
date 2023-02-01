
# '''
# Enunciado: Crea una agenda de teléfonos que se gestione por consola, que te permita:

# Añadir a cualquier persona, indicando nombre y después teléfono

# Buscar el teléfono de una persona

# Objetivo:

# Aprender a manejar la entrada y la salida por consola.

# El uso de colecciones (array o diccionario)

# Ampliación:

# Al buscar a una persona, que te muestre todas aquellas que comiencen por el texto que has introducido. Ejemplo:

# Introduce un nombre: Pep
# Resultados:

# Pepe 659331013

# Pepe Martín 633743551
# '''

nombres = []
telefonos = []
data = False
if data  == False: 
    agenda = dict()


def main():
    print("""Opciones:
            1 - Consultar Registro
            2 - Agregar Teléfono
                """)
    
    user = int(input("Introduce opcion 1 ó 2: "))
    if user == 1:
        consulta()
    elif user == 2:
        agregar_telefono()
    else:
        print("opcion incorrecta")

def consulta(query, agenda):
    query = input("Introduce nombre a buscar: ")
    consultaRegistro(query, agenda)
    

def agregar_telefono():
    for i in range(5):
        nombre = input("Introduce un nombre: ")
        telefono = input("Introduce un telefono: ")
        nombres.append(nombre)
        telefonos.append(telefono)
    agenda=dict(zip(nombres, telefonos))
    data==True
    consulta(nombre, agenda)

def consultaRegistro(query, agenda):
    for query,valor in agenda.items():
        if query.startswith("L"):
            print(f"Nombre: {query}; Telefono: {valor}")

if __name__ == '__main__':
    main()