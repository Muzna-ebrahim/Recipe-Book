#!/usr/bin/env python3

from models import Session, Category, Recipe, Ingredient, create_db, drop_db
from faker import Faker
import random

fake = Faker()

def seed_database():
    drop_db()
    create_db()
    
    session = Session()
    
    # Create categories
    categories = [
        Category(name="Appetizers"),
        Category(name="Main Courses"),
        Category(name="Desserts"),
        Category(name="Beverages"),
        Category(name="Salads")
    ]
    
    for category in categories:
        session.add(category)
    
    session.commit()
    
    # Create recipes with ingredients
    units = ["cup", "tbsp", "tsp", "oz", "lb", "g", "kg", "ml", "l", "", "piece", "clove"]
    ingredients_list = [
        "flour", "sugar", "salt", "pepper", "butter", "oil", "water", "milk", "eggs",
        "chicken", "beef", "pork", "fish", "rice", "pasta", "tomato", "onion", "garlic",
        "carrot", "potato", "cheese", "cream", "vanilla", "chocolate", "lemon", "lime"
    ]
    
    for _ in range(20):
        category = random.choice(categories)
        recipe = Recipe(
            title=fake.catch_phrase(),
            instructions=fake.text(max_nb_chars=200),
            cooking_time=random.randint(10, 120),
            category_id=category.id
        )
        session.add(recipe)
        session.flush()  # To get the recipe ID
        
        # Add 3-7 ingredients to each recipe
        for _ in range(random.randint(3, 7)):
            ingredient = Ingredient(
                name=random.choice(ingredients_list),
                quantity=round(random.uniform(0.5, 4.0), 1),
                unit=random.choice(units),
                recipe_id=recipe.id
            )
            session.add(ingredient)
    
    session.commit()
    session.close()
    print("Database seeded with sample data!")

if __name__ == "__main__":
    seed_database()