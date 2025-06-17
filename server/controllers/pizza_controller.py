from flask import Blueprint, jsonify
from ..config import db
from ..models.pizza import Pizza

pizza_cntrl = Blueprint('pizza', __name__)

@pizza_cntrl.route('/pizzas', methods=['GET'])
def get_pizza():
    pizzas = Pizza.query.all()

    if not pizzas:
        return jsonify({ "error": "No pizzas found" }), 404
    
    return jsonify([{
        'id': pizza.id,
        'name': pizza.name,
        'ingredients': pizza.ingredients
    } for pizza in pizzas
    ]), 200
