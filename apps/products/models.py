from apps import db
from apps.attributes.models import AttributeValue
from apps.categories.models import Category

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    price = db.Column(db.Numeric(10,2))
    discounted_price = db.Column(db.Numeric(10,2))
    image = db.Column(db.String(150))
    image_2 = db.Column(db.String(150))
    thumbnail = db.Column(db.String(150))
    display = db.Column(db.Integer)

    def __init__(self, name, description, price, discounted_price, image, image_2, thumbnail, display):
        self.name = name
        self.description = description
        self.price = price
        self.discounted_price = discounted_price
        self.image = image
        self.image_2 = image_2
        self.thumbnail = thumbnail
        self.display = display

    def __repr__(self):
    	return '{} {}'.format(self.name, self.description)


class ProductAttribute(db.Model):
    product_id = db.Column(db.Integer, db.ForeignKey("product.product_id"), primary_key=True)
    attribute_value_id = db.Column(db.Integer, db.ForeignKey("attribute_value.attribute_value_id"))

    def __init__(self, attribute_value_id):
        self.attribute_value_id = attribute_value_id

    def __repr__(self):
        return '{} {}'.format(self.product_id, self.attribute_value_id)


class ProductCategoty(db.Model):
    product_id = db.Column(db.Integer, db.ForeignKey("product.product_id"), primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey("category.category_id"))

    def __init__(self, category_id):
        self.category_id = category_id

    def __repr__(self):
        return '{} {}'.format(self.product_id, self.category_id)