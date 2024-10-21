from DB import DBConexion

class ProcesosDB:
    conexionGlobal = None
    def __init__(self) -> None:
        conexionDB = DBConexion()
        conexionGlobal = conexionDB.obtener_cursor()
        pass
    
    
    def insertar_producto(self,descripcion, precio, codigoBarras):
        conexionDB = DBConexion()
        cursor = conexionDB.obtener_cursor()

        if cursor:
            try:
                sql_insert_query = "INSERT INTO productos (descripcion, precio,codigo_barras) VALUES (%s, %s, %s)"
                cursor.execute(sql_insert_query, (descripcion, precio,codigoBarras))
                conexionDB.conexionGlobal.commit()
                print("Producto insertado correctamente")
            except Error as e:
                print(f"Error al insertar producto: {e}")
            finally:
                cursor.close()

        conexionDB.cerrar_conexion()
        
    def editar_producto(self,id,descripcion, precio):
        conexionDB = DBConexion()
        cursor = conexionDB.obtener_cursor()

        if cursor:
            try:
                sql_insert_query = "update productos set descripcion = %s , precio = %s where id_productos = %s"
                cursor.execute(sql_insert_query, (descripcion, precio, id))
                conexionDB.conexionGlobal.commit()
                print("Producto insertado correctamente")
            except Error as e:
                print(f"Error al insertar producto: {e}")
            finally:
                cursor.close()

        conexionDB.cerrar_conexion()
        
    def borrar_producto(self,id):
        conexionDB = DBConexion()
        cursor = conexionDB.obtener_cursor()

        if cursor:
            try:
                sql_insert_query = "delete from productos where id_productos = %s"
                cursor.execute(sql_insert_query, (id,))
                conexionDB.conexionGlobal.commit()
                print("Producto insertado correctamente")
            except IOError as e:
                print(f"Error al insertar producto: {e}")
            finally:
                cursor.close()

        conexionDB.cerrar_conexion()
    
    def insertar_venta(self):
        conexionDB = DBConexion()
        cursor = conexionDB.obtener_cursor()

        if cursor:
            try:
                sql_insert_query = "INSERT INTO ventas (fecha) VALUES (NOW())"
                cursor.execute(sql_insert_query)
                conexionDB.conexionGlobal.commit()
                
                # Obtener el ID generado
                id_generado = cursor.lastrowid
                print(f"Venta insertada correctamente con ID: {id_generado}")
                return id_generado  # Opcional: devolver el ID generado
                
            except Error as e:
                print(f"Error al insertar Venta: {e}")
            finally:
                cursor.close()

        conexionDB.cerrar_conexion()
    
    def insertar_venta_detalle(self,id_venta,id_producto):
        conexionDB = DBConexion()
        cursor = conexionDB.obtener_cursor()

        if cursor:
            try:
                sql_insert_query = "INSERT INTO ventasDetalle (id_venta,id_productos) VALUES (%s,%s)"
                cursor.execute(sql_insert_query, (id_venta,id_producto,))
                conexionDB.conexionGlobal.commit()
                print("Venta insertado correctamente")
            except Error as e:
                print(f"Error al insertar Venta: {e}")
            finally:
                cursor.close()

        conexionDB.cerrar_conexion()
        
    def obtener_productos(self):
        conexionDB = DBConexion()
        cursor = conexionDB.obtener_cursor()

        if cursor:
            try:
                cursor.execute("SELECT * FROM productos")
                return cursor.fetchall()
            except OSError as e:
                print(f"Error al insertar Venta: {e}")
            finally:
                cursor.close()

        conexionDB.cerrar_conexion()    

    def obtener_ventas(self):
        conexionDB = DBConexion()
        cursor = conexionDB.obtener_cursor()

        if cursor:
            try:
                cursor.execute("select t2.id_productos,descripcion , precio , fecha from ventasDetalle as t1 join productos as t2 on t1.id_productos = t2.id_productos")
                return cursor.fetchall()
            except OSError as e:
                print(f"Error al insertar Venta: {e}")
            finally:
                cursor.close()

        conexionDB.cerrar_conexion()