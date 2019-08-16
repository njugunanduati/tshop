from apps import ma

class CategorySchema(ma.Schema):
	class Meta:
		fields = ('category_id', 'department_id', 'name', 'description')