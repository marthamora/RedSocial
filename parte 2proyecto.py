from Tkinter import*
import tkMessageBox

    c1=photo1.get()
    c2=photo1.get()
    c3=photo1.get()
    c4=photo1.get()
    c5=photo1.get()
    photos= c1+c2+c3+c4+c5
    photosB = photosA
    photosA += photos
    ventana=Tk()
    ventana.geometry("750x700+0+0")
    ventana.title("imagenes por categorias")
    photosA=18
    allimages=PhotoImage(file="allimages.gif")
    perro1=PhotoImage(file="perro.jpg")
    perro2=PhotoImage(file="perro2.jpg")
    perro3=PhotoImage(file="perro3.jpg")
    gato1=PhotoImage(file="gato.jpg")
    leon=PhotoImage(file="lion.jpg")
    tigre=PhotoImage(file="tigre.jpg")
    conejo=PhotoImage(file="conejo.jpg")


lblp1=Label(ventana,text="escribe una categoria").grid(row=0,column=5)

                boton1 = Checkbutton(ventana,image=allimages[vector2[photosA]],bg='red',variable=photo1,onvalue=1,offvalue=0).grid(row=0,column=0)
                            boton2 = Checkbutton(ventana,image=allimages[vector2[photosA]],bg='red',variable=,onvalue=1,offvalue=0).grid(row=0,column=1)

    else:
        lblp1=Label(ventana,text="estas imagenes son de la categoria DOMESTICOS").grid(row=0,column=5)
                photosA tkMessageBox.showinfo(title="SON DE LA CATEGORIA FELINOS",message="SON MUCHOS FELINOS")
    if>=18
        tkMessageBox.showinfo(title="SON TODAS LAS IMAGENES EN EL DIRECTORIO",message="SE ACABARON")
