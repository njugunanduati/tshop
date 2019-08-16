#!/usr/bin/python3.6
import pymysql
from flask import Flask, Blueprint
from flask_restplus import Api
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from config import Config


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)  
ma = Marshmallow(app)
api = Api(app, version='1.0', title='Turing ECommerce API',
          description='Official documentation about Turing Ecommerce API.')


def register_blueprints(app):
	from apps.departments.views import ns as departments_namespace
	from apps.categories.views import ns as categories_namespace
	from apps.attributes.views import ns as attributes_namespace
	from apps.products.views import ns as products_namespace
	from apps.customers.views import ns as customers_namespace
	from apps.shipping.views import ns as shipping_namespace

	blueprint = Blueprint('api', __name__, url_prefix='/api')
	api.init_app(blueprint)
	api.add_namespace(departments_namespace)
	api.add_namespace(categories_namespace)
	api.add_namespace(attributes_namespace)
	api.add_namespace(products_namespace)
	api.add_namespace(shipping_namespace)
	app.register_blueprint(blueprint)
	return app


register_blueprints(app)

if __name__ == '__main__':
	app.run()