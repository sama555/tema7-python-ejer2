import time
import pprint
import tiempo.hora
"""
En este segundo ejercicios tendréis que crear un script que nos diga si es la hora de ir a casa. 
Tendréis que hacer uso del modulo time. Necesitaréis la fecha del sistema y poder comprobar la hora.

En el caso de que sean más de las 7, se mostrará un mensaje y en caso contrario, 
haréis una operación para calcular el tiempo que queda de trabajo.
"""

"""tiempo_segundos = time.time()
tiempo_cadena= time.ctime(tiempo_segundos) # 1488651001.7188754 seg
print(tiempo_cadena)
"""
"""
tiempo=time.ctime()
print(tiempo)
"""


def main():
    irse = tiempo.hora.ircasa()
    print(irse)


if __name__ == '__main__':
    main()
