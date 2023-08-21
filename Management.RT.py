
import tkinter as tk
from tkinter import ttk
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Crear la base de datos SQLite y establecer la conexión



class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Repuestos")

        self.create_ui()

    def create_ui(self):
        self.left_frame = ttk.Frame(self.root)
        self.left_frame.pack(side="left", padx=10, pady=10)

        self.right_frame = ttk.Frame(self.root)
        self.right_frame.pack(side="left", padx=10, pady=10)

        # Crear recuadro 
        repuesto_label = ttk.Label(self.left_frame, text="Tipo:")
        repuesto_label.pack(anchor="w")
        self.repuesto_entry = ttk.Entry(self.left_frame)
        self.repuesto_entry.pack(fill="x")

        # Crear recuadro p
        cantidad_label = ttk.Label(self.left_frame, text="Marca:")
        cantidad_label.pack(anchor="w")
        self.cantidad_entry = ttk.Entry(self.left_frame)
        self.cantidad_entry.pack(fill="x")

         # Crear recuadro
        cantidad_label = ttk.Label(self.left_frame, text="Módelo:")
        cantidad_label.pack(anchor="w")
        self.cantidad_entry = ttk.Entry(self.left_frame)
        self.cantidad_entry.pack(fill="x")

         # Crear recuadro 
        cantidad_label = ttk.Label(self.left_frame, text="Descripción:")
        cantidad_label.pack(anchor="w")
        self.cantidad_entry = ttk.Entry(self.left_frame)
        self.cantidad_entry.pack(fill="x")

         # Crear recuadro 
        cantidad_label = ttk.Label(self.left_frame, text="Color:")
        cantidad_label.pack(anchor="w")
        self.cantidad_entry = ttk.Entry(self.left_frame)
        self.cantidad_entry.pack(fill="x")

          # Crear recuadro 
        cantidad_label = ttk.Label(self.left_frame, text="Precio:")
        cantidad_label.pack(anchor="w")
        self.cantidad_entry = ttk.Entry(self.left_frame)
        self.cantidad_entry.pack(fill="x")

        # Crear botón para agregar
        agregar_button = ttk.Button(self.left_frame, text="Agregar")
        agregar_button.pack()

         # Crear botón para Buscar
        agregar_button = ttk.Button(self.left_frame, text="Buscar")
        agregar_button.pack()

        # Ventana en el lado derecho para ver los datos
        self.ver_datos_text = tk.Text(self.right_frame, wrap="none")
        self.ver_datos_text.pack(fill="both", expand=True)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
