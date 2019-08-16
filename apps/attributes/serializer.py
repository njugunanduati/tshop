from apps import ma

class AttributeSchema(ma.Schema):
	class Meta:
		fields = ('attribute_id', 'name')