import matplotlib.pyplot as plt
import time
import numpy as np
import matplotlib.ticker as ticker

class grafico:

    def grafico(self):

        print("\n****BIENVENIDO A GRÁFICOS INTERESANTES****")
        print("\nTe invito a conocer estos tipos de gráficos: \n \n 1-Barra \n 2-Torta \n 3-Lineal ")
        
        a=1

        while a == 1:
            
            tipo=int(input("\n¿Cuál es el gráfico que te interesa? "))

            if tipo==1:
                print("\n          ### Gráfico Barra ###          ")
                print("\nUn diagrama de barras es un gráfico usado para mostrar de forma resumida un grupo de "
                "datos que puede incluir variables cualitativas y cuantitativas.  ")
                plt.title("Plataforma de Streaming con mayor suscriptores")
                time.sleep(3)
                x=np.array(["Netflix","Disney","Amazon","HBO Max"])
                plt.xlabel("Plataformas")
                y=np.array([221,118,200,67])
                plt.ylabel("Millones de suscriptores")
                plt.bar(x,y,color="purple")
                plt.show()       
            
            elif tipo==2:
                print("\n          ### Gráfico Torta ###          ")
                print("\nUna gráfica de tarta es una gráfica circular dividida en sectores, que ilustran magnitudes o frecuencias relativas."
                "En una gráfica de tarta, el área de cada sector es proporcional a la cantidad que representa.")
                plt.title("Tipo de Pelicúlas más vistas")
                time.sleep(3)
                valores= np.array([4,4,1,5,6])
                etiquetas=["Ciencia Ficción","Comedia","Drama","Acción","Romance"]
                separacion=[0,0,0,0,0.2]
                plt.pie(valores, labels=etiquetas, explode=separacion,autopct="%0.1f %%")
                plt.show()
             
            elif tipo==3:
                print("\n          ### Gráfico Líneal ###          ")
                print("\nEl diagrama o gráfico lineal se compone de una serie de puntos que al unirlos te muestran una línea completa con los" 
                "cambios de una variable a lo largo del tiempo.")
                time.sleep(3)
                plt.plot([0,2,3,4],[1,5,7,9],"r*-")
                plt.title("Función Lineal")
                plt.xlabel("Velocidad")
                plt.ylabel("Tiempo")
                plt.show()
            else:
                print("Opción incorrecta")
        

            print("\n¿Querés conocer sobre otro gráfico? \n 1- Si \n 2- No")
            print("")
            a=int(input("¿Qué elegís?: "))
        print("\n#### Nos vemos en el próximo apendizaje ####")






