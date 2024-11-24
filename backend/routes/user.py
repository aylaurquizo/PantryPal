from flask import Flask, jsonify, request
from supabase import Client
from db_utils import get_db_connection

def UserRoutes(app: Flask, supabase: Client):
    @app.route('/add_ingredient', methods=['POST'])
    def add_ingredient():
        print("Added ingredient")
        data = request.json
        print(data)
        user_id = data.get('user_id')
        ingredient_name = data.get('ingredient_name')

        if not user_id or not ingredient_name:
            return jsonify({"error": "Missing user_id or ingredient_name"}), 400

        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                # Insert the ingredient into the Ingredients table if it doesn't exist
                cursor.execute(
                    "INSERT IGNORE INTO Ingredients (ingredient_name) VALUES (%s)", 
                    (ingredient_name,)
                )
                connection.commit()

                # Get the ingredient ID
                cursor.execute(
                    "SELECT ingredient_id FROM Ingredients WHERE ingredient_name = %s", 
                    (ingredient_name,)
                )
                ingredient_id = cursor.fetchone()['ingredient_id']

                # Link the ingredient to the user in UserIngredients
                cursor.execute(
                    "INSERT IGNORE INTO UserIngredients (user_id, ingredient_id) VALUES (%s, %s)",
                    (user_id, ingredient_id)
                )
                connection.commit()

            return jsonify({"message": "Ingredient added successfully"}), 201
        finally:
            connection.close()

