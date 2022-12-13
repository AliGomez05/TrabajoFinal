# Tu desafío es desarrollar un programa que permita realizar diferentes operaciones en base a
# las opciones que el usuario vaya ingresando por línea de comandos:
# ● Jugar a “piedra, papel, tijera” compitiendo contra la computadora.
# ● Adivinar un número compitiendo contra la computadora.
# ● Tirar un dado.
# ● Graficar una función matemática.

import piedra_papel_tijera
import tirardado
import adivinanumero
import grafico_matematico

print("\n***ACTIVIDADES PARA EL TIEMPO LIBRE***")

nombre= input("\n Hola mi nombre es CPU, ¿el tuyo cuál es?: ")
a=1
print("\nHola", nombre,"!!")

while a==1:
    
    print("\n¿Qué actividad querés hacer?")
    print("\n 1-Jugar a Piedra, papel, tijera \n 2-Tirar el dado \n 3-Adivinar un númmero \n 4-Conocer sobre gráficos \n 5-Salir")
    print("\n",nombre.upper(), end=" ")
    jugar= int(input("¿Qué opción elegís?:"))

    if jugar == 1:
        juego= piedra_papel_tijera.ppt()
        juego.jugar()
    elif jugar == 2:
        juego=tirardado.dado()
        juego.jugar()
    elif jugar == 3:
        juego=adivinanumero.adivina()
        juego.jugar()
    elif jugar == 4:
        juego=grafico_matematico.grafico()
        juego.grafico()
    elif jugar==5:
        break
    else:
        print("Opción Incorrecta, elije otra opción.")
        jugar= int(input("\n ¿Qué opción elegís?"))
    print("\n",nombre.upper(), "¿Volvemos al menú de actividades? \n \n 1- Si \n 2- No")
    a=int(input("\n¿Qué elegís?: "))
   
print("\n¡¡Te espero pronto ",nombre,"!! :-)")






