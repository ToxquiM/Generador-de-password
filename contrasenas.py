import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generar_contraseña():
    longitud = int(entry_longitud.get())
    incluir_caracteres_especiales = var_especiales.get()
    
    caracteres = string.ascii_letters + string.digits
    if incluir_caracteres_especiales:
        caracteres += string.punctuation
    
    contraseña = ''.join(random.choice(caracteres) for i in range(longitud))
    entry_contraseña.delete(0, tk.END)
    entry_contraseña.insert(0, contraseña)

def copiar_contraseña():
    pyperclip.copy(entry_contraseña.get())
    messagebox.showinfo("Información", "¡Contraseña copiada al portapapeles!")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Generador de Contraseñas")

tk.Label(root, text="Longitud de la contraseña:").pack(pady=5)
entry_longitud = tk.Entry(root)
entry_longitud.pack(pady=5)

var_especiales = tk.BooleanVar()
tk.Checkbutton(root, text="Incluir caracteres especiales", variable=var_especiales).pack(pady=5)

tk.Button(root, text="Generar Contraseña", command=generar_contraseña).pack(pady=10)

tk.Label(root, text="Contraseña generada:").pack(pady=5)
entry_contraseña = tk.Entry(root, width=50)
entry_contraseña.pack(pady=5)

tk.Button(root, text="Copiar Contraseña", command=copiar_contraseña).pack(pady=10)

root.mainloop()
