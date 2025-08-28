#!/usr/bin/env python3

from helpers import (
    exit_program,
    list_categories,
    find_category_by_name,
    create_category,
    delete_category,
    list_recipes,
    view_recipe_details,
    create_recipe,
    delete_recipe,
    search_recipes,
    list_recipes_by_category
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_categories()
        elif choice == "2":
            find_category_by_name()
        elif choice == "3":
            create_category()
        elif choice == "4":
            delete_category()
        elif choice == "5":
            list_recipes()
        elif choice == "6":
            view_recipe_details()
        elif choice == "7":
            create_recipe()
        elif choice == "8":
            delete_recipe()
        elif choice == "9":
            search_recipes()
        elif choice == "10":
            list_recipes_by_category()
        else:
            print("Invalid choice. Please try again.")
        
        input("\nPress Enter to continue...")

def menu():
    print("\n" + "="*50)
    print("RECIPE BOOK MANAGEMENT SYSTEM")
    print("="*50)
    print("0. Exit the program")
    print("1. List all categories")
    print("2. Find category by name")
    print("3. Create a new category")
    print("4. Delete a category")
    print("5. List all recipes")
    print("6. View recipe details")
    print("7. Create a new recipe")
    print("8. Delete a recipe")
    print("9. Search recipes")
    print("10. List recipes by category")
    print("="*50)
    print("Please select an option:")

if __name__ == "__main__":
    # Initialize database
    from models import create_db
    create_db()
    
    # Add some sample data if database is empty
    from models import Session, Category
    session = Session()
    if session.query(Category).count() == 0:
        sample_categories = ["Appetizers", "Main Courses", "Desserts", "Beverages", "Salads"]
        for cat_name in sample_categories:
            session.add(Category(name=cat_name))
        session.commit()
        print("Sample categories added to the database.")
    session.close()
    
    main()