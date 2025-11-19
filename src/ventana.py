import tkinter as tk
from tkinter import messagebox

def mostrar_mensaje():
    messagebox.showinfo("Aviso", "¡Botón presionado!")

ventana = tk.Tk() #Crea la ventana principal
ventana.title("Ventana simple") #Le da un titulo    

label = tk.Label(ventana, text="Presionada el botón ´para ver un mensaje") #Crea un widget de texto
label.pack(pady=10) #Lo coloca en la ventana

boton = tk.Button(ventana, text="Haz click aqui", command =mostrar_mensaje)
boton.pack(pady=10)



ventana.mainloop() #Muestra la ventana y espera acciones del usuario