from apps import ma

class ShippingSchema(ma.Schema):
	class Meta:
		fields = ('shipping_id', 'shipping_type', 'shipping_cost', 'shipping_region_id')


class ShippingRegionSchema(ma.Schema):
	class Meta:
		fields = ('shipping_region_id', 'shipping_region')
