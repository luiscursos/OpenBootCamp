# Enunciado: Crea una función que calcule los números primos entre 1 y N, siendo N el parámetro que recibe la función.

# Objetivo:

# Uso de bucles anidados

# El uso de colecciones





def main():
    numero_final = int(input("Número final: "))
    numeros_primos(numero_final)


def numeros_primos(numero_final):
    lista_nPrimos=[]
    numero = 2

    while numero < numero_final:
        count = 2
        resto = 0
        while count < numero:
            if numero % count == 0:
                resto+=1
            count+=1
        if resto ==0:
            lista_nPrimos.append(numero)
            print(numero, "Es primo")

        numero+=1

if __name__ == '__main__':
    main()



