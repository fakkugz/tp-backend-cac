from flask import Flask
from app.database import init_app
from app.views import *
from flask_cors import CORS

app = Flask(__name__)

init_app(app)
CORS(app, resources={r"/*": {"origins": "*"}}) 

app.route("/gestion/", methods=["GET"])(get_all_products)
app.route("/tienda/", methods=["GET"])(get_all_products)
app.route("/gestion/<int:product_id>", methods=["GET"])(get_product)
app.route("/gestion/", methods=["POST"])(create_product)
app.route("/gestion/<int:product_id>", methods=["PUT"])(update_product)
app.route('/gestion/<int:product_id>', methods=['DELETE'])(delete_product)

if __name__ == "__main__":
    app.run(debug=True)