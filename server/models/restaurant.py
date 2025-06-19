# Relationship: Restaurant has many RestaurantPizzas
"""Restaurant model for Pizza API."""
# Relationship: Restaurant has many RestaurantPizzas
"""Restaurant model for Pizza API."""
# Relationship: Restaurant has many RestaurantPizzas
"""Restaurant model for Pizza API."""
# Relationship: Restaurant has many RestaurantPizzas
"""Restaurant model for Pizza API."""
# Relationship: Restaurant has many RestaurantPizzas
"""Restaurant model for Pizza API."""
# Relationship: Restaurant has many RestaurantPizzas
"""Restaurant model for Pizza API."""
from server.config import db  

class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(100))
    
    pizzas = db.relationship('RestaurantPizza', back_populates='restaurant', cascade='all, delete-orphan')