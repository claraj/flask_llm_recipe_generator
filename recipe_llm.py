from google import genai 
from google.genai.types import GenerateContentConfig
import os 
from model import Recipe
import logging as log


GOOGLE_API_KEY = os.environ.get('GEMINI_API_KEY')
client = genai.Client(api_key=GOOGLE_API_KEY)

# TODO read this from a file 
system_instruction = """Use the ingredients given to create a recipe"""

def generate_recipe(ingredients):

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash', 
            contents=ingredients,
            config=GenerateContentConfig(
                system_instruction=system_instruction,
                response_mime_type='application/json',
                response_schema=Recipe,
                )
        )

        return response.parsed, None 
    
    except Exception as e:
        log.exception(f'Error making LLM request for ingredients "{ingredients}"')
        return None, e 
    