import tkinter as tk
from PIL import ImageTk, Image

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ventana con imagen de fondo")

# Cargar la imagen de fondo
imagen = Image.open("ruta_de_la_imagen.jpg")  # Reemplaza "ruta_de_la_imagen.jpg" con la ruta de tu imagen
imagen = imagen.resize((800, 600), Image.ANTIALIAS)  # Ajustar el tamaño de la imagen si es necesario
imagen_de_fondo = ImageTk.PhotoImage(imagen)

# Crear un widget Label para mostrar la imagen de fondo
fondo_label = tk.Label(ventana, image=imagen_de_fondo)
fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

# Ajustar las dimensiones de la ventana principal para que coincidan con las dimensiones de la imagen de fondo
ventana.geometry(f"{imagen.width}x{imagen.height}")

# Ejecutar el bucle principal de Tkinter
ventana.mainloop()
