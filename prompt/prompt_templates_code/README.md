# LangChain Prompt Templates — Code Files

## Files Ka Order

| File | Topic | Kya Hai |
|------|-------|---------|
| 1_string_prompt.py | String Prompt | Sabse aasaan — sirf ek sawaal |
| 2_chat_prompt.py | Chat Prompt | System + Human — proper role |
| 3_few_shot_prompt.py | Few Shot Prompt | Examples de kar sikhana |
| 4_structured_output.py | Structured Output | Guaranteed format mein jawab |
| 5_parser.py | Parser | AI ka jawab check karna |
| 6_movie_extractor_project.py | Real Project 1 | 3 movies se info nikalna |
| 7_research_paper_explainer.py | Real Project 2 | Streamlit UI + Paper explainer |

## Setup

```bash
# 1. venv banao
python -m venv venv

# 2. Activate karo
venv\Scripts\activate  # Windows

# 3. Install karo
pip install langchain langchain-groq langchain-mistralai pydantic python-dotenv streamlit

# 4. .env file banao
GROQ_API_KEY=aapki_key_yahan
```

## Run Kaise Karein

```bash
# Normal Python files
python 1_string_prompt.py
python 2_chat_prompt.py
python 3_few_shot_prompt.py
python 4_structured_output.py
python 5_parser.py
python 6_movie_extractor_project.py

# Streamlit project
streamlit run 7_research_paper_explainer.py
```

## Teen Types Ka Farq

```
String Prompt  →  Sirf sawaal (koi role nahi)
Chat Prompt    →  System role + Human sawaal (90% yahi use hota)
Few Shot       →  Examples de kar AI ko sikhao
```

## Quick Cheatsheet

```python
# String Prompt
from langchain.prompts import PromptTemplate
template = PromptTemplate(template="{topic} batao", input_variables=["topic"])

# Chat Prompt
from langchain.prompts import ChatPromptTemplate
template = ChatPromptTemplate.from_messages([
    ("system", "Tum {role} ho"),
    ("human", "{sawaal}")
])

# Chain
from langchain.output_parsers import StrOutputParser
chain = template | model | StrOutputParser()
response = chain.invoke({"role": "doctor", "sawaal": "..."})

# Structured Output
from pydantic import BaseModel
class Info(BaseModel):
    name: str
    year: int
structured_model = model.with_structured_output(Info)
```
