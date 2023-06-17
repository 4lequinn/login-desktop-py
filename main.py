import tkinter as tk
from tkinter import messagebox

def iniciar_sesion():
    username = entry_username.get()
    password = entry_password.get()
    
    if username == "admin" and password == "admin123":
        # Si las credenciales son correctas, se muestra un mensaje de éxito y se cierra la ventana actual
        messagebox.showinfo("Inicio de sesión exitoso", "¡Bienvenido!")
        ventana.destroy()
    else:
        # Si las credenciales son incorrectas, se muestra un mensaje de error
        messagebox.showerror("Error de inicio de sesión", "Credenciales incorrectas")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Login")

ventana.tk.call('tk', 'scaling', 1.0)


ventana.geometry("600x400")  # Ancho x Alto


ventana.configure(bg="lightgray")


label_username = tk.Label(ventana, text="Usuario:")
label_username.pack()
entry_username = tk.Entry(ventana)
entry_username.pack()

label_password = tk.Label(ventana, text="Contraseña:")
label_password.pack()
entry_password = tk.Entry(ventana, show="*")  
entry_password.pack()


boton_iniciar_sesion = tk.Button(ventana, text="Iniciar sesión", command=iniciar_sesion)
boton_iniciar_sesion.pack()


ventana.mainloop()
