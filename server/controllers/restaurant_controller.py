
from flask import Blueprint, jsonify
from ..config import db
from ..models.restaurant import Restaurant

restaurant_cntrl = Blueprint('restaurant', __name__)

@restaurant_cntrl.route('/', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    result = []
    for restaurant in restaurants:
        result.append({
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address
        })
    return jsonify(result), 200

@restaurant_cntrl.route('/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)

    if not restaurant:
        return jsonify({ "error": "Restaurant not found" }), 404
    
    pizzas = [{
        'id': rp.pizza.id,
        'name': rp.pizza.name,
        'ingredients': rp.pizza.ingredients,
        'price': rp.price
    }for rp in restaurant.pizzas]

    return jsonify ({
        'id': restaurant.id,
        'name': restaurant.name,
        'address': restaurant.address,
        'pizzas': pizzas
    }), 200

@restaurant_cntrl.route('/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)

    if not restaurant:
        return jsonify({ "error": "Restaurant not found" }), 404
    
    db.session.delete(restaurant)
    db.session.commit()
    return '', 204