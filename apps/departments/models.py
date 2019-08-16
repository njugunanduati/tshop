from apps import db

class Department(db.Model):
    department_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(1000))

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
    	return 'Department name is {}'.format(self.name)