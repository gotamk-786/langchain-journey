from langchain_mistralai import MistralAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = MistralAIEmbeddings(model="mistral-embed")

result = embedding.embed_query("Pakistan ka capital Islamabad hai")

print(str(result))