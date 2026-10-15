from pydantic import BaseModel

class Recipe(BaseModel):
    recipe_name: str 
    ingredients: list[str]
    instructions: list[str]
