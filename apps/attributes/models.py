from apps import db

class Attribute(db.Model):
    attribute_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
    	return 'Attribute {}'.format(self.name)


class AttributeValue(db.Model):
    attribute_value_id = db.Column(db.Integer, primary_key=True)
    attribute_id = db.Column(db.Integer, db.ForeignKey("attribute.attribute_id"))
    value = db.Column(db.String(100))

    def __init__(self, attribute_id, value):
        self.attribute_id = attribute_id
        self.value = value

    def __repr__(self):
        return '{} {}'.format(self.attribute_id, self.value)
        