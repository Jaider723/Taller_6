import tkinter as tk

#Ejemplo de implementación de una interfaz gráfica con Tkinter

def actualizar_etiqueta():
    etiqueta.config(text="¡Hola, mundo!")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Interfaz Gráfica")

# Crear una etiqueta
etiqueta = tk.Label(ventana, text="Bienvenido a mi aplicación")
etiqueta.pack(pady=10)

# Crear un botón
boton = tk.Button(ventana, text="Haz clic aquí", command=actualizar_etiqueta)
boton.pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
