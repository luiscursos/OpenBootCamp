from functools import reduce
# En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos impares de una lista pasada por parámetro con filter y realizará una suma de todos estos elementos obtenidos mediante reduce.



def odd_numbers (number):
    if number % 2 != 0:
        return True

def add (a,b):
    return a+b

numbers_list = [1,23,45,4,67,8,6,10,14,11,14,82]
odd_result=(list(filter(odd_numbers,numbers_list)))
print(reduce(add,odd_result))

