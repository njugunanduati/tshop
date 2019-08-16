from apps import ma

class DepartmentSchema(ma.Schema):
	class Meta:
		fields = ('department_id', 'name', 'description')