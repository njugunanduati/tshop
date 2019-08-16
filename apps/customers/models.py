from apps import db
from apps.shipping.models import ShippingRegion

class Customer(db.Model):
    customer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(150))
    password = db.Column(db.String(50))
    credit_card = db.Column(db.Text)
    address_1 = db.Column(db.String(100))
    address_2 = db.Column(db.String(100))
    city = db.Column(db.String(100))
    region = db.Column(db.String(100))
    postal_code = db.Column(db.String(100))
    country = db.Column(db.String(100))
    shipping_region_id = db.Column(db.Integer, db.ForeignKey("shipping_region.shipping_region_id"))
    day_phone = db.Column(db.String(100))
    eve_phone = db.Column(db.String(100))
    mob_phone = db.Column(db.String(100))


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


