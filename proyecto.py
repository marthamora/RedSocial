import os
from os import walk
from PIL import Image
from os import walk


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

Numerodeosos=lista.count("oso")
print(Numerodeosos," son osos")
Numerodeperros=lista.count("perro")
print(Numerodeperros," son perros")
Numerodepersonas=lista.count("persona")
print(Numerodepersonas," son personas")
Numerodecasas=lista.count("casa")
print(Numerodecasas," son casas")
Numerodefotos=lista.count("foto")
print(Numerodefotos," son fotos")
Numerodecomputadoras=lista.count("computadora")
print(Numerodecomputadoras," son computadora")
Numerodepajaros=lista.count("pajaro")
print(Numerodepajaros," son pajaros")
Numerodearticulos=lista.count("articulo")
print(Numerodearticulos," son articulos")
                            
                            
                
#for (ruta, carpeta, imagen) in walk('ruta_deimagenes'):
   # print ruta
    #print carpeta
    #print imagen

 ##  Lista_carpeta = [carpeta]
    #Lista_imagen = [imagen]
   # print Lista_imagen
