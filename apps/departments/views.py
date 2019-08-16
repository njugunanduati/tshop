import os
from flask_restplus import Resource
from apps.departments.serializer import DepartmentSchema
from apps.departments.models import Department
from apps import api


ns = api.namespace('departments', description='Everything about departments')

			
department_schema = DepartmentSchema(strict=True)
departments_schema = DepartmentSchema(many=True, strict=True)

@ns.route('/')
class DepartmentsListResource(Resource):
	def get(self):
		departments = Department.query.all()
		return departments_schema.jsonify(departments)

@ns.route('/<department_id>')
class DepartmentResource(Resource):
	def get(self, department_id=None):
		department = Department.query.get(department_id)
		return department_schema.jsonify(department)
