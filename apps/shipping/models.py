from apps import db

class Shipping(db.Model):
    shipping_id = db.Column(db.Integer, primary_key=True)
    shipping_type = db.Column(db.String(100))
    shipping_cost = db.Column(db.Numeric(10, 2))
    shipping_region_id = db.Column(db.Integer, db.ForeignKey("shipping_region.shipping_region_id"))

    def __init__(self, shipping_type, shipping_cost, shipping_region_id):
        self.shipping_type = shipping_type
        self.shipping_cost = shipping_cost
        self.shipping_region_id = shipping_region_id


    def __repr__(self):
    	return '{} {} {} {}'.format(self.shipping_id , self.shipping_type, self.shipping_cost, self.shipping_region_id)


class ShippingRegion(db.Model):
    shipping_region_id = db.Column(db.Integer, primary_key=True)
    shipping_region = db.Column(db.String(100))

    def __init__(self, shipping_region):
        self.shipping_region = shipping_region

    def __repr__(self):
        return 'Shipping region is {}'.format(self.shipping_region)