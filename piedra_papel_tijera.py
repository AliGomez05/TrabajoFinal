import random
import time

class ppt:

    def __init__(self):
        self.a=1
        self.jugada=1
        self.empate=0
        self.ganacpu=0
        self.ganausua=0
        

    def resultados(self):
        print("\n****RESUMEN DEL PARTIDO****")
        print("\n Jugadas ganadas",self.ganausua)
        print("\n Jugadas perdidas",self.ganacpu)
        print("\n Jugadas empatadas",self.empate)
        print("\n#### Nos vemos en la próxima partida ####")


    def jugar(self):

        print("\n****BIENVENIDO A PIEDRA PAPEL TIJERA****")
        print("\nEstoy pensando mi opción... Vamos a ver quien gana este partido :-) \nTenemos 3 jugadas ¡¡Buena Suerte!!")
        time.sleep(2)
      

        while self.a == 1:
                
            while self.jugada <=3:
                cpu = random.choice(["Piedra","Papel","Tijera"]).lower()
                print("\nJugada N°",self.jugada)
                usuario=input("\n¿Qué elejís? Piedra-Papel-Tijera: ").lower()
                if usuario =="piedra" or usuario=="papel" or usuario== "tijera":

                    if usuario == cpu:
                        time.sleep(2)
                        print("\n Elegimos", usuario.capitalize(),"...", "Esto es un ¡¡EMPATE!!") 
                        self.empate+=1
                        self.jugada+=1
                    elif ((usuario== "piedra" and cpu=="tijera") or(usuario=="papel" and cpu=="piedra") or(usuario=="tijera"and cpu=="papel")):
                        time.sleep(2)
                        print("\n***Elegí",cpu.capitalize(), "***")
                        print("\n",usuario.capitalize(),"mata a",cpu.capitalize(),"... ¡GANASTE!") 
                        self.ganausua+=1  
                        self.jugada+=1             
                    elif((usuario== "tijera" and cpu=="piedra") or(usuario=="piedra" and cpu=="papel") or(usuario=="papel"or cpu=="tijera")):
                        time.sleep(2)
                        print("\n***Elegí",cpu.capitalize(), "***")
                        print("\n",cpu.capitalize(),"mata a",usuario.capitalize(),"... ¡PERDISTE!")   
                        self.ganacpu+=1
                        self.jugada+=1
                else:
                    print("\nOpción incorrecta. Probá de nuevo con Piedra, Papel o Tijera.")
                
            
            
            print("\n¿Querés jugar de nuevo? \n \n 1- Si \n 2- No")
            print("")
            self.a=int(input("¿Te animás?: "))
            self.jugada=1

            ppt.resultados(self)







