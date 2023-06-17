import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import requests
from settings.settings import BASE_URL
from model.user import User, Role


def create_btn(name:str, window):
    btn = tk.Button(window, text=name)
    btn.pack()


def open_window(user:User):
    redirect = tk.Tk()
    redirect.configure(bg="orange")  
    redirect.geometry("800x600")
    redirect.title(f"Dashboard {user.role.description}")
    label_info = tk.Label(redirect, text=f"Bienvenido : {user.username}")
    label_info.pack()

    labels = []

    if user.role.id == 1:
        labels = ['Modificar profesional','Modificar cliente','Eliminar profesional','Eliminar cliente','Generar indicadores']
    elif user.role.id == 2:
        labels = ['Asesorias','Ingresar llamadas','Visitas','Clientes','Accidente']
    elif user.role.id == 3:
        labels = ['Solicitar capacitacion','Llamadas','Facturas','Accidente','Historial']
    
    for name in labels:
        create_btn(name,redirect)


def kind_user(response:dict):
    role = Role(response['role_id'],response['role_description'])
    user = User(username=response['username'],company=response['company'],role=role)
    open_window(user)


def login():
    username = entry_username.get()
    password = entry_password.get()

    endpoint = BASE_URL + '/api/v1/auth/token/'

    # Datos a enviar en la petición POST
    data = { 'username': username, 'password': password }

    # Realizar la petición POST
    response = requests.post(endpoint, data=data)

        
    if response.status_code == 200:
        response_data = response.json()
        
        # Si las credenciales son correctas, se muestra un mensaje de éxito y se cierra la ventana actual
        messagebox.showinfo("Inicio de sesión exitoso", "¡Bienvenido!")
        window.destroy()
        
        kind_user(response_data)

    else:
        # Si las credenciales son incorrectas, se muestra un mensaje de error
        messagebox.showerror("Error de inicio de sesión", "Credenciales incorrectas")


# Crear la ventana principal
window = tk.Tk()
window.title("Login")

# Cargar la imagen de fondo
img = Image.open('./static/img/bg1.png')  # Reemplaza "ruta_de_la_imagen.jpg" con la ruta de tu imagen
img = img.resize((800, 600), Image.ANTIALIAS)  # Ajustar el tamaño de la imagen si es necesario
background = ImageTk.PhotoImage(img)

# Crear un widget Label para mostrar la imagen de fondo
bg_label = tk.Label(window, image=background)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Ajustar las dimensiones de la ventana principal para que coincidan con las dimensiones de la imagen de fondo
window.geometry(f"{background.width()}x{background.height()}")  # Añade paréntesis a los métodos width y height

label_username = tk.Label(window, text="Usuario:")
label_username.pack()
entry_username = tk.Entry(window)
entry_username.pack()

label_password = tk.Label(window, text="Contraseña:")
label_password.pack()
entry_password = tk.Entry(window, show="*")
entry_password.pack()

btn_login = tk.Button(window, text="Iniciar sesión", command=login)
btn_login.pack()

window.mainloop()
