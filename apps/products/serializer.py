from apps import ma

class ProductSchema(ma.Schema):
	class Meta:
		fields = ('product_id', 'name', 'description', 'price', 'discounted_price', 'image', 'image_2', 'thumbnail', 'display')