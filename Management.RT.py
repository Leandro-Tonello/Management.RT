
import tkinter as tk
from tkinter import ttk
import openpyxl
#from sqlalchemy import create_engine, Column, Integer, String
#from sqlalchemy.orm import sessionmaker
#from sqlalchemy.ext.declarative import declarative_base

# Crear la base de datos SQLite y establecer la conexión



class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Repuestos")
        self.create_ui()
    
    def cargar_datos(self):
        self.path = r"Libro excel.xlsx"
        self.workbook = openpyxl.load_workbook(self.path)
        self.sheet = self.workbook.active
        self.lista_de_valores = list(self.sheet.values)
        print(self.lista_de_valores)
        
        # Convertir el generador en una lista y luego configurar los encabezados
        nombres_de_columnas = list(self.lista_de_valores[0])
        for nombre_de_columna, columna in zip(nombres_de_columnas, self.columnas):
            self.treeview.heading(columna, text=nombre_de_columna)
        
        for valor in self.lista_de_valores[1:]:
            self.treeview.insert('', tk.END, values= valor)
        
    def agregar_repuesto(self):
        self.tipo = self.tipo_entry.get()
        self.marca = self.marca_entry.get()
        self.modelo = self.modelo_entry.get()
        self.descripción = self.descripción_entry.get()
        self.color = self.color_entry.get()
        self.precio = self.precio_entry.get()
        
        self.path = r"Libro excel.xlsx"
        self.workbook = openpyxl.load_workbook(self.path)
        self.sheet = self.workbook.active
        self.valores_de_fila = [self.tipo, self.marca, self.modelo, self.descripción, self.color, self.precio]         
        self.sheet.append(self.valores_de_fila)
        self.workbook.save(self.path)
        self.treeview.insert('', tk.END, values = self.valores_de_fila)

      
    def create_ui(self):
        root.tk.call("source", "forest-dark.tcl")
        
        style = ttk.Style(root)
        style.theme_use("forest-dark")
        
        
        self.left_frame = ttk.Frame(self.root)
        self.left_frame.pack(side="left", padx=10, pady=10)

        self.right_frame = ttk.Frame(self.root)
        self.right_frame.pack(side="left", padx=10, pady=10)
        
        # Crear recuadro 
        tipo_label = ttk.Label(self.left_frame, text="Tipo:")
        tipo_label.pack(anchor="w")
        self.tipo_entry = ttk.Entry(self.left_frame)
        self.tipo_entry.pack(fill="x")

        # Crear recuadro p
        marca_label = ttk.Label(self.left_frame, text="Marca:")
        marca_label.pack(anchor="w")
        self.marca_entry = ttk.Entry(self.left_frame)
        self.marca_entry.pack(fill="x")

         # Crear recuadro
        modelo_label = ttk.Label(self.left_frame, text="Módelo:")
        modelo_label.pack(anchor="w")
        self.modelo_entry = ttk.Entry(self.left_frame)
        self.modelo_entry.pack(fill="x")

         # Crear recuadro 
        descripción_label = ttk.Label(self.left_frame, text="Descripción:")
        descripción_label.pack(anchor="w")
        self.descripción_entry = ttk.Entry(self.left_frame)
        self.descripción_entry.pack(fill="x")

         # Crear recuadro 
        color_label = ttk.Label(self.left_frame, text="Color:")
        color_label.pack(anchor="w")
        self.color_entry = ttk.Entry(self.left_frame)
        self.color_entry.pack(fill="x")

          # Crear recuadro 
        precio_label = ttk.Label(self.left_frame, text="Precio")
        precio_label.pack(anchor="w")
        self.precio_entry = ttk.Entry(self.left_frame)
        self.precio_entry.pack(fill="x", pady = 5)

        # Crear botón para agregar
        agregar_button = ttk.Button(self.left_frame, text="Agregar", command = self.agregar_repuesto)
        
        agregar_button.pack(padx = 5, pady = 5)

         # Crear botón para Buscar
        agregar_button = ttk.Button(self.left_frame, text="Buscar")
        
        agregar_button.pack(padx = 5, pady = 5)

        # Ventana en el lado derecho para ver los datos
        self.treeFrame = ttk.Frame(self.right_frame)
        self.treeFrame.grid(row = 0, column = 1)
        self.treeScroll = ttk.Scrollbar(self.treeFrame)
        self.treeScroll.pack(side="right", fill = "y")
        
        self.columnas = ("Tipo", "Marca", "Modelo", "Descripción", "Color", "Precio")
        
        self.treeview = ttk.Treeview(self.treeFrame, show = "headings", yscrollcommand=self.treeScroll.set, columns = self.columnas, height = 13)
        self.treeview.column("Tipo", width = 100)
        self.treeview.column("Marca", width = 100)
        self.treeview.column("Modelo", width = 100)
        self.treeview.column("Descripción", width = 100)
        self.treeview.column("Color", width = 100)
        self.treeview.column("Precio", width = 100)
        
    
        self.treeview.pack()
        self.treeScroll.config(command=self.treeview.yview)
        
if __name__ == "__main__":
    root = tk.Tk()
    
    app = App(root)
    app.cargar_datos()
    
    
    
    
    root.mainloop()
