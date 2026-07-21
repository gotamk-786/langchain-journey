from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# Initialize Model
model = ChatMistralAI(
    model="mistral-small-2503"
)

# Create Prompt
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are an expert Information Extraction Assistant.

Your task is to carefully analyze the given paragraph and extract the most useful information.

Rules:

1. Read the entire paragraph carefully.
2. Extract only explicitly mentioned information.
3. Do not assume or hallucinate missing facts.
4. If information is missing, write "Not Mentioned".
5. Keep the response clean and well organized.
6. Use headings and bullet points.
7. Preserve names, dates, ratings, and numbers exactly as written.
8. Generate a concise Quick Summary (2-4 sentences).

Extract the following information:

- Title / Name
- Document Type
- Genre
- Release Year
- Director
- Author / Creator
- Producer
- Main Cast
- Main Characters
- Plot / Main Idea
- Setting
- Themes
- Organizations
- Locations
- Ratings
- Awards
- Soundtrack
- Key Features
- Keywords
- Overall Sentiment

Finally generate a Quick Summary.
        """
    ),
    (
        "human",
        """
Analyze the following paragraph and extract all useful information.

Paragraph:

{paragraph}
        """
    )
])

# Create Messages
para=input("Give your paragraph: ")

final_propmt=prompt.invoke(
    {"paragraph":para}
)


# Invoke Model
response = model.invoke(final_propmt)

print(response.content)