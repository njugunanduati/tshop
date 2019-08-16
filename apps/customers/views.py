import os
from flask_restplus import Resource
from apps.products.serializer import ProductSchema
from apps.products.models import Product
from apps import api


ns = api.namespace('products', description='Everything about products')

			
product_schema = ProductSchema(strict=True)
products_schema = ProductSchema(many=True, strict=True)

@ns.route('/')
class ProductsListResource(Resource):
	def get(self):
		products = Product.query.all()
		return products_schema.jsonify(products)

@ns.route('/<product_id>')
class ProductResource(Resource):
	def get(self, product_id=None):
		product = Product.query.get(product_id)
		return products_schema.jsonify(department)
