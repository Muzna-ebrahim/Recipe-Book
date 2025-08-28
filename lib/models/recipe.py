from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Recipe(Base):
    __tablename__ = 'recipes'
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    instructions = Column(Text, nullable=False)
    cooking_time = Column(Integer)  # in minutes
    category_id = Column(Integer, ForeignKey('categories.id'))
    
    # Relationships
    category = relationship("Category", back_populates="recipes")
    ingredients = relationship("Ingredient", back_populates="recipe", cascade="all, delete-orphan")
    
    def __repr__(self):
        return f"<Recipe(id={self.id}, title='{self.title}', category_id={self.category_id})>"
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "instructions": self.instructions,
            "cooking_time": self.cooking_time,
            "category_id": self.category_id,
            "ingredients": [ingredient.to_dict() for ingredient in self.ingredients]
        }