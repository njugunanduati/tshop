import os
from flask_restplus import Resource
from apps.shipping.serializer import ShippingSchema, ShippingRegionSchema
from apps.shipping.models import Shipping, ShippingRegion
from apps.products.models import Product
from apps import api


ns = api.namespace('shipping', description='Everything about shipping')

			
shipping_schema = ShippingSchema(strict=True)
shippings_schema = ShippingSchema(many=True, strict=True)

shipping_region_schema = ShippingRegionSchema(strict=True)
shipping_regions_schema = ShippingRegionSchema(many=True, strict=True)

@ns.route('/regions')
class ShippingRegionsResource(Resource):
	def get(self):
		shipping_regions = ShippingRegion.query.all()
		return shipping_regions_schema.jsonify(shipping_regions)

@ns.route('/regions/<shipping_region_id>')
class ShippingResource(Resource):
	def get(self, shipping_region_id):
		shipping = Shipping.query.filter_by(shipping_region_id=shipping_region_id).all()
		return shipping_schema.jsonify(shipping)
