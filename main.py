import os 
from biblioteca import biblioteca
ruta_deimagenes = os.getcwd()  

directorio= "ruta_deimagenes"
Bibloteca = biblioteca(directorio)
Numerodeosos=Bibioteca.count([1,4,5,6])
print(Numerodeosos)
Biblioteca.show([1,3,5]);
Biblioteca.showImagenes(1,40)




