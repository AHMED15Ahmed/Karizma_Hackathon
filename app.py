from flask import Flask, render_template, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
jwt = JWTManager(app)

# Structure de données en mémoire pour stocker temporairement les recettes
recipes_data = [
    {'id': 1, 'name': 'Recette 1', 'ingredients': 'Ingrédients 1', 'preparation_time': '30 minutes'},
    {'id': 2, 'name': 'Recette 2', 'ingredients': 'Ingrédients 2', 'preparation_time': '45 minutes'}
]

# Fonction utilitaire pour obtenir les recettes d'un utilisateur
def get_user_recipes(user_id):
    return [recipe for recipe in recipes_data if recipe['user_id'] == user_id]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/recipes', methods=['GET'])
@jwt_required()
def get_recipes():
    current_user = get_jwt_identity()
    user_recipes = get_user_recipes(current_user)
    return jsonify(recipes=user_recipes), 200

if __name__ == '__main__':
    app.run(debug=True)
