import os
from flask_restplus import Resource
from apps.attributes.serializer import AttributeSchema
from apps.attributes.models import Attribute
from apps import api

ns = api.namespace('attributes', description='Everything about attributes')
			
attribute_schema = AttributeSchema(strict=True)
attributes_schema = AttributeSchema(many=True, strict=True)

@ns.route('/')
class AttributesListResource(Resource):
	def get(self):
		attributes = Attribute.query.all()
		return attributes_schema.jsonify(attributes)


@ns.route('/<attribute_id>')
class AttributeResource(Resource):
	def get(self, attribute_id=None):
		attributes = Attribute.query.all()
		return attributes_schema.jsonify(attributes)