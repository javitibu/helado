import mysql.connector

class Catalogo:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="trabajanosotros")
        
        self.cursor = self.conn.cursor(dictionary=True)
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS trabajanosotros (
            codigo INT,
            apellido VARCHAR(255) NOT NULL,
            nombre VARCHAR(255) NOT NULL,
            correo VARCHAR(255) NOT NULL,
            telefono INT NOT NULL,
            comentario VARCHAR(500) NOT NULL,
            cv_url VARCHAR(255)NOT NULL,
            edad INT NOT NULL
            )''')
        self.conn.commit()

    def agregar_postulante(self, codigo, apellido, nombre, correo, telefono, comentario, edad, CV):
        self.cursor.execute("SELECT * FROM trabajanosotros WHERE codigo = %s", (codigo,))
        postulante_existe = self.cursor.fetchone()
        if postulante_existe:
            return False
    
        sql = "INSERT INTO trabajanosotros \
           (codigo, apellido, nombre, correo, telefono, comentario, cv_url, edad) \
           VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (codigo, apellido, nombre, correo, telefono, comentario, CV, edad)
    
        self.cursor.execute(sql, values)
        self.conn.commit()
        return True 
    #----------------------------------------------------------------
    def consultar_postulante(self, codigo):
        self.cursor.execute(f"SELECT * FROM trabajanosotros WHERE codigo = {codigo}")
        return self.cursor.fetchone()
    
    def modificar_postulante(self, codigo, nuevo_apellido, nuevo_nombre, nuevo_correo, nuevo_telefono, nuevo_comentario, nuevo_CV, nueva_edad):
        sql = "UPDATE trabajanosotros SET \
                apellido = %s, \
                nombre = %s, \
                correo = %s, \
                telefono = %s, \
                comentario = %s, \
                cv_url = %s, \
                edad = %s \
            WHERE codigo = %s"
    
        values = (nuevo_apellido, nuevo_nombre, nuevo_correo, nuevo_telefono, nuevo_comentario, nuevo_CV, nueva_edad, codigo)
    
        self.cursor.execute(sql, values)
        self.conn.commit()
        return self.cursor.rowcount > 0

    def listar_postulantes(self):
        self.cursor.execute("SELECT * FROM trabajanosotros")
        postulantes = self.cursor.fetchall()
        print("-" * 40)
        for postulante in postulantes:
            print(f"Código.....: {postulante['codigo']}")
            print(f"apellido: {postulante['apellido']}")
            print(f"nombre...: {postulante['nombre']}")
            print(f"telefono.....: {postulante['telefono']}")
            print(f"correo.....: {postulante['correo']}")
            print(f"comentario.....: {postulante['comentario']}")
            print(f"CV.....: {postulante['cv_url']}")
            print(f"edad..: {postulante['edad']}")
            print("-" * 40)

    def eliminar_postulante(self, codigo):
        self.cursor.execute("DELETE FROM trabajanosotros WHERE codigo = %s", (codigo,))
        self.conn.commit()
        return self.cursor.rowcount > 0

    def mostrar_postulante(self, codigo):
        postulante = self.consultar_postulante(codigo)
        if postulante:
            print("-" * 40)
            print(f"Código.....: {postulante['codigo']}")
            print(f"apellido: {postulante['apellido']}")
            print(f"nombre...: {postulante['nombre']}")
            print(f"telefono.....: {postulante['telefono']}")
            print(f"correo.....: {postulante['correo']}")
            print(f"comentario.....: {postulante['comentario']}")
            print(f"CV.....: {postulante['cv_url']}")
            print(f"edad..: {postulante['edad']}")
            print("-" * 40)
        else:
            print("Postulante no encontrado.")

# Ejemplo de uso con MariaDB
catalogo = Catalogo(host='127.0.0.1', user='root', password='', database='trabajanosotros')

# Agregamos productos a la tabla
#catalogo.agregar_postulante(1, 'Araujo', 'Leandro', 'leandrojosearaujo@gmail.com', 1154853541,'Listo para trabajar', 'CV_12345', 40)
#catalogo.agregar_postulante(2, 'Michelini Campos', 'Gregorio', 'gmichelinicampos@gmail.com', 250025000,  'Quiero laburar en una heladeria ahora que viene el calorcito', 'CV_56789', 39)
#catalogo.agregar_postulante(3, 'Buron', 'Javier Alejandro', 'javierburon@gmail.com', 55555000,  'Ya que tengo que montar guardia, prefiero montarla en una heladeria!', 'CV_999999', 29)
#catalogo.agregar_postulante(4, 'Zamudio', 'Facundo', 'leandrojosearaujo@gmail.com', 1154853541,'Los sueños de mi vida son 1-Trabajar en esta empresa. 2-Ganar un mundial', 'CV_12345', 38)
#catalogo.agregar_postulante(5, 'Sztejnberg', 'Delia Karina', 'ksztejnberg@gmail.com', 1154855450,'Holgazanear no es una opcion, dejar helado sin probar, tampoco', 'CV_123455093', 30)
#catalogo.agregar_postulante(6,'Velazquez Fariña', 'Karen Romina', 'karenrovelaf@gmail.com',  445566677788,  'Helados y democracia', 26, 'CV_13141516')

# Consultamos un postulante y lo mostramos
postulante = catalogo.consultar_postulante(1)
if postulante:
    print(f"Postulante encontrado: {postulante['apellido']}")
else:
    print("Postulante no encontrado.")

# Modificamos un postulante y lo mostramos
catalogo.modificar_postulante(1, 'Sztejnberg', 'Delia Karina', 'ksztejnberg@gmail.com', 1154855450,'Holgazanear no es una opcion, dejar helado sin probar, tampoco', 'CV_123455093', 30)
#catalogo.modificar_postulante(4, 'Zamudio', 'Facundo', 'leandrojosearaujo@gmail.com', 1154853541,'Los sueños de mi vida son 1-Trabajar en esta empresa. 2-Ganar un mundial', 'CV_12345', 38)
#catalogo.modificar_postulante(3, 'Buron', 'Javier Alejandro', 'javierburon@gmail.com', 55555000,  'Ya que tengo que montar guardia, prefiero montarla en una heladeria!', 'CV_999999', 29)

# Listamos todos los postulantes
#catalogo.listar_postulantes()

# Eliminamos un postulante
#catalogo.eliminar_postulante(6)
#catalogo.mostrar_postulante(4)
