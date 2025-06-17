from .app import app
from .config import db
from .models.restaurant import Restaurant
from .models.pizza import Pizza
from .models.restaurant_pizza import RestaurantPizza

def seed_data():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Sample data
        restaurants = [
            Restaurant(name="Pizza Heaven", address="123 Cloud Street"),
            Restaurant(name="Mario's", address="456 Mushroom Road")
        ]
        db.session.add_all(restaurants)

        pizzas = [
            Pizza(name="Margherita", ingredients="Tomato, Mozzarella, Basil"),
            Pizza(name="Pepperoni", ingredients="Tomato, Mozzarella, Pepperoni")
        ]
        db.session.add_all(pizzas)
        db.session.commit()

        # Create associations
        restaurant_pizzas = [
            RestaurantPizza(price=10, restaurant_id=1, pizza_id=1),
            RestaurantPizza(price=12, restaurant_id=1, pizza_id=2),
            RestaurantPizza(price=11, restaurant_id=2, pizza_id=1)
        ]
        db.session.add_all(restaurant_pizzas)
        db.session.commit()
        print("✅ Database seeded successfully!")

if __name__ == '__main__':
    seed_data()