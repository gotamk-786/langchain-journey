from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

# Initialize Model
model = ChatMistralAI(
    model="mistral-small-2503"
)

# Pydantic Schema
class Movie(BaseModel):
    Title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str


# Output Parser
parser = PydanticOutputParser(pydantic_object=Movie)

# Prompt
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an expert movie information extractor.

Extract the movie information from the given paragraph.

{format_instructions}
            """
        ),
        (
            "human",
            "{paragraph}"
        )
    ]
)

# User Input
para = input("Give your paragraph: ")

# Format Prompt
final_prompt = prompt.invoke(
    {
        "paragraph": para,
        "format_instructions": parser.get_format_instructions()
    }
)

# Invoke Model
response = model.invoke(final_prompt)

# Parse Output
movie = parser.parse(response.content)

print(movie)