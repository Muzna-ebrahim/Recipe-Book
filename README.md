# Recipe Book CLI Application

A command-line interface application for managing your personal recipe collection. This application allows you to create, view, update, and delete recipes, ingredients, and categories.

## Features

1. Category Management**: Create and manage recipe categories (Appetizers, Main Courses, Desserts, etc.)
2. Recipe Management**: Add new recipes with detailed instructions and cooking times
3. Ingredient Tracking**: Associate ingredients with quantities and units to each recipe
4. Search Functionality**: Find recipes by title or ingredient name
5. Organized Viewing**: Browse recipes by category

## Installation

1. Clone or download this project
2. Navigate to the project directory
3. Install dependencies using Pipenv:
   ```bash
   pipenv install

## USAGE 
Run application python lib/cli.py
### MAIN MENU OPTIONS
1. Exit the program - Close the application
2. List all categories - View all available recipe categories
3. Find category by name - Search for a specific category
4. Create a new category - Add a new category to organize recipes
5. Delete a category - Remove a category (Note: Recipes in this category will lose their category association)
6. List all recipes - View all recipes in your collection
7. View recipe details - See full recipe including ingredients and instructions
8. Create a new recipe - Add a new recipe with its ingredients and instructions
9. Delete a recipe - Remove a recipe from your collection
10. Search recipes - Find recipes by title or ingredient name
11. List recipes by category - Browse recipes organized by category

## PROJECT STRUCTURE
Recipe-Book/
├── Pipfile                 
├── Pipfile.lock           
├── README.md              
├── alembic.ini            
├── migrations               
│   ├── env.py            
│   ├── script.py.mako    
│   └── versions        
└── lib/ 

    ├── cli.py           
    ├── debug.py           
    ├── helpers.py         
    ├── recipe_book.db     
    └── models/           
        ├── __init__.py    
        ├── recipe.py      
        ├── ingredient.py  
        └── category.py    

## MODELS
  1. Recipe Represents a recipe with title, instructions, and cooking time
  2. Ingredient Represents an ingredient with quantity and unit
  3. Category Represents a category for organizing recipes (e.g., "Desserts", "Main Courses")

## License
This project is licensed under the MIT License.

## CONTRIBUTIONS
All contributions are allowed and appreciated.

## Author
This project was done by Muzna Ebrahim Mohamed.