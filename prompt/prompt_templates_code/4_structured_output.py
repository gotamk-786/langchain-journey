# ============================================
# STRUCTURED OUTPUT
# Guaranteed format mein jawab lo
# Normal string nahi — proper object milta hai
# ============================================

from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv

load_dotenv()

model = ChatMistralAI(model="mistral-small-2503")

# ─── Example 1: Movie Info Extractor ───

# Step 1: Structure define karo
class MovieInfo(BaseModel):
    movie_name:    str    # string
    year:          int    # number
    director:      str    # string
    cast:          str    # string
    genre:         str    # string
    imdb_rating:   float  # decimal
    quick_summary: str    # string

# Step 2: Structured model banao
structured_model = model.with_structured_output(MovieInfo)

# Step 3: Paragraph do
paragraph = """
Interstellar is a visually stunning science fiction epic directed by Christopher Nolan.
Released in 2014, the film stars Matthew McConaughey, Anne Hathaway, Jessica Chastain,
and Michael Caine. It holds a rating of 8.6 on IMDb and is often considered one of the
greatest sci-fi films of the 21st century.
"""

response = structured_model.invoke(paragraph)

# Step 4: Seedha access karo
print("Movie Info:")
print(f"Name:    {response.movie_name}")
print(f"Year:    {response.year}")
print(f"Director:{response.director}")
print(f"Rating:  {response.imdb_rating}")
print(f"Summary: {response.quick_summary}")
print("-" * 50)

# ─── Example 2: Multiple Movies Loop ───

class MovieList(BaseModel):
    movie_name:  str
    director:    str
    imdb_rating: float

structured_model2 = model.with_structured_output(MovieList)

movies = [
    "The Dark Knight (2008) directed by Christopher Nolan. IMDb 9.0. Stars Christian Bale.",
    "3 Idiots (2009) directed by Rajkumar Hirani. IMDb 8.4. Stars Aamir Khan.",
]

print("All Movies:")
for i, movie in enumerate(movies, 1):
    result = structured_model2.invoke(movie)
    print(f"{i}. {result.movie_name} | {result.director} | {result.imdb_rating}")
