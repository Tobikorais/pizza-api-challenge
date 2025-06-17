from ..config import db
from sqlalchemy.orm import validates

class RestaurantPizza(db.Model):
    __tablename__ = 'restaurant_pizzas'

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)

    # FK
    restaurant_id = db.Column(db.Integer(),db.ForeignKey('restaurants.id'))
    pizza_id = db.Column(db.Integer(),db.ForeignKey('pizzas.id'))

    # relationships
    restaurant = db.relationship('Restaurant',back_populates = 'pizzas')
    pizza = db.relationship('Pizza',back_populates = 'restaurant_pizzas')


    @validates('price')
    def validate_price(self, key, price):
        if not 1 <= price <= 30:
            raise ValueError("Price must be between 1 and 30")
        return price

    def __repr__(self):
        return f"<Pizza {self.name}>"