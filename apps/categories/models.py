from apps import db
from apps.departments.models import Department

class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    department_id = db.Column(db.Integer, db.ForeignKey("department.department_id"))
    name = db.Column(db.String(100))
    description = db.Column(db.String(1000))

    def __init__(self, department_id, name, description):
    	self.department_id = department_id
    	self.name = name
    	self.description = description

    def __repr__(self):
    	return 'Category {}'.format(self.name)