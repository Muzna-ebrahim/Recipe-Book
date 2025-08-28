from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Ingredient(Base):
    __tablename__ = 'ingredients'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    quantity = Column(Float, nullable=False)
    unit = Column(String)
    recipe_id = Column(Integer, ForeignKey('recipes.id'))
    
    # Relationships
    recipe = relationship("Recipe", back_populates="ingredients")
    
    def __repr__(self):
        return f"<Ingredient(id={self.id}, name='{self.name}', quantity={self.quantity}{self.unit if self.unit else ''})>"
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "quantity": self.quantity,
            "unit": self.unit,
            "recipe_id": self.recipe_id
        }