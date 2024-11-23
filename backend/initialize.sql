-- Drop the existing database if it exists
DROP DATABASE IF EXISTS PantryPal;

-- Create the database and select it
CREATE DATABASE PantryPal;
USE PantryPal;

-- Users table
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    user_password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Ingredients table
CREATE TABLE Ingredients (
    ingredient_id INT AUTO_INCREMENT PRIMARY KEY,
    ingredient_name VARCHAR(255) NOT NULL UNIQUE
);

-- Meals table
CREATE TABLE Meals (
    meal_id INT AUTO_INCREMENT PRIMARY KEY,
    meal_name VARCHAR(255) NOT NULL,
    meal_description TEXT,
    instructions TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- MealIngredients table
CREATE TABLE MealIngredients (
    meal_ingredient_id INT AUTO_INCREMENT PRIMARY KEY,
    meal_id INT NOT NULL,
    ingredient_id INT NOT NULL,
    FOREIGN KEY (meal_id) REFERENCES Meals(meal_id) ON DELETE CASCADE,
    FOREIGN KEY (ingredient_id) REFERENCES Ingredients(ingredient_id) ON DELETE CASCADE,
    UNIQUE (meal_id, ingredient_id)
);

-- UserIngredients table
CREATE TABLE UserIngredients (
    user_ingredient_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    ingredient_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (ingredient_id) REFERENCES Ingredients(ingredient_id) ON DELETE CASCADE,
    UNIQUE (user_id, ingredient_id)
);


