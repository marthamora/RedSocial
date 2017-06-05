import os
from os import walk
from PIL import Image
from os import walk
from imagen import imagen



class Biblioteca:
    Etiquetas = {
    "oceano":[2,3,4,5],
    "playa":[1]
    }
    ListaImagenes = [];

    def __init__(self,diretorio):
        ## "perrito.jpg","/misimagenes",""
        ## leerdirectorio
    def showId(self,Id):
        return ListaImagenes.index(Id)

    def leerdirectorio(self,directorio):
        ##Leer todas las imagenes del directorio
         ListaImagenes.append(imagen(ruta,nombre,""))
    def etiquetar():
        #Mostrar imagenes en

    def clasificar():
        ruta_deimagenes = os.getcwd()  # obtiene ruta del crpeta
        contenido = os.listdir(ruta_deimagenes)
        print (contenido)
        for (ruta,carpeta,imagen) in os.walk(ruta_deimagenes):
            Lista_imagenes= []
            print (Lista_imagenes)
            lista=[]
            for i in (contenido):
                   if i.endswith(('.png', '.pnj', '.gif')):
                       mi_imagen= Image.open(ruta_deimagenes+'/'+ i)
                       mi_imagen.show()
                       for i in range(0,5):
                           lista.append(raw_input("ingresar etiquetas: "))

    def showImagenes(self,inicio,final):
        for i in range(inicio,final):
            ListaImagenes.showId(i)
