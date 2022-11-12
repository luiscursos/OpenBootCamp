from time import localtime,  strptime 

"""
En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. 
Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.

En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, 
haréis una operación para calcular el tiempo que queda de trabajo.
"""
current = localtime()[3] # 

if current >= strptime(("07:00"[:2]),"%H")[3]:
     print("It's time go to home")
else:
     work_time_left = strptime("07:00"[:2],"%M%H")[3]-current
     print(work_time_left," hours left to get off work")
     


