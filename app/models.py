from app.database import get_db

class Producto:
    def __init__(self, id_producto=None, nombre=None, precio=None, url_imagen=None):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.url_imagen = url_imagen

    @staticmethod
    def get_by_id(producto_id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM productos WHERE id_producto = %s", (producto_id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Producto(id_producto=row[0], nombre=row[1], precio=row[2], url_imagen=row[3])
        return None
    
    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM productos")
        rows = cursor.fetchall()
        productos = [Producto(id_producto=row[0], nombre=row[1], precio=row[2], url_imagen=row[3]) for row in rows]
        cursor.close()
        return productos
    
    def serialize (self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio,
            "url_imagen": self.url_imagen,
        }
    
    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id_producto:
            query = """
                UPDATE productos SET nombre = %s, precio = %s, url_imagen = %s
                WHERE id_producto = %s
            """
            cursor.execute(query, (self.nombre, self.precio, self.url_imagen, self.id_producto))
        else:
            cursor.execute("""
                INSERT INTO productos (nombre, precio, url_imagen) VALUES (%s, %s, %s)
            """, (self.nombre, self.precio, self.url_imagen))
            self.id_producto = cursor.lastrowid
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM productos WHERE id_producto = %s", (self.id_producto,))
        db.commit()
        cursor.close()

