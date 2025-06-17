from flask import Blueprint, jsonify, request
from ..config import db
from ..models.restaurant_pizza import RestaurantPizza
from ..models.restaurant import Restaurant
from ..models.pizza import Pizza

restaurant_pizza_cntrl = Blueprint('restairant_pizza', __name__)

@restaurant_pizza_cntrl.route('/restaurant_pizzas', methods=['POST'])
def create_RestaurantPizza():
    data = request.get_json()
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    if price is None or pizza_id is None or restaurant_id is None:
        return jsonify({"errors": ["Missing required fields."]}), 400

    if not (1 <= price <= 30):
        return jsonify({"errors": ["Price must be between 1 and 30"]}), 400

    pizza = Pizza.query.get(pizza_id)
    restaurant = Restaurant.query.get(restaurant_id)
    if not pizza or not restaurant:
        return jsonify({"errors": ["Invalid pizza_id or restaurant_id"]}), 400

    restaurant_pizza = RestaurantPizza()
    restaurant_pizza.price = price
    restaurant_pizza.pizza_id = pizza_id
    restaurant_pizza.restaurant_id = restaurant_id
    db.session.add(restaurant_pizza)
    db.session.commit()

    response = {
        "id": restaurant_pizza.id,
        "price": restaurant_pizza.price,
        "pizza_id": restaurant_pizza.pizza_id,
        "restaurant_id": restaurant_pizza.restaurant_id,
        "pizza": {
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        },
        "restaurant": {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address
        }
    }
    return jsonify(response), 201

@restaurant_pizza_cntrl.route('/restaurant_pizzas', methods=['GET'])
def get_all_REstaurantPizzas():
    restaurant_pizzas = RestaurantPizza.query.all()
    
    if not restaurant_pizzas:
        return jsonify({"error": "No RestaurantPizzas found"}), 404

    response = []
    for rp in restaurant_pizzas:
        pizza = Pizza.query.get(rp.pizza_id)
        restaurant = Restaurant.query.get(rp.restaurant_id)

        if not pizza or not restaurant:
            continue  

        response.append({
            "id": rp.id,
            "price": rp.price,
            "pizza_id": rp.pizza_id,
            "restaurant_id": rp.restaurant_id,
            "pizza": {
                "id": pizza.id,
                "name": pizza.name,
                "ingredients": pizza.ingredients
            },
            "restaurant": {
                "id": restaurant.id,
                "name": restaurant.name,
                "address": restaurant.address
            }
        })
    
    return jsonify(response), 200