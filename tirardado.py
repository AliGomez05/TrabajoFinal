import random
import time

class dado:
    
    
    def jugar(self):
        print("\n****BIENVENIDO A TIRAR EL DADO****")
        a=1
        while a == 1:
            print("\nJuguemos...")
            time.sleep(2)

            tiro=random.randint(1,6)
            print("\nEl número que te tocó es: ", tiro)
            print("")

            print("¿Querés jugar de nuevo? \n \n 1- Si \n 2- No")
            print("")
            a=int(input("¿Qué elegís?: "))
        print("\n#### Nos vemos en la próxima partida ####")
    
 






