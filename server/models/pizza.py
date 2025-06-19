"""Pizza model for Pizza API."""
"""Pizza model for Pizza API."""
"""Pizza model for Pizza API."""
"""Pizza model for Pizza API."""
"""Pizza model for Pizza API."""
"""Pizza model for Pizza API."""
from ..config import db

class Pizza(db.Model):
    __tablename__ = 'pizzas'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    ingredients = db.Column(db.String())

    restaurant_pizzas = db.relationship('RestaurantPizza', back_populates='pizza')

    def __repr__(self):
        return f"<Pizza {self.name}>"