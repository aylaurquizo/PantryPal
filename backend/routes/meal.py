from flask import Flask, jsonify
from supabase import Client
from db_utils import get_db_connection

def MealRoutes(app: Flask, supabase: Client):
    import requests
    @app.route('/fetch_meals', methods=['GET'])
    def fetch_meals():
        api_url = "https://www.themealdb.com/api/json/v1/1/search.php?s="
        response = requests.get(api_url)
        if response.status_code != 200:
            return jsonify({"error": "Failed to fetch meals"}), 500

        meals_data = response.json().get('meals', [])
        connection = get_db_connection()
        try:
            with connection.cursor() as cursor:
                for meal in meals_data:
                    meal_name = meal['strMeal']
                    meal_description = meal.get('strCategory', '')
                    instructions = meal.get('strInstructions', '')

                    # Insert the meal into Meals table
                    cursor.execute(
                        """
                        INSERT INTO Meals (meal_name, meal_description, instructions)
                        VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE meal_id=LAST_INSERT_ID(meal_id)
                        """,
                        (meal_name, meal_description, instructions)
                    )
                    connection.commit()
                    meal_id = cursor.lastrowid

                    # Insert ingredients into Ingredients and MealIngredients tables
                    for i in range(1, 21):  # TheMealDB API lists ingredients as strIngredient1, strIngredient2, ...
                        ingredient_name = meal.get(f'strIngredient{i}')
                        if ingredient_name:
                            # Insert into Ingredients
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

                            # Link to the Meal in MealIngredients
                            cursor.execute(
                                "INSERT IGNORE INTO MealIngredients (meal_id, ingredient_id) VALUES (%s, %s)",
                                (meal_id, ingredient_id)
                            )
                            connection.commit()

            return jsonify({"message": "Meals and ingredients added successfully"}), 201
        finally:
            connection.close()
