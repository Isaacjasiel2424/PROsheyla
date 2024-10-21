import tkinter as tk
from ProcesosDB import ProcesosDB
from tkinter import ttk

class clsVentanas:
    
    # Variables globales que almacenan las distintas ventanas activas
    globalVentana = None
    globalVentanaAlta = None 
    globalVentanaEdicion = None  
    globalVentanaBusqueda = None  
    globalVentanaVentas = None 
    
    globalTablaInicio = None
    globalTablaVenta = None
    
    
    globalNombreProducto = None
    globalPrecioProducto = None
    globalCodigoBarrasProducto = None
    
    
    globalIdActualEdicion = None
    
    globalEntryFiltro = None
    
    allProducts = []
    
    # Constructor de la clase
    def __init__(self) -> None:
        print("Inicio Clase Ventanas")  # Imprime un mensaje al inicializar la clase
        pass
    
    
    # Función que se ejecuta al hacer doble clic en un elemento de la tabla
    def on_double_click(self,event):
        item = self.globalTablaInicio.selection()[0]  # Obtener el elemento seleccionado
        item_valores = self.globalTablaInicio.item(item, "values")  # Obtener los valores del elemento
        self.globalTablaVenta.insert("", "end", values=(item_valores[1],item_valores[2],item_valores[0]))
        

    def buscar(self,v1):
        filtro = self.globalEntryFiltro.get().lower()

        # Limpiar la tabla antes de insertar los resultados filtrados
        for item in self.globalTablaInicio.get_children():
            self.globalTablaInicio.delete(item)

        # Insertar solo los productos que coincidan con el filtro
        for producto in self.allProducts:
            print(producto[2].lower())
            if filtro in producto[2]:
                self.globalTablaInicio.insert("", "end", values=(producto[0], producto[2], producto[3]))
                # self.globalTablaInicio.insert('', tk.END, values=producto)
        
    # Método para crear la ventana principal
    def ventanaPrincipal(self):
        ventana = tk.Tk()  # Crea una nueva ventana de Tkinter
        ventana.title("Ventana Principal")  # Establece el título de la ventana
        ventana.geometry("1100x450")  # Define el tamaño de la ventana (800x400)
        self.globalVentana = ventana  # Asigna la ventana principal a la variable global
        
        

        # Campo de texto para el filtro
        entry_filtro = tk.Entry(ventana)
        entry_filtro.grid(row=0, column=2, padx=10, pady=10, sticky="ew")
        entry_filtro.bind('<KeyRelease>', self.buscar)  # Filtrar mientras se escribe
        self.globalEntryFiltro = entry_filtro
        
        tabla = ttk.Treeview(ventana, columns=("Código de Barras", "Nombre", "Precio"), show="headings")
        tabla.heading("Código de Barras", text="Código de Barras")
        tabla.heading("Nombre", text="Nombre")
        tabla.heading("Precio", text="Precio")
        tabla.grid(row=1, column=1,columnspan=2, padx=10, pady=10, sticky="ew")
        
        # Vincular el evento de doble clic al Treeview
        tabla.bind("<Double-1>", self.on_double_click)
        
        tablaVenta = ttk.Treeview(ventana, columns=("Nombre", "Precio","Código de Barras"), show="headings")
        tablaVenta.heading("Nombre", text="Nombre")
        tablaVenta.heading("Precio", text="Precio")
        tabla.heading("Código de Barras", text="Código de Barras")
        
        # Ocultar la columna "Código de Barras"
        tablaVenta.column("Código de Barras", width=0, minwidth=0)
        tablaVenta.grid(row=1, column=0,columnspan=1, padx=1, pady=1, sticky="ew")
        
        self.globalTablaVenta = tablaVenta
        
        # Creación de botones con sus respectivas acciones
        btnAlta = self.btn(ventana, 'Alta', self.btnAltaClicked)  # Crea el botón "Alta"
        btnAlta.grid(row=2, column=0, padx=1, pady=1, sticky="ew")  # Ubicación del botón en la ventana

        btnActualizar = self.btn(ventana, 'Actualizar', self.btnEdicionClicked)  # Crea el botón "Actualizar"
        btnActualizar.grid(row=2, column=1, padx=1, pady=1, sticky="ew")

        btnVentasRealizadas = self.btn(ventana, 'Ventas Realizadas', self.btnVentasClicked)  # Botón "Ventas"
        btnVentasRealizadas.grid(row=3, column=0 ,padx=1, pady=1, sticky="ew")
        
        # Creación de botones con sus respectivas acciones
        btnAlta = self.btn(ventana, 'Aceptar', self.aceptarVenta)  # Crea el botón "Alta"
        btnAlta.grid(row=0, column=0, padx=1, pady=1, sticky="ew")  # Ubicación del botón en la ventana
        
         # Creación de botones con sus respectivas acciones
        btnAlta = self.btnBorrar(ventana, 'Cancelar', self.cancelarVenta)  # Crea el botón "Alta"
        btnAlta.grid(row=0, column=1, padx=1, pady=1, sticky="ew")  # Ubicación del botón en la ventana
        
        self.globalTablaInicio = tabla
        
        conexion = ProcesosDB()
        allData = conexion.obtener_productos()
        self.allProducts = allData
        
        # Imprimir los resultados
        for fila in allData:
            self.globalTablaInicio.insert("", "end", values=(fila[0], fila[2], fila[3]))
            
        ventana.mainloop()  # Mantiene la ventana abierta y a la espera de eventos

        print("Mostrar Pantalla principal")  # Imprime un mensaje cuando se abre la ventana
        
    # Método para crear la ventana "Alta"
    def ventanaAlta(self):
        ventana = tk.Tk()  # Crea una nueva ventana
        ventana.title("Ventana Alta")  # Establece el título de la ventana
        ventana.geometry("800x400")  # Define el tamaño de la ventana

        # Almacena la ventana "Alta" en la variable global para futuras referencias
        self.globalVentanaAlta = ventana
        
        ec2L = tk.Label(ventana, text="Nombre")
        ec2L.grid(row=0, column=0, padx=1, pady=1, sticky="ew")
        
        textNombre = tk.Entry(ventana)
        textNombre.grid(row=1, column=0, padx=1, pady=1, sticky="ew")
        
        self.globalNombreProducto = textNombre
        
        ec2L = tk.Label(ventana, text="Precio")
        ec2L.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        
        textPrecio = tk.Entry(ventana)
        textPrecio.grid(row=1, column=1, padx=1, pady=1, sticky="ew")
        self.globalPrecioProducto = textPrecio
        
        btnGuardar = self.btn(ventana, 'Guardar', self.guardarDatosAlta)
        btnGuardar.grid(row=0, column=7, padx=10, pady=10, sticky="ew")
        
        # Crea un botón para cerrar esta ventana y volver a la ventana principal
        btnCerrar = self.btn(ventana, 'Cerrar', self.cerrarVentanaAlta)
        btnCerrar.grid(row=0, column=8, padx=10, pady=10, sticky="ew")
        
        

        ventana.mainloop()  # Inicia el loop para mantener la ventana activa
        print("Mostrar Pantalla Alta")  # Imprime un mensaje cuando se abre la ventana "Alta"
        
    # Método para crear la ventana "Edición"
    def ventanaEdicion(self,nombre,precio):
        ventana = tk.Tk()  # Crea una nueva ventana
        ventana.title("Ventana Edicion")  # Establece el título
        ventana.geometry("800x400")  # Define el tamaño 

        # Almacena la ventana "Edición" en la variable global
        self.globalVentanaEdicion = ventana
        
        ec2L = tk.Label(ventana, text="Nombre")
        ec2L.grid(row=0, column=0, padx=1, pady=1, sticky="ew")
        
        textNombre = tk.Entry(ventana)
        textNombre.grid(row=1, column=0, padx=1, pady=1, sticky="ew")
        textNombre.insert(0, nombre)
        
        self.globalNombreProducto = textNombre
        
        ec2L = tk.Label(ventana, text="Precio")
        ec2L.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
        
        textPrecio = tk.Entry(ventana)
        textPrecio.grid(row=1, column=1, padx=1, pady=1, sticky="ew")
        textPrecio.insert(0, precio)
        self.globalPrecioProducto = textPrecio

        btnGuardar = self.btn(ventana, 'Guardar', self.guardarDatosEdicion)
        btnGuardar.grid(row=0, column=7, padx=10, pady=10, sticky="ew")
        
        btnBorrar = self.btnBorrar(ventana, 'Borrar', self.borrarProducto)
        btnBorrar.grid(row=0, column=8, padx=10, pady=10, sticky="ew")

        # Crea un botón para cerrar esta ventana y volver a la ventana principal
        btnCerrar = self.btn(ventana, 'Cerrar', self.cerrarVentanaEdicion)
        btnCerrar.grid(row=0, column=9, padx=10, pady=10, sticky="ew")

        ventana.mainloop()  # Inicia el loop de la ventana
        print("Mostrar Pantalla Edicion")  # Imprime un mensaje cuando se abre la ventana "Edición"
            
    # Método para crear la ventana "Búsqueda"
    def ventanaBusqueda(self):
        ventana = tk.Tk()  # Crea una nueva ventana
        ventana.title("Ventana Busqueda")  # Establece el título
        ventana.geometry("800x500")  # Define el tamaño

        # Almacena la ventana "Búsqueda" en la variable global
        self.globalVentanaBusqueda = ventana

        # Crea un botón para cerrar esta ventana y volver a la ventana principal
        btnCerrar = self.btn(ventana, 'Cerrar', self.cerrarVentanaBusqueda)
        btnCerrar.grid(row=0, column=7, padx=10, pady=10, sticky="ew")

        ventana.mainloop()  # Inicia el loop de la ventana
        print("Mostrar Pantalla Busqueda")  # Imprime un mensaje cuando se abre la ventana "Búsqueda"
        
    # Método para crear la ventana "Ventas"
    def ventanaVentas(self):
        ventana = tk.Tk()  # Crea una nueva ventana
        ventana.title("Ventana Ventas")  # Establece el título
        ventana.geometry("1000x400")  # Define el tamaño
               

        # Almacena la ventana "Ventas" en la variable global
        self.globalVentanaVentas = ventana

        # Crea un botón para cerrar esta ventana y volver a la ventana principal
        btnCerrar = self.btn(ventana, 'Cerrar', self.cerrarVentanaVentas)
        btnCerrar.grid(row=0, column=7, padx=10, pady=10, sticky="ew")
        
        #tabla de ventas (colocada en el boton de ventas realizadas)
        tabla = ttk.Treeview(ventana, columns=("Código de Barras", "Nombre", "Precio" ,"Fecha"), show="headings")
        tabla.heading("Código de Barras", text="Código de Barras")
        tabla.heading("Nombre", text="Nombre")
        tabla.heading("Precio", text="Precio")
        tabla.heading("Fecha", text="Fecha")
        tabla.grid(row=1, column=1,columnspan=2, padx=10, pady=10, sticky="ew")
       
        conexion = ProcesosDB()
        allData = conexion.obtener_ventas()
        print(allData)
        
        # Imprimir los resultados
        for fila in allData:
            tabla.insert("", "end", values=(fila[0], fila[1], fila[2], fila[3]))

        ventana.mainloop()  # Inicia el loop de la ventana
        print("Mostrar Pantalla Ventas")  # Imprime un mensaje cuando se abre la ventana "Ventas"
        
    # Método que crea un botón personalizado
    def btn(self, ventana, nombre, function):
        # Devuelve un botón con propiedades de estilo y la función que ejecutará al ser clickeado
        return tk.Button(ventana, 
                         text=nombre,  # Texto del botón
                         font=("Helvetica", 12, "bold"),  # Fuente del texto
                         bg="#4CAF50",  # Color de fondo del botón
                         fg="white",  # Color del texto del botón
                         padx=10,  # Padding horizontal
                         pady=5,  # Padding vertical
                         relief="raised",  # Efecto de relieve del botón
                         command=function,  # Función que se ejecutará al hacer clic
                         bd=10)  # Grosor del borde del botón
        
    # Método que crea un botón personalizado
    def btnBorrar(self, ventana, nombre, function):
        # Devuelve un botón con propiedades de estilo y la función que ejecutará al ser clickeado
        return tk.Button(ventana, 
                         text=nombre,  # Texto del botón
                         font=("Helvetica", 12, "bold"),  # Fuente del texto
                         bg="#ef2a21",  # Color de fondo del botón
                         fg="white",  # Color del texto del botón
                         padx=10,  # Padding horizontal
                         pady=5,  # Padding vertical
                         relief="raised",  # Efecto de relieve del botón
                         command=function,  # Función que se ejecutará al hacer clic
                         bd=10)  # Grosor del borde del botón
    
    # Función ejecutada al hacer clic en el botón "Alta"
    def btnAltaClicked(self):
        self.globalVentana.destroy()  # Cierra la ventana principal
        self.ventanaAlta()  # Abre la ventana "Alta"
        print("En boton se ha clickeado alta")  # Mensaje informativo
        
    # Función ejecutada al hacer clic en el botón "Actualizar"
    def btnEdicionClicked(self):
        productoSelecionado = self.globalTablaInicio.focus()
        productoSelecionado = self.globalTablaInicio.item(productoSelecionado)
        self.globalIdActualEdicion = productoSelecionado["values"][0]
        self.globalVentana.destroy()  # Cierra la ventana principal
        
        nombre = productoSelecionado["values"][1]
        precio = productoSelecionado["values"][2]
        self.ventanaEdicion(nombre,precio)  # Abre la ventana "Edición"
        print("En boton se ha clickeado edicion")  # Mensaje informativo
        
    # Función ejecutada al hacer clic en el botón "Búsqueda de Producto"
    def btnBusquedaClicked(self):
        self.globalVentana.destroy()  # Cierra la ventana principal
        self.ventanaBusqueda()  # Abre la ventana "Búsqueda"
        print("En boton se ha clickeado Busqueda")  # Mensaje informativo
        
    # Función ejecutada al hacer clic en el botón "Ventas Realizadas"
    def btnVentasClicked(self):
        self.globalVentana.destroy()  # Cierra la ventana principal
        self.ventanaVentas()  # Abre la ventana "Ventas"
        print("En boton se ha clickeado ventas")  # Mensaje informativo

    # Funciones para cerrar las ventanas individuales y regresar a la ventana principal
    def cerrarVentanaAlta(self):
        self.globalVentanaAlta.destroy()  # Cierra la ventana "Alta"
        self.ventanaPrincipal()  # Vuelve a la ventana principal
        
    def cerrarVentanaEdicion(self):
        self.globalVentanaEdicion.destroy()  # Cierra la ventana "Edición"
        self.ventanaPrincipal()  # Vuelve a la ventana principal
        
    def cerrarVentanaBusqueda(self):
        self.globalVentanaBusqueda.destroy()  # Cierra la ventana "Búsqueda"
        self.ventanaPrincipal()  # Vuelve a la ventana principal
        
    def cerrarVentanaVentas(self):
        self.globalVentanaVentas.destroy()  # Cierra la ventana "Ventas"
        self.ventanaPrincipal()  # Vuelve a la ventana principal

    def guardarDatosAlta(self):
        conexion = ProcesosDB()
        conexion.insertar_producto(self.globalNombreProducto.get() , self.globalPrecioProducto.get() , '')
        self.cerrarVentanaAlta()
        self.ventanaPrincipal()
        #print("Valores Guardar")
        
    def guardarDatosEdicion(self):
        conexion = ProcesosDB()
        conexion.editar_producto(self.globalIdActualEdicion , self.globalNombreProducto.get() , self.globalPrecioProducto.get())
        self.cerrarVentanaEdicion()
        self.ventanaPrincipal()
        #print("Valores Guardar")
        
    def borrarProducto(self):
        conexion = ProcesosDB()
        conexion.borrar_producto(self.globalIdActualEdicion)
        self.cerrarVentanaEdicion()
        self.ventanaPrincipal()
        
    def cancelarVenta(self):
        for item in self.globalTablaVenta.get_children():
            self.globalTablaVenta.delete(item)
        
    def aceptarVenta(self):
        conexion = ProcesosDB()
        
        id = conexion.insertar_venta()
        detalles = self.globalTablaVenta.get_children()
        for item in detalles:
            productoSelecionadoParaVenta = self.globalTablaVenta.item(item)
            conexion.insertar_venta_detalle(id,productoSelecionadoParaVenta["values"][2])
            self.globalTablaVenta.delete(item)
            

            
        
    