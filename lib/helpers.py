from models import Session, Category, Recipe, Ingredient
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, or_
from sqlalchemy.orm import joinedload

def exit_program():
    print("Goodbye!")
    exit()

def list_categories():
    session = Session()
    categories = session.scalars(select(Category)).all()
    session.close()
    
    if not categories:
        print("No categories found.")
        return []
    
    print("\n=== Categories ===")
    for i, cat in enumerate(categories, 1):
        print(f"{i}. {cat.name}")
    
    return categories

def find_category_by_name():
    name = input("Enter category name: ").strip()
    session = Session()
    category = session.scalars(select(Category).where(Category.name.ilike(f"%{name}%"))).first()
    session.close()
    
    if category:
        print(f"Found: {category.name}")
    else:
        print(f"Category '{name}' not found.")
    return category

def create_category():
    name = input("Enter category name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return None
    
    session = Session()
    try:
        category = Category(name=name)
        session.add(category)
        session.commit()
        print(f"Category '{name}' created!")
        return category
    except IntegrityError:
        session.rollback()
        print(f"Category '{name}' already exists.")
        return None
    finally:
        session.close()

def delete_category():
    categories = list_categories()
    if not categories:
        return
    
    try:
        choice = int(input("Enter category number to delete: "))
        if 1 <= choice <= len(categories):
            session = Session()
            session.delete(categories[choice-1])
            session.commit()
            session.close()
            print("Category deleted!")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a number.")

def list_recipes(category_id=None):
    session = Session()
    stmt = select(Recipe)
    if category_id:
        stmt = stmt.where(Recipe.category_id == category_id)
    stmt = stmt.options(joinedload(Recipe.category))
    
    recipes = session.scalars(stmt).unique().all()
    session.close()
    
    if not recipes:
        print("No recipes found.")
        return []
    
    print("\n=== Recipes ===")
    for i, recipe in enumerate(recipes, 1):
        print(f"{i}. {recipe.title} ({recipe.category.name})")
    
    return recipes

def view_recipe_details():
    recipes = list_recipes()
    if not recipes:
        return
    
    try:
        choice = int(input("Enter recipe number to view: "))
        if 1 <= choice <= len(recipes):
            session = Session()
            recipe = session.scalars(
                select(Recipe)
                .where(Recipe.id == recipes[choice-1].id)
                .options(joinedload(Recipe.category), joinedload(Recipe.ingredients))
            ).first()
            
            print(f"\n=== {recipe.title} ===")
            print(f"Category: {recipe.category.name}")
            print(f"Time: {recipe.cooking_time} minutes")
            print("\nIngredients:")
            for ing in recipe.ingredients:
                unit = ing.unit if ing.unit else ""
                print(f"- {ing.quantity} {unit} {ing.name}")
            
            print(f"\nInstructions:\n{recipe.instructions}")
            session.close()
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a number.")

def create_recipe():
    title = input("Enter recipe title: ").strip()
    if not title:
        print("Title cannot be empty.")
        return None
    
    categories = list_categories()
    if not categories:
        print("Create a category first.")
        return None
    
    try:
        cat_choice = int(input("Enter category number: "))
        if not (1 <= cat_choice <= len(categories)):
            print("Invalid category.")
            return None
    except ValueError:
        print("Please enter a number.")
        return None
    
    try:
        cooking_time = int(input("Enter cooking time (minutes): "))
    except ValueError:
        print("Time must be a number.")
        return None
    
    instructions = input("Enter instructions: ").strip()
    if not instructions:
        print("Instructions cannot be empty.")
        return None
    
    session = Session()
    try:
        recipe = Recipe(
            title=title,
            instructions=instructions,
            cooking_time=cooking_time,
            category_id=categories[cat_choice-1].id
        )
        session.add(recipe)
        
        print("Add ingredients (enter 'done' when finished):")
        while True:
            name = input("Ingredient name: ").strip()
            if name.lower() == 'done':
                break
            if not name:
                continue
            
            try:
                quantity = float(input("Quantity: "))
            except ValueError:
                print("Quantity must be a number.")
                continue
            
            unit = input("Unit (optional): ").strip()
            
            ingredient = Ingredient(
                name=name,
                quantity=quantity,
                unit=unit if unit else None,
                recipe=recipe
            )
            session.add(ingredient)
        
        session.commit()
        print(f"Recipe '{title}' created!")
        return recipe
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
        return None
    finally:
        session.close()

def delete_recipe():
    recipes = list_recipes()
    if not recipes:
        return
    
    try:
        choice = int(input("Enter recipe number to delete: "))
        if 1 <= choice <= len(recipes):
            session = Session()
            recipe = session.get(Recipe, recipes[choice-1].id)
            session.delete(recipe)
            session.commit()
            session.close()
            print("Recipe deleted!")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a number.")

def search_recipes():
    search_term = input("Search term (title or ingredient): ").strip()
    if not search_term:
        print("Search term cannot be empty.")
        return
    
    session = Session()
    stmt = select(Recipe).where(
        or_(
            Recipe.title.ilike(f"%{search_term}%"),
            Recipe.ingredients.any(Ingredient.name.ilike(f"%{search_term}%"))
        )
    ).options(joinedload(Recipe.category))
    
    recipes = session.scalars(stmt).unique().all()
    session.close()
    
    if not recipes:
        print(f"No recipes found for '{search_term}'.")
        return
    
    print(f"\n=== Recipes matching '{search_term}' ===")
    for i, recipe in enumerate(recipes, 1):
        print(f"{i}. {recipe.title} ({recipe.category.name})")

def list_recipes_by_category():
    categories = list_categories()
    if not categories:
        return
    
    try:
        choice = int(input("Enter category number: "))
        if 1 <= choice <= len(categories):
            list_recipes(categories[choice-1].id)
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a number.")