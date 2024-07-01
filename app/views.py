from flask import jsonify, request
from app.models import Producto


def get_all_products():
    productos = Producto.get_all()
    list_productos = [producto.serialize() for producto in productos]
    return jsonify(list_productos)

def get_product(product_id):
    product = Producto.get_by_id(product_id)
    if not product:
        return jsonify({'message': 'product not found'}), 404
    return jsonify(product.serialize())

def create_product():
    data = request.json
    #validacion
    new_product= Producto(None, data["nombre"], data["precio"], data["url_imagen"])
    new_product.save()
    return jsonify({"message":"Producto agregado"}), 201

def update_product(product_id):
    product = Producto.get_by_id(product_id)
    if not product:
        return jsonify({'message': 'product not found'}), 404
    data = request.json
    product.nombre = data['nombre']
    product.precio = data['precio']
    product.url_imagen = data['url_imagen']
    product.save()
    return jsonify({'message': 'product updated successfully'})

def delete_product(product_id):
    product = Producto.get_by_id(product_id)
    if not product:
        return jsonify({'message': 'product not found'}), 404
    product.delete()
    return jsonify({'message': 'product deleted successfully'})