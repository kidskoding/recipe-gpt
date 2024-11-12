import openai
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

client = openai

recipe_name = input("What recipe would you like to know about?")

completion = client.chat.completions.create(
    model="gpt-40-mini",
    messages=[
        {"role": "system", "content": "A helpful assistant that provides recipes."},
        {
            "role": "user",
            "content": f"What are the ingredients, instructions, and estimated cooking time for {recipe_name}?"
        }
    ]
)

print(completion.choices[0].message['content'])