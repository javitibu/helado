# -------------------------------------------------------------------
# Escribimos una serie de funciones para crear una pequeña app que
# maneje un arreglo que contenga datos de productos.
#
# Nuestras funciones harán lo siguiente:
#
# - Agregar un producto al arreglo
# - Consultar un producto a partir de su código
# - Modificar los datos de un producto a partir de su código
# - Obtener un listado de los productos que existen en el arreglo.
# - Eliminar un producto de la lista
#
# Cada producto tiene:
#
# - codigo: int, código numérico del producto.
# - descripcion: str, descripción alfabética del producto.
# - cantidad: int, cantidad en stock del producto.
# - precio: float, precio de venta del producto.
# - imagen: str, nombre de la imagen del producto.
# - proveedor: int, número de proveedor del producto.
# -------------------------------------------------------------------
import mysql.connector

class Catalogo:
    #catalogo = []

    # -------------------------------------------------------------------
    # Funcion que añade un producto a la lista
    # -------------------------------------------------------------------
    def __init__(self, host, user, password, db ):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=db
        )
        self.cursor = self.conn.cursor(dictionary=True)
        try:
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS productos (
                    codigo INT,
                    descripcion VARCHAR(255) NOT NULL,
                    cantidad INT,
                    precio DECIMAL(10,2) NOT NULL,
                    imagen_url VARCHAR(255),
                    proveedor INT(2)
                    );'''
                )
            self.conn.commit()
        except:
            print("Exploto el verano!!!!!!")

    # -------------------------------------------------------------------
    # Funcion que añade un producto a la lista
    # -------------------------------------------------------------------
    def agregar_producto(self, cod, des, can, pre, ima, pro):
        self.cursor.execute(f"SELECT * FROM productos WHERE codigo = {cod};")
        resultado = self.cursor.fetchone()
        if resultado:
            return False
        else:
            aux = f"INSERT INTO productos \
               (codigo, descripcion, cantidad, precio, imagen_url, proveedor) \
               VALUES \
               ({cod}, '{des}', {can}, {pre}, '{ima}', {pro});"
            self.cursor.execute(aux)
            self.conn.commit()
            return True
    
    # -------------------------------------------------------------------
    # Funcion lista los productos
    # -------------------------------------------------------------------
    def listar_producto(self):
        print("-"*30)
        for producto in self.catalogo:
            print(f"      Codigo: {producto['codigo']}")
            print(f" Descripción: {producto['descrip']}")
            print(f"    Cantidad: {producto['stock']}")
            print(f"Valor unidad: {producto['precio']}")
            print(f"  URL Imagen: {producto['foto']}")
            print(f"   Proveedor: {producto['prove']}")
            print("-"*30)

    # -------------------------------------------------------------------
    # Funcion eliminar un producto
    # -------------------------------------------------------------------
    def eliminar_producto(self,cod):
        self.cursor.execute(f"DELETE FROM productos WHERE codigo = {cod};")
        self.conn.commit()
        return self.cursor.rowcount > 0

    # -------------------------------------------------------------------
    # Funcion que devuelve los datos de un producto
    # -------------------------------------------------------------------
    def consultar_producto(self, cod):
        self.cursor.execute(f"SELECT * FROM productos WHERE codigo = {cod};")
        resultado = self.cursor.fetchone()
        return resultado

    # -------------------------------------------------------------------
    # Funcion que muestra un producto
    # -------------------------------------------------------------------
    def mostrar_producto(self, producto):
        print("-"*30)
        print(f"      Codigo: {producto['codigo']}")
        print(f" Descripción: {producto['descripcion']}")
        print(f"    Cantidad: {producto['cantidad']}")
        print(f"Valor unidad: {producto['precio']}")
        print(f"  URL Imagen: {producto['imagen_url']}")
        print(f"   Proveedor: {producto['proveedor']}")
        print("-"*30)



# -------------------------------------------------------------------
# Programa principal
# -------------------------------------------------------------------
print("\033[H\033[J")  # Limpiamos la pantalla

mi_lista1 = Catalogo('Laraujo.mysql.pythonanywhere.com', 'Laraujo', 'grupo5!!', 'Laraujo$postulandes')
# mi_lista2 = Catalogo()

#print(mi_lista1.agregar_producto(1, "TV color 14", 1, 300, "old_tv.jpg", 3))
#print(mi_lista1.agregar_producto(2, "TV color 32", 2, 3000, "super_tv.jpg", 3))
#print(mi_lista1.eliminar_producto(1))

a = mi_lista1.consultar_producto(1)
mi_lista1.mostrar_producto(a)


# mi_lista1.listar_producto()
# mi_lista1.mostrar_producto(1)