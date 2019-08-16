import os
from flask_restplus import Resource
from apps.categories.serializer import CategorySchema
from apps.categories.models import Category
from apps import api


ns = api.namespace('categories', description='Everything about categories')
			
category_schema = CategorySchema(strict=True)
categories_schema = CategorySchema(many=True, strict=True)


@ns.route('/')
class CategoriesListResource(Resource):
	def get(self, category_id=None):
		categories = Category.query.all()
		return categories_schema.jsonify(categories)


@ns.route('/<category_id>')
class CategoryResource(Resource):
	def get(self):
		category = Category.query.get(category_id)
		return category_schema.jsonify(category)