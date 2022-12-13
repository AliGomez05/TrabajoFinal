import random
import time

class adivina:

    def __init__(self):
        self.adivi=0
        self.noadiv=0
        self.num=0
        self.pensado=0
        self.intento=1
        self.a=1
        
    def resultados(adivi,noadiv):
        print("\n****RESUMEN DE LAS JUGADAS****")
        print("\n Veces que adivinaste",adivi)
        print("\n Veces que fallaste",noadiv)
        print("\n#### Nos vemos en la próxima partida ####")
       
    
    def comparacion(self,pensado,num):
        if pensado == num:
            print("\nAdivinaste en el intento", self.intento,"¡FELICITACIONES!")
            self.intento+=3
            self.adivi+=1
        elif self.intento==3:
            print("\nÚltimo intento, no adivinaste :-( ...  ***El número que pensé era", num,"*** \n¡¡Suerte en la próxima!!" )
            self.intento+=3
            self.noadiv+=1
        else:
            print("\nNo adivinaste,no te preocupes,intentemos de nuevo.")
            self.intento+=1
            self.noadiv+=1  
     
    def jugar(self):

        print("\n****BIENVENIDO A ADIVINA EL NÚMERO****")
        print("\nEstoy pensando un número del 1 al 10 y te reto a adivinarlo. \nTenés 3 intentos \n¡¡Buena Suerte!!")
        time.sleep(2)
                                 
        while self.a == 1:
            num = random.randint(1,10)
           
            while self.intento <=3:
                print("\nIntento para adivinar N°",self.intento)
                pensado=int(input("\n¿Qué número pensé?: "))
                if pensado >=1 and pensado<=10:
                    time.sleep(2)
                    adivina.comparacion(self,pensado,num)   
                else:
                    print("\nOpción incorrecta. Probá de nuevo con un número del 1 al 10.")             
                     
            print("\n¿Querés jugar de nuevo? \n \n 1- Si \n 2- No")
            print("")
            self.a=int(input("¿Qué elegís?: "))
            self.intento=1
        
        adivina.resultados(self.adivi,self.noadiv)
        
            

                       