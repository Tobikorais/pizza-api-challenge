from flask import Flask
from flask_migrate import Migrate
from server.config import db  

def create_app():
    flask_app = Flask(__name__)
    flask_app.config.from_object('server.config.Config')
    
    # Database and migrations
    db.init_app(flask_app)
    Migrate(flask_app, db) 
    
    with flask_app.app_context():
        # Import models 
        from server.models.pizza import Pizza as PizzaModel
        from server.models.restaurant import Restaurant as RestaurantModel
        from server.models.restaurant_pizza import RestaurantPizza as RestaurantPizzaModel
        
        # Register blueprints 
        from server.controllers.pizza_controller import pizza_cntrl as pizza_blueprint
        from server.controllers.restaurant_controller import restaurant_cntrl as restaurant_blueprint
        from server.controllers.restaurant_pizza_controller import restaurant_pizza_cntrl as rp_blueprint
        
        flask_app.register_blueprint(pizza_blueprint, url_prefix='/api/pizzas')
        flask_app.register_blueprint(restaurant_blueprint, url_prefix='/api/restaurants')
        flask_app.register_blueprint(rp_blueprint, url_prefix='/api/restaurant-pizzas')

    return flask_app

app = create_app()
@app.route('/')
def home():
    return 'Index for Restaurant/pizza/RestaurantPizzas'
if __name__ == '__main__':
    app.run(port=5555, debug=True)